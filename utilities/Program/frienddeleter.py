import requests
import os
from colorama import *

green = Fore.GREEN
red = Fore.RED
magenta = Fore.MAGENTA
blue = Fore.BLUE
r = Fore.WHITE
lmagenta = Fore.LIGHTMAGENTA_EX
lred = Fore.LIGHTRED_EX
yellow = Fore.YELLOW
cyan = Fore.CYAN
lgreen = Fore.LIGHTGREEN_EX
lblue = Fore.LIGHTBLUE_EX


async def friendsdeleter():
    os.system('cls')
    print(lmagenta + """                                                           
 _____     _           _        ____      _     _           
|   __|___|_|___ ___ _| |___   |    \ ___| |___| |_ ___ ___ 
|   __|  _| | -_|   | . |_ -|  |  |  | -_| | -_|  _| -_|  _|
|__|  |_| |_|___|_|_|___|___|  |____/|___|_|___|_| |___|_|  
                                                            

""")
    token = input(Fore.RED + '[+] TOKEN : ')
    headers = {
        'Authorization': token
    }

    req = requests.get("https://discord.com/api/v9/users/@me/relationships", headers=headers)

    friends = req.json()
    for friend in friends:
        friendid = friend['id']
        reqx = requests.delete(f"https://discord.com/api/v9/users/@me/relationships/{friendid}", headers=headers)
        
        if reqx.status_code == 204 or reqx.status_code == 200:
            print(Fore.GREEN + f"DELETED FRIEND : {friend['user']['username']}")
        else:
            print(Fore.RED + f"ERROR {reqx.status_code} : FAILED TO REMOVE {friend['user']['username']}")

    input(Fore.BLUE + '\n\n[!] PRESS ENTER TO RETURN TO MENU')