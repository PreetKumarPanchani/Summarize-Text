from TextSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from TextSummarizer.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from TextSummarizer.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from TextSummarizer.pipeline.stage_04_model_trainer import ModelTrainingPipeline
from TextSummarizer.pipeline.stage_05_model_evaluation import ModelEvaluationPipeline

from TextSummarizer.logging import logger


STAGE_NAME = "DATA INGESTION STAGE"

try:
    logger.info(f"Starting {STAGE_NAME}")
    data_ingestion_pipeline = DataIngestionTrainingPipeline()
    data_ingestion_pipeline.main()
    logger.info(f"Completed the  {STAGE_NAME}")

except Exception as e:
    logger.exception(e)
    raise e



STAGE_NAME = "DATA VALIDATION STAGE"

try:
    logger.info(f"Starting {STAGE_NAME}")
    data_validation_pipeline = DataValidationTrainingPipeline()
    data_validation_pipeline.main()
    logger.info(f"Completed the  {STAGE_NAME}")
    
except Exception as e:
    logger.exception(e)
    raise e




STAGE_NAME = "DATA TRANSFORMATION STAGE"

try:
    logger.info(f"Starting {STAGE_NAME}")
    data_transformation_pipeline = DataTransformationTrainingPipeline()
    data_transformation_pipeline.main()
    logger.info(f"Completed the  {STAGE_NAME}")
    
except Exception as e:
    logger.exception(e)
    raise e




STAGE_NAME = "MODEL TRAINER STAGE"

try:
    logger.info(f"Starting {STAGE_NAME}")
    model_training_pipeline = ModelTrainingPipeline()
    model_training_pipeline.main(training_data_name = 'test')
    logger.info(f"Completed the  {STAGE_NAME}")
    
except Exception as e:
    logger.exception(e)
    raise e




STAGE_NAME = "MODEL EVALUATION STAGE"

try:
    logger.info(f"Starting {STAGE_NAME}")
    model_evaluation_pipeline = ModelEvaluationPipeline()
    model_evaluation_pipeline.main()
    logger.info(f"Completed the  {STAGE_NAME}")
    
except Exception as e:
    logger.exception(e)
    raise e
