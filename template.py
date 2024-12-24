import os
import sys
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format="[%(asctime)s]: %(message)s")

project_name = "TextSummarizer"

list_of_files = [
    ".github/workflows/.gitkeep" ,         # Empty Folders will not be Uploaded in the GITHUB 
    f"src/{project_name}/__init__.py",     # For import purposes
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/common.py",     # To have common fn and Classes
    f"src/{project_name}/logging/__init__.py",  # For logging
    f"src/{project_name}/config/__init__.py",  
    f"src/{project_name}/config/configuration.py",  # For configuration
    f"src/{project_name}/pipeline/__init__.py",  # For Training and Predication Pipeline
    f"src/{project_name}/entity/__init__.py",  # For 
    f"src/{project_name}/constants/__init__.py",  # For 
    "config/config.yaml" ,                        # For configuration in YAML
    "params.yaml",                                # For Parameter in YAML
    "app.py",
    "main.py",                                     
    "Dockerfile",                                 # Helps in the Docker Image Creation
    "requirements.txt",                           # For Including the Libraries to be used in the Project
    "setup.py",                                   # For setup the Local Packages and Installations
    "research/trails.ipynb",                      # For testing the code ( Sub functions , classes and modules before putting in the real code Directries)
    "test.py" , 

]


for filepath in list_of_files:
    filepath = Path( filepath)                                       # Gives the Path based on the OS as different OS has different File Path Formats ==> It gives Object as WindowsPath('')
    filedir , filename  = os.path.split( filepath )
    
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Created directory: {filedir} for the file {filename}")


    if ( not ( os.path.exists( filename ) ) or os.path.getsize(filename ) == 0):
        with open( filepath , 'w' ) as f:
            pass
        logging.info(f"Creating empty file: {filepath} ")


    else:
        logging.info(f" File {filepath} already exists ")





