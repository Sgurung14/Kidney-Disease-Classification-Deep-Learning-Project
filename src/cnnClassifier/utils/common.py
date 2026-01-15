import os
from box.exceptions import BoxValueError
import yaml
from cnnClassifier import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """Reads a yaml file and returns

    Args:
        path_to_yaml (Path): Path to yaml file

    Returns:
        ConfigBox: ConfigBox type object
    """
    try:
        with open(path_to_yaml, 'r') as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError as e:
        raise ValueError(f"Error while converting yaml to ConfigBox: {e}")
    except Exception as e:
        raise e
    
@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """Creates list of directories

    Args:
        path_to_directories (list[Path]): List of directory paths
    """
    for path_to_directory in path_to_directories:
        os.makedirs(path_to_directory, exist_ok=True)
        if verbose:
            logger.info(f"Created directory at: {path_to_directory}")

@ensure_annotations
def save_json(path: Path, data: dict) -> None:
    """Saves dictionary data to a json file

    Args:
        path (Path): Path to the json file
        data (dict[str, Any]): Data to be saved
    """
    with open(path, 'w') as json_file:
        json.dump(data, json_file, indent=4)

    logger.info(f"JSON file saved at: {path}")

@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """Loads json file and returns as ConfigBox

    Args:
        path (Path): Path to the json file

    Returns:
        ConfigBox: ConfigBox type object
    """
    with open(path, 'r') as json_file:
        content = json.load(json_file)

    logger.info(f"JSON file loaded from: {path}")
    return ConfigBox(content)   

@ensure_annotations
def save_bin(data: Any, path: Path) -> None:
    """Saves binary data to a file

    Args:
        data (Any): Data to be saved
        path (Path): Path to the binary file
    """
    joblib.dump(data, path)
    logger.info(f"Binary file saved at: {path}") 

@ensure_annotations
def load_bin(path: Path) -> Any:
    """Loads binary data from a file

    Args:
        path (Path): Path to the binary file

    Returns:
        Any: Object stored in the file
    """
    data = joblib.load(path)
    logger.info(f"Binary file loaded from: {path}")
    return data

@ensure_annotations
def get_size(path: Path) -> str:
    """Returns size of file in KB

    Args:
        path (Path): Path to the file

    Returns:
        str: Size of file in KB
    """
    size_in_kb = round(os.path.getsize(path) / 1024)
    return f"~ {size_in_kb} KB"

@ensure_annotations
def decode_image(imgstring: str, filename: str) -> None:
    """Decodes base64 string and saves it as an image file

    Args:
        imgstring (str): Base64 encoded image string
        filename (str): Name of the output image file
    """
    imgdata = base64.b64decode(imgstring)
    with open(filename, 'wb') as f:
        f.write(imgdata)
    logger.info(f"Image file saved at: {filename}")

@ensure_annotations
def encode_image_into_base64(cropped_image_path: str) -> str:
    """Encodes image file into base64 string

    Args:
        cropped_image_path (str): Path to the cropped image file

    Returns:
        str: Base64 encoded image string
    """
    with open(cropped_image_path, 'rb') as f:
        img_bytes = f.read()
    return base64.b64encode(img_bytes).decode('utf-8')