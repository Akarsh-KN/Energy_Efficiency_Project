import yaml
import os, sys
from energy.exception import EnergyException






def read_yaml_file(file_path):
    """
    This function will read yaml file and return its contents
    """


    try:
        with open(file_path,"rb") as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise EnergyException(e, sys) from e