import os
import sys
import logging

## Logging Format
logging_str = "[%(asctime)s : %(levelname)s : %(module)s :  %(message)s]"  # Time, loggging Type, Module and Message

## Logging File Path AND Directry
log_dir = 'logs'
log_filepath = os.path.join(log_dir, "running_logs.log")

os.makedirs(log_dir , exist_ok= True)

## Define Logging Configuration
logging.basicConfig(
    level = logging.INFO , format = logging_str ,
    handlers = [ logging.FileHandler(log_filepath)  , 
                logging.StreamHandler(sys.stdout)    ]  # To display in Terminal as well  , use logging.StreamHandler(sys.stdout)
)

# Create a Logger
logger = logging.getLogger("textSummarizerLogger")




