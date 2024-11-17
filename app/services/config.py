# services/config.py

import json

def load_config(config_file: str = 'config.json') -> dict:
    """
    Loads configuration data from a JSON file.
    """
    with open(config_file, 'r') as file:
        return json.load(file)
