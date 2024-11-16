from textsummarizer.config.configuration import ConfigurationManager
from textsummarizer.components.data_transformation import DataTransformation


class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_Transformation_config = config.get_data_transformation_config()
        data_Transformation = DataTransformation(config = data_Transformation_config)
        data_Transformation.convert()