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

async def dmdeleter():
    os.system('cls')
    print(yellow + f"""
 _______                       _______             __              __                         
/       \                     /       \           /  |            /  |                        
$$$$$$$  | _____  ____        $$$$$$$  |  ______  $$ |  ______   _$$ |_     ______    ______  
$$ |  $$ |/     \/    \       $$ |  $$ | /      \ $$ | /      \ / $$   |   /      \  /      \ 
$$ |  $$ |$$$$$$ $$$$  |      $$ |  $$ |/$$$$$$  |$$ |/$$$$$$  |$$$$$$/   /$$$$$$  |/$$$$$$  |
$$ |  $$ |$$ | $$ | $$ |      $$ |  $$ |$$    $$ |$$ |$$    $$ |  $$ | __ $$    $$ |$$ |  $$/ 
$$ |__$$ |$$ | $$ | $$ |      $$ |__$$ |$$$$$$$$/ $$ |$$$$$$$$/   $$ |/  |$$$$$$$$/ $$ |      
$$    $$/ $$ | $$ | $$ |      $$    $$/ $$       |$$ |$$       |  $$  $$/ $$       |$$ |      
$$$$$$$/  $$/  $$/  $$/       $$$$$$$/   $$$$$$$/ $$/  $$$$$$$/    $$$$/   $$$$$$$/ $$/       

                                                                         
""")
    token = input(red + '[+] TOKEN : ')
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



    dm = "https://discord.com/api/v9/channels/"

    for dms in ids:
        req = requests.delete(url=f"https://discord.com/api/v9/channels/{dms}",headers=headers)
        
        if req.status_code == 200 or 204:
            print(green + f'[+] DM DELETED : {dms}')

        else:
            print(red + f'[-] ERROR {req.status_code} : FAILED TO DELETE DM : {dms} ')

    print(blue + '\n[!] FINISH')
    input(cyan + '\n\n[+] PRESS ENTER TO RETURN TO MENU')
