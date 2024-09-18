import requests
import os
from colorama import *

async def idscrapper():
    os.system('cls')
    print(Fore.YELLOW+"""

   _______    ____                              
  /  _/ _ \  / __/__________ ____  ___  ___ ____
 _/ // // / _\ \/ __/ __/ _ `/ _ \/ _ \/ -_) __/
/___/____/ /___/\__/_/  \_,_/ .__/ .__/\__/_/   
                           /_/  /_/             

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
                print(Fore.LIGHTRED_EX + f"ID: {dm['id']}")
    else:
        print(f"ERROR : {req.status_code}")

    input(Fore.BLUE + '\n\n[!] PRESS ENTER TO RETURN TO MENU')