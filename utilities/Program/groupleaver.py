################################################################

            # discord : uhq.s
            # tiktok  : https://tiktok.com/@uhq.s
            # server  : https://discord.gg/xhell
            # dev     : uhq.s
            # owner   : uhq.s
            # github  : https://github.com/seized0

#################################################################

from colorama import *
import os
import requests
red = Fore.RED






async def groupLeaver():
    os.system('cls')
    print(Fore.CYAN + r"""
  ________                            .____                                    
 /  _____/______  ____  __ ________   |    |    ____ _____ ___  __ ___________ 
/   \  __\_  __ \/  _ \|  |  \____ \  |    |  _/ __ \\__  \\  \/ // __ \_  __ \
\    \_\  \  | \(  <_> )  |  /  |_> > |    |__\  ___/ / __ \\   /\  ___/|  | \/
 \______  /__|   \____/|____/|   __/  |_______ \___  >____  /\_/  \___  >__|   
        \/                   |__|             \/   \/     \/          \/              
""")

    token = input(Fore.BLUE + '[+] TOKEN ACCOUNT : ') 
    headers = {
        'Authorization':token
    }
    groupid = input(Fore.CYAN + '[+] GROUP ID : ')

    url = f'https://discord.com/api/v9/channels/{groupid}?silent=true'


    req = requests.delete(url=url,headers=headers)

    if req.status_code == 200:
        print(Fore.GREEN + '[+] GROUP LEFT SUCCESSFULLY')
    else:
        print(Fore.RED + f'[!] ERROR {req.status_code} : {req.text}')

    input(red + '\n\n[!] PRESS ENTER TO RETURN TO MENU')
