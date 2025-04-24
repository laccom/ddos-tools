import sys
import time
from colorama import Fore

ascii_text = """
####       ###      ####     ####    #####   ##   ##           #####    #####     #####    #####
 ##       ## ##    ##  ##   ##  ##  ### ###  ### ###            ## ##    ## ##   ### ###  ##   ##
 ##      ##   ##  ##       ##       ##   ##  #######            ##  ##   ##  ##  ##   ##  ##
 ##      ##   ##  ##       ##       ##   ##  ## # ##            ##  ##   ##  ##  ##   ##   #####
 ##      #######  ##       ##       ##   ##  ##   ##            ##  ##   ##  ##  ##   ##       ##
 ##  ##  ##   ##   ##  ##   ##  ##  ### ###  ##   ##            ## ##    ## ##   ### ###  ##   ##
#######  ##   ##    ####     ####    #####   ### ###           #####    #####     #####    #####
"""

def print_ascii_text():
    for char in ascii_text:
        sys.stdout.write(Fore.RED + char)
        sys.stdout.flush()
        time.sleep(0.00025)
    print()

def print_ascii_text2():
    for char in ascii_text:
        sys.stdout.write(Fore.GREEN + char)
        sys.stdout.flush()
    print()
