from textsummarizer.logging import logger


from textsummarizer.pipeline.state_01_data_ingestion import DataIngestionTrainingPipeline
from textsummarizer.pipeline.state_02_data_validation  import DataValiationTrainingPipeline
from textsummarizer.pipeline.state_03_data_transformation  import DataTransformationTrainingPipeline
from textsummarizer.pipeline.state_04_model_trainer  import ModelTrainerTrainingPipeline

STAGE_NAME = "Data Ingestion Stage"
#try:
  #  logger.info(f">>>>>>>>>>>>stage {STAGE_NAME} started <<<<<<<<<<")
 #  data_ingestion = DataIngestionTrainingPipeline()
  #  data_ingestion.main()
  #  logger.info(f"{STAGE_NAME} completed successfully")
#except Exception as e:
#    logger.exception(e)
 #   raise e


STAGE_NAME = "Data Validation Stage"
#try:
 #   logger.info(f">>>>>>>>>>>>stage {STAGE_NAME} started <<<<<<<<<<")
 #   data_validation = DataValiationTrainingPipeline()
 #   data_validation.main()
 #   logger.info(f"{STAGE_NAME} completed successfully")
#except Exception as e:
 #   logger.exception(e)
 #   raise e

# STAGE_NAME = "Data Transformation Stage"
# try:
#     logger.info(f">>>>>>>>>>>>stage {STAGE_NAME} started <<<<<<<<<<")
#     data_transformation = DataTransformationTrainingPipeline()
#     data_transformation.main()
#     logger.info(f"{STAGE_NAME} completed successfully")
# except Exception as e:
#     logger.exception(e)
#     raise e

STAGE_NAME = "Model Training Stage"
try:
    logger.info(f">>>>>>>>>>>>stage {STAGE_NAME} started <<<<<<<<<<")
    model_trainer = ModelTrainerTrainingPipeline()
    model_trainer.main()
    logger.info(f"{STAGE_NAME} completed successfully")
except Exception as e:
    logger.exception(e)
    raise e