"""
This code is used to:

1. read paramaters from the parameters file
2. Process it
3. Return a DataFrame
"""

import os
import yaml
import pandas as pd
import argparse


def read_params(config_path):
    """
    Function that read the configuration file from the path and convert the yaml file into json
    """
    with open(config_path) as yaml_file:
        config = yaml.safe_load(yaml_file)
    return config


def get_data(config_path):
    config = read_params(config_path)
    data_path = config["data_source"]["s3_source"]
    df = pd.read_csv(data_path, sep=",", encoding="UTF-8")
    return df


if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="params.yaml")
    parsed_args = args.parse_args()
    get_data(config_path=parsed_args.config)
