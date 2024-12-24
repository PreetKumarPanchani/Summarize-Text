from TextSummarizer.config.configuration import ConfigManager
from TextSummarizer.components.data_validation import DataValidation
from TextSummarizer.logging import logger
from TextSummarizer.constants import CONFIG_FILE_PATH, PARAMS_FILE_PATH


class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):

        config_path= CONFIG_FILE_PATH 
        params_path = PARAMS_FILE_PATH
        
        conf_manager = ConfigManager( config_path , params_path )

        data_validation_config = conf_manager.get_data_validation_config()
        data_validation = DataValidation(data_validation_config)
        data_validation.validate_all_files_exists()

