import os
import urllib.request as request
import zipfile
from pathlib import Path
#import importlib
#import TextSummarizer.utils.common
#importlib.reload(TextSummarizer.utils.common)

from TextSummarizer.logging import logger
from TextSummarizer.utils.common import get_size
from TextSummarizer.entity import ( DataIngestionConfig) 

class DataIngestion:
    def __init__(self, config: DataIngestionConfig ):
        self.config = config
    
    def download_file( self):#
        if not os.path.exists(self.config.local_data_file):
            
            print('source_URL::', self.config.source_URL)
            print( 'local_data_file::', self.config.local_data_file)

            filename , headers  = request.urlretrieve( self.config.source_URL , self.config.local_data_file )
            logger.info(f'{filename} downloaded , with following info: {headers}')
        else:
            logger.info(f'file already exist  , with size as : {get_size( Path(self.config.local_data_file))} ')


    def extract_zip_file( self):
        """
        Extracts the zip file into the Data Directory 

        zip_file_path : str

        """
        
        unzip_path = self.config.unzip_dir 
        os.makedirs( unzip_path , exist_ok= True  )

        with zipfile.ZipFile( self.config.local_data_file, 'r' ) as zip_ref:
            zip_ref.extractall(unzip_path)
        


    

