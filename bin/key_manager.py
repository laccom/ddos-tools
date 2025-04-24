import requests
import json
import os
from colorama import Fore

def verify_key(api_url, key):
    url = f"{api_url}?key={key}"
    response = requests.get(url)
    if response.status_code == 200:
        return True
    elif response.status_code == 404:
        return False
    elif response.status_code == 429:
        return True
    else:
        return False

def save_key_to_config(key, config_file='config-key.json'):
    with open(config_file, 'w') as f:
        json.dump({"key": key}, f)

def load_key_from_config(config_file='config-key.json'):
    try:
        with open(config_file, 'r') as f:
            config = json.load(f)
            return config.get("key")
    except FileNotFoundError:
        return None

def delete_config_file(config_file='config-key.json'):
    if os.path.exists(config_file):
        os.remove(config_file)
        print(Fore.RED + f"{config_file} supprimé.")
