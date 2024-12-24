from TextSummarizer.config.configuration import ConfigManager
from TextSummarizer.components.data_transformation import DataTransformation
from TextSummarizer.logging import logger
from TextSummarizer.constants import CONFIG_FILE_PATH, PARAMS_FILE_PATH
from TextSummarizer.components.model_trainer import ModelTrainer

class ModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self, training_data_name):

        config_path= CONFIG_FILE_PATH 
        params_path = PARAMS_FILE_PATH
        
        config_path= CONFIG_FILE_PATH 
        params_path = PARAMS_FILE_PATH
        config = ConfigManager(config_path , params_path )
        model_trainer_config = config.get_model_trainer_config()
        model_trainer_config = ModelTrainer(config=model_trainer_config)
        model_trainer_config.train(training_data_name)
