import os
from box.exceptions import BoxValueError
import yaml
from textsummarizer.logging import logger
from box import ConfigBox
from pathlib import Path
from ensure import ensure_annotations
from typing import Any


@ensure_annotations
def read_yaml(path_to_yaml:Path)-> ConfigBox:

    try:
        with open(path_to_yaml, 'r') as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaanl file:{path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        logger.error(f"File not found: {path_to_yaml}")
        raise ValueError("yaml file is empty")
    except Exception as e:
        logger.error(f"An error occurred while reading YAML: {path_to_yaml}")
        raise e

@ensure_annotations
def create_directories(path_to_directiories: list, verbose=True):
    for path in path_to_directiories:
        os.makedirs(path, exist_ok=True)
       
        if verbose:
            logger.info(f"Created directory: {path}")



@ensure_annotations
def get_size(pah: Path) -> str:
    size_in_kb = round(pah.lstat().st_size/1024)
    return f"{size_in_kb} KB"