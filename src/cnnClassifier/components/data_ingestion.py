import os
import zipfile
import kagglehub
from cnnClassifier import logger
from cnnClassifier.entity.config_entity import DataIngestionConfig
import shutil
import random
from pathlib import Path

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def _limit_files_per_class(self, base_dir: Path, class_name: str, max_files: int = 100):
        class_dir = Path(base_dir) / class_name

        files = [f for f in class_dir.iterdir() if f.is_file()]

        if len(files) <= max_files:
            return  # nothing to trim

        random.shuffle(files)
        files_to_remove = files[max_files:]

        for f in files_to_remove:
            f.unlink()


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
            cache_path = Path(kagglehub.dataset_download(file_id))

            # Copy all files from cache to your project directory
            #shutil.copytree(cache_path, unzip_path, dirs_exist_ok=True)

            #LIMIT DATASET SIZE for speed during experimentation
            self._limit_files_per_class(unzip_path, "CT-KIDNEY-DATASET-Normal-Cyst-Tumor-Stone/CT-KIDNEY-DATASET-Normal-Cyst-Tumor-Stone/Cyst", max_files=100)
            self._limit_files_per_class(unzip_path, "CT-KIDNEY-DATASET-Normal-Cyst-Tumor-Stone/CT-KIDNEY-DATASET-Normal-Cyst-Tumor-Stone/Tumor", max_files=100)
            self._limit_files_per_class(unzip_path, "CT-KIDNEY-DATASET-Normal-Cyst-Tumor-Stone/CT-KIDNEY-DATASET-Normal-Cyst-Tumor-Stone/Normal", max_files=100)
            self._limit_files_per_class(unzip_path, "CT-KIDNEY-DATASET-Normal-Cyst-Tumor-Stone/CT-KIDNEY-DATASET-Normal-Cyst-Tumor-Stone/Cyst", max_files=100)
            self._limit_files_per_class(unzip_path, "CT-KIDNEY-DATASET-Normal-Cyst-Tumor-Stone/CT-KIDNEY-DATASET-Normal-Cyst-Tumor-Stone/Stone", max_files=100)
            
            logger.info(f"Data downloaded to {self.config.local_data_file} into {unzip_path}")
        except Exception as e:
            logger.error(f"Error occurred while downloading data: {e}")
            raise e
    