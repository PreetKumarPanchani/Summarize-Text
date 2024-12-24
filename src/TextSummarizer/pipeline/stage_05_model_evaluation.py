from TextSummarizer.config.configuration import ConfigManager
from TextSummarizer.constants import CONFIG_FILE_PATH, PARAMS_FILE_PATH
from TextSummarizer.components.model_evaluation import ModelEvaluation

class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def main(self):

        config_path= CONFIG_FILE_PATH 
        params_path = PARAMS_FILE_PATH
        
        config = ConfigManager(config_path , params_path )
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation_config = ModelEvaluation(config=model_evaluation_config)
        model_evaluation_config.evaluate()

        