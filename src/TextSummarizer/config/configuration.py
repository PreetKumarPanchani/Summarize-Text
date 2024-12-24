
import os
from pathlib import Path

# Restart your Python environment or kernel.
#import importlib
#import TextSummarizer.constants
#import TextSummarizer.utils.common
#import TextSummarizer.entity

#importlib.reload(TextSummarizer.entity)
#importlib.reload(TextSummarizer.utils.common)
#importlib.reload(TextSummarizer.constants)

from TextSummarizer.constants import CONFIG_FILE_PATH, PARAMS_FILE_PATH
from TextSummarizer.utils.common import *
from TextSummarizer.entity import ( DataIngestionConfig, DataValidationConfig, DataTransformationConfig , ModelTrainerConfig) 


class ConfigManager:
    def __init__(self, config_path= CONFIG_FILE_PATH , params_path = PARAMS_FILE_PATH  ):

        #with open(config_path, 'r') as yaml_file:
        #    content = yaml.safe_load(yaml_file)
        #    print(f"Type of parsed content: {type(content)}")
        #    print(f"Content: {content}")


        self.config = read_yaml_file(config_path)
        self.params = read_yaml_file(params_path)

        # Create dir for 'artifacts' and 'artifacts/data_validation' folder
        create_directries( [self.config.artifacts_root , self.config.data_validation.root_dir , self.config.data_transformation.root_dir ]  )    



    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directries( [ config.root_dir , ]  )   # Create dir for 'artifacts/data ingestion' folder

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir 
        )

        return data_ingestion_config
    

   
    def get_data_validation_config(self) -> DataValidationConfig:

        config = self.config.data_validation

        data_ingestion_config = DataValidationConfig(
                
                root_dir = config.root_dir,
                STATUS_FILE = config.STATUS_FILE,
                ALL_REQUIRED_FILES = config.ALL_REQUIRED_FILES,

        )

        return data_ingestion_config



    def get_data_transformation_config(self) -> DataTransformationConfig:

        config = self.config.data_transformation
        

        data_transformation_config = DataTransformationConfig(
                
                root_dir  = config.root_dir,
                data_path = config.data_path,
                tokenizer_name = config.tokenizer_name,
        )

        return data_transformation_config



    def get_model_trainer_config(self) -> ModelTrainerConfig:
          
        config = self.config.model_trainer
        params = self.params.TrainingArguments
        
        create_directries([config.root_dir])

        model_trainer_config = ModelTrainerConfig( 
    
            root_dir   =  config.root_dir, 
            data_path  = config.data_path ,
            model_ckpt = config.model_ckpt ,

            num_train_epochs =  params.num_train_epochs,
            warmup_steps  = params.warmup_steps ,
            per_device_train_batch_size =  params.per_device_train_batch_size ,
            weight_decay  = params.weight_decay ,
            logging_steps = params.logging_steps , 
            evaluation_strategy =  params.evaluation_strategy ,
            eval_steps = params.eval_steps ,
            save_steps = params.save_steps ,
            gradient_accumulation_steps = params.gradient_accumulation_steps ,

        )

        return model_trainer_config





