## It contains the File Path for the Config and Params YAML Files
from pathlib import Path

CONFIG_FILE_PATH = Path( "config/config.yaml")
PARAMS_FILE_PATH = Path( "params.yaml")

'''
# src/TextSummarizer/constants/__init__.py
import os
from pathlib import Path

# Get the src directory path
SRC_DIR = Path(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
ROOT_DIR = Path(os.path.dirname(SRC_DIR))

# Define the paths
CONFIG_FILE_PATH = ROOT_DIR / "config" / "config.yaml"
PARAMS_FILE_PATH = ROOT_DIR / "params.yaml"

# Print paths for debugging
print(f"SRC_DIR: {SRC_DIR}")
print(f"ROOT_DIR: {ROOT_DIR}")
print(f"CONFIG_FILE_PATH: {CONFIG_FILE_PATH}")
print(f"PARAMS_FILE_PATH: {PARAMS_FILE_PATH}")

# Make sure these variables are exported
__all__ = ['CONFIG_FILE_PATH', 'PARAMS_FILE_PATH']
'''