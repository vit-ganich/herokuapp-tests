"""Configuration file reader"""
import json
import os


def read():
    """Open json file and load it's content"""
    with open(f"{os.path.realpath('.')}/config.json", 'r') as config:
        return json.load(config)
