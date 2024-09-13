################################################################

            # discord : uhq.s
            # tiktok  : https://tiktok.com/@uhq.s
            # server  : https://discord.gg/wyUuYr9DEN
            # dev     : uhq.s
            # owner   : uhq.s
            # github  : https://github.com/seized0

#################################################################

import asyncio
from pystyle import *
from colorama import *
import os
import time
import requests
import random
import seizcord

from utilities.Program.utils.utils import *



red = Fore.RED


async def tokenleaver():
    os.system('cls')
    print(Fore.LIGHTRED_EX + """

  ______      __                 __                              
 /_  __/___  / /_____  ____     / /   ___  ____ __   _____  _____
  / / / __ \/ //_/ _ \/ __ \   / /   / _ \/ __ `/ | / / _ \/ ___/
 / / / /_/ / ,< /  __/ / / /  / /___/  __/ /_/ /| |/ /  __/ /    
/_/  \____/_/|_|\___/_/ /_/  /_____/\___/\__,_/ |___/\___/_/     
                                                                 
                                   
""")
    
    token = input(red + '[+] TOKEN ACCOUNT : ')
    cli = seizcord.Client(token=f'{token}')
    cli.enableDevMode()
    gid = input(red + '[+] GUILD ID : ')
    

    cli.leaveGuild(guildid=gid)
    
    input(red + '\n\n[!] PRESS ENTER TO RETURN TO MENU')
