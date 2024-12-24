import os
from box.exceptions import BoxValueError
import yaml 
from TextSummarizer.logging import logger
from ensure import ensure_annotations
from box import Box, ConfigBox
from pathlib import Path 
from typing import Any


## If Incorrect Return Type or Incorrect Input Type then it Returns an Error hence Ensuring Correct Annotations using @ensure_annotations Decorator

@ensure_annotations
def read_yaml_file(path_to_yaml: Path) -> ConfigBox:
    """reads yaml file and returns

    Args:
        path_to_yaml (str): path like input

    Raises:
        ValueError: if yaml file is empty
        e: empty file

    Returns:
        ConfigBox: ConfigBox type
    """
    try:
        #print('path_to_yamllllllllllllllllllllllllllllll',path_to_yaml)
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            #print(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    


@ensure_annotations
def create_directries(path_to_directories: list , verbose= True ):
    """
    Create a List of Directories.

    Args:
        path_to_directories (list)     : The list of Path Directories
        ignore_log ( bool , optional ) : Ignore if Multiple Dirs to be created. Default to True

    """

    for filepath in path_to_directories:
        os.makedirs( filepath , exist_ok=True )
        if verbose:
            logger.info( f"Directory {filepath} created successfully.")





@ensure_annotations
def get_size( filepath: Path ) -> str:
    """
    Get Size in KB.

    Args:
        filepath (Path)  : The Path Of Directory

    Returns:
        str              : Get Size in KB.
    """

    size_in_KB = round( os.path.getsize(filepath) / 1024 )
    return f"{size_in_KB} KB"
    














