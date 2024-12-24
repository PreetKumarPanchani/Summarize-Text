from TextSummarizer.config.configuration import ConfigManager
from TextSummarizer.components.data_ingestion import DataIngestion
from TextSummarizer.logging import logger
from TextSummarizer.constants import CONFIG_FILE_PATH, PARAMS_FILE_PATH


class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):

        config_path= CONFIG_FILE_PATH 
        params_path = PARAMS_FILE_PATH
        
        conf_manager = ConfigManager( config_path , params_path )

        data_ingestion_config = conf_manager.get_data_ingestion_config()
        data_ingestion = DataIngestion(data_ingestion_config)#
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()

