from textsummarizer.components.data_ingestion import DataIngestion
from textsummarizer.config.configuration import ConfigrationManager
from textsummarizer.utils.common import logger
#create the pipeline

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
         
        config = ConfigrationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config = data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()
        