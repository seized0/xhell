import time
import requests
from colorama import Fore
import os

green = Fore.GREEN
red = Fore.RED
magenta = Fore.MAGENTA
blue = Fore.BLUE
r = Fore.WHITE
lmagenta = Fore.LIGHTMAGENTA_EX
lred = Fore.LIGHTRED_EX
yellow = Fore.YELLOW
lgreen = Fore.LIGHTGREEN_EX


async def hypesquadchanger():
    os.system('cls')
    print("""

                                                                                      
 _____             _____               _    _____ _____ _____ _____ _____ _____ _____ 
|  |  |_ _ ___ ___|   __|___ _ _ ___ _| |  |     |  |  |  _  |   | |   __|   __| __  |
|     | | | . | -_|__   | . | | | .'| . |  |   --|     |     | | | |  |  |   __|    -|
|__|__|_  |  _|___|_____|_  |___|__,|___|  |_____|__|__|__|__|_|___|_____|_____|__|__|
      |___|_|             |_|                                                         


""")
    hypetoken = input(f"\n{red}Your token account: {Fore.RESET}") # OBLIGATOIRE 
    print(red + f"\n[1] Bravery\n[2] Briliance\n[3] Balance\n")
    hypesquad = input(f"[#] Choice : {Fore.RESET}")
    headersosat = {
        'Authorization': str(hypetoken)
    }

    payloadsosat = {
        'house_id': str(hypesquad)
    }
    time.sleep(1)
    rep = requests.session().post("https://discord.com/api/v8/hypesquad/online", json=payloadsosat, headers=headersosat)

    input(red + '\nFINISH! ')
