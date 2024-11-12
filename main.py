from textsummarizer.logging import logger


from textsummarizer.pipeline.state_01_data_ingestion import DataIngestionTrainingPipeline
from textsummarizer.pipeline.state_02_data_validation  import DataValiationTrainingPipeline

STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>>>>>>>>>>stage {STAGE_NAME} started <<<<<<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f"{STAGE_NAME} completed successfully")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data Validation Stage"
try:
    logger.info(f">>>>>>>>>>>>stage {STAGE_NAME} started <<<<<<<<<<")
    data_validation = DataValiationTrainingPipeline()
    data_validation.main()
    logger.info(f"{STAGE_NAME} completed successfully")
except Exception as e:
    logger.exception(e)
    raise e