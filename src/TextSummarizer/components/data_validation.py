from dataclasses import dataclass
from pathlib import Path
from TextSummarizer.constants import CONFIG_FILE_PATH, PARAMS_FILE_PATH
from TextSummarizer.utils.common import *
from TextSummarizer.entity import (  DataValidationConfig) 



## Data Validation Class

class DataValidation:
    def __init__(self, config: DataValidationConfig ):
        self.config = config
    
    def validate_all_files_exists( self) -> bool:#

        all_required_files = self.config.ALL_REQUIRED_FILES

        try:
            validation_status = None
                    
            all_files = os.listdir( os.path.join("artifacts" , "data-ingestion" , "samsum_dataset") )

            for file in all_files:
                if file not in all_required_files:
                    validation_status = False


                else:
                    validation_status = True

            with open(self.config.STATUS_FILE , 'w') as f:
                f.write( f"Validation status, {validation_status}")
            
            return validation_status
            
        except Exception as e:

            raise e
    
