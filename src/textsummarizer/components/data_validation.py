import os
from textsummarizer.logging import logger
from textsummarizer.config.configuration import DataValidationConfig

class  DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config
       
    def validate_all_files_exists(self)->bool:
        try:
            validation_status = None

            all_files= os.listdir(self.config.DATA_SOURCE_DIR)
           
            for file in all_files:
                    # Check if it's the first JSON file and skip it
                if file.endswith('.json')  :
                    continue
            
                if file not in self.config.ALL_REQUIRED_FILES:
                    validation_status = False
                    logger.info(f"{file} not eixts")
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation status: {validation_status}")
                        break
                else:
                    validation_status = True
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation status: {validation_status}")
            return validation_status   
        except Exception as e:      
            raise e