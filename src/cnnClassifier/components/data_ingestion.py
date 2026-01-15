import os
import zipfile
import kagglehub
from cnnClassifier.utils.common import get_size
from cnnClassifier import logger
from cnnClassifier.entity.config_entity import DataIngestionConfig
import shutil

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        '''
        Fetch data from the url
        '''
        try: 
            dataset_url = self.config.source_URL
            unzip_path = self.config.unzip_dir
            os.makedirs("artifacts/data_ingestion", exist_ok=True)
            logger.info(f"Downloading data from source URL {dataset_url} to {unzip_path}")

            # Code to download data from self.config.source_URL
            file_id = dataset_url.split("/")[-2] + "/" + dataset_url.split("/")[-1].split("?")[0]
            cache_path = kagglehub.dataset_download(file_id)

            # Copy all files from cache to your project directory
            shutil.copytree(cache_path, unzip_path, dirs_exist_ok=True)

            
            logger.info(f"Data downloaded to {self.config.local_data_file} into {unzip_path}")
        except Exception as e:
            logger.error(f"Error occurred while downloading data: {e}")
            raise e
        
    def extract_zip_file(self):
        """
        zip_file_path: str
        Extracts the zip file into the data directory
        Function returns None
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)