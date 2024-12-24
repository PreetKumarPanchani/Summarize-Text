from TextSummarizer.config.configuration import ConfigManager
from TextSummarizer.components.data_transformation import DataTransformation
from TextSummarizer.logging import logger
from TextSummarizer.constants import CONFIG_FILE_PATH, PARAMS_FILE_PATH


class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):

        config_path= CONFIG_FILE_PATH 
        params_path = PARAMS_FILE_PATH
        
        conf_manager = ConfigManager( config_path , params_path )

        data_transformation_config = conf_manager.get_data_transformation_config()
        data_transformation = DataTransformation(data_transformation_config)
        data_transformation.convert()


