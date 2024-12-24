import os
import torch 
from TextSummarizer.logging import logger
from transformers import TrainingArguments , Trainer  
from transformers import DataCollatorForSeq2Seq
from transformers import AutoModelForSeq2SeqLM , AutoTokenizer
from datasets import load_from_disk 
from TextSummarizer.entity import ( ModelTrainerConfig)

class ModelTrainer:
    def __init__(self , config: ModelTrainerConfig):
        self.config = config

    def train(self, training_data_name ):

        assert training_data_name== 'train' or training_data_name== 'test' or training_data_name== 'validation'
        print(f'Using {training_data_name} Dataset for training the Model ')
        
        ## Call the Device, Tokenizer , Model( Seq2SeqLM ), DataCollator
        device = 'cuda' if torch.cuda.is_available() else 'cpu'
        tokenizer = AutoTokenizer.from_pretrained(self.config.model_ckpt)
        model_pegasus = AutoModelForSeq2SeqLM.from_pretrained( self.config.model_ckpt).to(device)
        seq2seq_data_collator = DataCollatorForSeq2Seq( tokenizer, model =model_pegasus  )

        logger.info(f"Training on {device}")
        
        ## Loading Data
        dataset_samsum_pt = load_from_disk( self.config.data_path)

        ## Training Arguments
        trainer_args = TrainingArguments(
            output_dir=self.config.root_dir, num_train_epochs=1, warmup_steps=500,
            per_device_train_batch_size=1, per_device_eval_batch_size=1,
            weight_decay=0.01, logging_steps=10,
            evaluation_strategy='steps', eval_steps=500, save_steps=1e6,
            gradient_accumulation_steps=16
        ) 

        ## Trainer 
        trainer = Trainer( model =  model_pegasus , args =  trainer_args ,
                           tokenizer = tokenizer  , data_collator  = seq2seq_data_collator, 
                           train_dataset = dataset_samsum_pt[training_data_name]  ,
                           eval_dataset = dataset_samsum_pt['validation']  
                        
                          )
     
        ## Train the model 
        trainer.train()

        ## Save Model
        model_pegasus.save_pretrained(os.path.join(self.config.root_dir,"pegasus-samsum-model"))

        ## Save Tokenzier
        tokenizer.save_pretrained(os.path.join(self.config.root_dir,"tokenizer"))





