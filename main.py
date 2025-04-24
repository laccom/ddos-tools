import subprocess
import sys

def install_requirements():
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
    except subprocess.CalledProcessError as e:
        print("Erreur lors de l'installation des dépendances:", e)
        sys.exit(1)

install_requirements()

import sys
import time
import os
from colorama import Fore, init

sys.path.append(os.path.join(os.path.dirname(__file__), 'bin'))

from ascii import print_ascii_text, print_ascii_text2
from key_manager import verify_key, save_key_to_config, load_key_from_config, delete_config_file
from requests_handler import send_request_with_status, validate_url

init(autoreset=True)
os.system('cls')

def main():
    print_ascii_text()

    API_URL = "https://laccom.org/api/v1/session"
    
    key = load_key_from_config()

    if key is None:
        print(Fore.CYAN + "Aucune clé trouvée. Veuillez entrer une clé valide")
        key = input("Clé : ")

    if not verify_key(API_URL, key):
        print(Fore.RED + "Clé incorrecte. Veuillez vérifier.")
        delete_config_file()
        return

    save_key_to_config(key)
    
    os.system('cls')

    print_ascii_text2()

    print(Fore.GREEN + "Clé vérifiée avec succès !")
    
    site_url = input(Fore.CYAN + "Entrez l'URL du site à tester : ")

    site_url = validate_url(site_url)

    request_count = 0

    is_valid_url = send_request_with_status(site_url)
    
    if not is_valid_url:
        print(Fore.RED + "URL invalide, arrêt du programme.")
        return
    
    print(Fore.CYAN + "Envoi des requêtes...")
    
    try:
        while True:
            time.sleep(0.01)
            if not send_request_with_status(site_url):
                print(Fore.RED + "L'URL est maintenant invalide. Arrêt du programme.")
                break
            request_count += 1
    except KeyboardInterrupt:
        print(Fore.YELLOW + f"\nNombre total de requêtes envoyées : {request_count}")
        print(Fore.RED + "Script arrêté.")
        sys.exit(0)

if __name__ == "__main__":
    main()
