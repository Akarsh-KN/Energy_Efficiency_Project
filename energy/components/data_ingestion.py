from energy.logger import logging
from energy.exception import EnergyException
import os
import sys
import pandas as pd
import numpy as np
from energy.entity.config_entity import DataIngestionConfig




class DataIngestion:

    def __init__(self,data_ingestion_config:DataIngestionConfig):
        try:
            logging.info(f"{'>>'*20}Data Ingestion log started {'<<'*20}")
            self.data_ingestion_config=data_ingestion_config
        except Exception as e:
            raise EnergyException(e,sys) from e

    def download_energy_data(self) -> str:
        try:
            download_url = self.data_ingestion_config.dataset_download_url
            os.makedirs()
        except Exception as e:
            raise EnergyException(e,sys) from e

        
    