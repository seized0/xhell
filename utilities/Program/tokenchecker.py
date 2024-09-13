################################################################

            # discord : uhq.s
            # tiktok  : https://tiktok.com/@uhq.s
            # server  : https://discord.gg/wyUuYr9DEN
            # dev     : uhq.s
            # owner   : uhq.s
            # github  : https://github.com/seized0

#################################################################

import os
import requests
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


async def tokenchecker():
    os.system('cls')
    print(lblue + """

 _____     _                _____ _               _             
|_   _|   | |              /  __ \ |             | |            
  | | ___ | | _____ _ __   | /  \/ |__   ___  ___| | _____ _ __ 
  | |/ _ \| |/ / _ \ '_ \  | |   | '_ \ / _ \/ __| |/ / _ \ '__|
  | | (_) |   <  __/ | | | | \__/\ | | |  __/ (__|   <  __/ |   
  \_/\___/|_|\_\___|_| |_|  \____/_| |_|\___|\___|_|\_\___|_|   
                                                                
   
""")
    
    
    with open('tokens.txt', 'r') as f:
        tokens = [token.strip() for token in f.readlines()]

    valid_tokens = 0
    invalid_tokens = 0

    for token in tokens:
        header = {'Authorization': token}
        url = 'https://discord.com/api/v9/users/@me'
        req = requests.get(url=url, headers=header)

        if req.status_code == 200:
            print(f"{green}VALID TOKEN | {token}")
            valid_tokens += 1
        else:
            print(f"{red}INVALID TOKEN | {token}")
            invalid_tokens += 1

    print(f"\n{green}VALID TOKENS :  {valid_tokens}")
    print(f"{red}INVALID TOKENS :  {invalid_tokens}")

    input(blue + '\n\nPRESS ENTER TO RETURN TO MENU')