import requests
from colorama import Fore

def send_request_with_status(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(Fore.GREEN + f"SUCCESS 200 | Requête vers {url} réussie.")
            return True
        elif response.status_code == 404:
            print(Fore.RED + f"ERROR 404 | URL {url} introuvable.")
            return False
        elif response.status_code == 429:
            print(Fore.YELLOW + f"RATE LIMIT 429 | Trop de requêtes.")
            return True
        else:
            print(Fore.RED + f"ERROR {response.status_code} | Problème avec l'URL.")
            return True
    except requests.exceptions.RequestException as e:
        return False

def validate_url(url):
    if not url.startswith("http://") and not url.startswith("https://"):
        url = "http://" + url
    return url
