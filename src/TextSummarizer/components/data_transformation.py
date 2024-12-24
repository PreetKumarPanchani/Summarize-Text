import os
import urllib.request as request

from TextSummarizer.logging import logger
from TextSummarizer.utils.common import get_size
from transformers import AutoTokenizer
from datasets import load_dataset, load_from_disk 
from TextSummarizer.entity import (  DataTransformationConfig) 



## Applying Tokenizer on Input and Target and then applying Masking, and taking only unmasked inputs and targets
class DataTransformation:
    def __init__(self, config: DataTransformationConfig ):
        self.config = config
        self.tokenizer = AutoTokenizer.from_pretrained(config.tokenizer_name)
    
    def convert( self):
        dataset_samsum = load_from_disk( self.config.data_path )
        dataset_samsum_pt =  dataset_samsum.map( self.convert_examples_to_features , batched= True)
        dataset_samsum_pt.save_to_disk( os.path.join( self.config.root_dir , "samsun_dataset" ))


    def convert_examples_to_features( self, example_batch):

        input_encodings = self.tokenizer( example_batch['dialogue'] , max_length=1024, truncation=True, padding='max_length')
        
        with self.tokenizer.as_target_tokenizer():
            target_encodings = self.tokenizer( example_batch['summary'] , max_length=1024, truncation=True, padding='max_length' )
        
        #print('input_encodings_unmasked:::' , input_encodings['input_ids'] )
        #print('masked_input_encodings:::' , input_encodings['attention_mask'] )
        #print('target_encodings_unmasked:::' , target_encodings['input_ids'] )

        return {
                'input_ids':  input_encodings['input_ids']   , 
                'attention_mask': input_encodings['attention_mask'] ,
                'labels' : target_encodings['input_ids'] ,  
                
                }

