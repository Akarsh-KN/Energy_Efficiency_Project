from distutils.command.config import config
import os
from datetime import datetime


def get_current_time_stamp():
    return f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}"


ROOT_DIR = os.getcwd()
CONFIG_DIR = "config"
CONFIG_FILE_NAME="config.yaml"
CONFIG_FILE_PATH = os.path.join(CONFIG_DIR,CONFIG_FILE_NAME)



CURRENT_TIME_STAMP = get_current_time_stamp()


#Training pipeline related variables
TRAINING_PIPELINE_CONFIG_KEY="training_pipeline_config"
TRAINING_PIPELINE_NAME_KEY="pipeline_name"
TRAINING_PIPELINE_ARTIFACT_DIR="artifact_dir"



#Data ingestion related config

DATA_INGESTION_CONFIG_KEY="data_ingestion_config"
DATA_INGESTION_DOWNLOAD_URL_KEY="dataset_download_url"
DATA_INGESTION_RAW_DATA_DIR_KEY="raw_data"
DATA_INGESTION_INGESTED_DIR_KEY="ingested_data"
DATA_INGESTION_TRAIN_DIR_KEY="train"
DATA_INGESTION_TEST_DIR_KEY="test"
DATA_INGESTION_ARTIFACT_DIR="data_ingestion"





