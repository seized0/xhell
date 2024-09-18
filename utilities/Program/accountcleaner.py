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

with open('ids.txt', 'r') as file:
    ids = [line.strip() for line in file if line.strip()]
    
async def cleaner():
    os.system('cls')
    print(blue + """
     _                             _      ____ _                            
    / \   ___ ___ ___  _   _ _ __ | |_   / ___| | ___  __ _ _ __   ___ _ __ 
   / _ \ / __/ __/ _ \| | | | '_ \| __| | |   | |/ _ \/ _` | '_ \ / _ \ '__|
  / ___ \ (_| (_| (_) | |_| | | | | |_  | |___| |  __/ (_| | | | |  __/ |   
 /_/   \_\___\___\___/ \__,_|_| |_|\__|  \____|_|\___|\__,_|_| |_|\___|_|   
                                                                            
""")
    token = input(Fore.RED + '[+] TOKEN : ')
    headers = {
        'Authorization': token
    }
    req = requests.get("https://discord.com/api/v9/users/@me/channels", headers=headers)

    if req.status_code == 200:
        dms = req.json()
        with open('ids.txt', 'w') as file:  
            for dm in dms:
                file.write(f"{dm['id']}\n")  

    else:
        print(f"ERROR : {req.status_code}")


    req = requests.get("https://discord.com/api/v9/users/@me/relationships", headers=headers)

    friends = req.json()
    for friend in friends:
        friendid = friend['id']
        reqx = requests.delete(f"https://discord.com/api/v9/users/@me/relationships/{friendid}", headers=headers)
        
        if reqx.status_code == 204 or reqx.status_code == 200:
            print(Fore.GREEN + f"[+] DELETED FRIEND : {friend['user']['username']}")
        else:
            print(Fore.RED + f"ERROR {reqx.status_code} : FAILED TO REMOVE {friend['user']['username']}")

    dm = "https://discord.com/api/v9/channels/"

    for dms in ids:
        req = requests.delete(url=f"https://discord.com/api/v9/channels/{dms}",headers=headers)
        
        if req.status_code == 200 or 204:
            print(green + f'[+] DM DELETED : {dms}')

        else:
            print(red + f'[-] ERROR {req.status_code} : FAILED TO DELETE DM : {dms} ')

    print(cyan + '\n[+] ACCOUNT CLEANED SUCCESSFULLY')
    input(blue + '\n\n[!] PRESS ENTER TO RETURN TO MENU')