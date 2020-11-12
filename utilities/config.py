import json
import os


def read():
    with open(f"{os.path.realpath('.')}/config.json", 'r') as f:
        return json.load(f)
