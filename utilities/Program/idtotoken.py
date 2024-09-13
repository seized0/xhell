################################################################

            # discord : uhq.s
            # tiktok  : https://tiktok.com/@uhq.s
            # server  : https://discord.gg/wyUuYr9DEN
            # dev     : uhq.s
            # owner   : uhq.s
            # github  : https://github.com/seized0

#################################################################

import base64
import os
from utilities.Program.utils.utils import *


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

async def idtotoken():
    os.system('cls')

    print(red + """  

██ ██████      ████████  ██████      ████████  ██████  ██   ██ ███████ ███    ██ 
██ ██   ██        ██    ██    ██        ██    ██    ██ ██  ██  ██      ████   ██ 
██ ██   ██        ██    ██    ██        ██    ██    ██ █████   █████   ██ ██  ██ 
██ ██   ██        ██    ██    ██        ██    ██    ██ ██  ██  ██      ██  ██ ██ 
██ ██████         ██     ██████         ██     ██████  ██   ██ ███████ ██   ████ 
                                                                                 
                                                                                 
""")

    id = input(lred + 'ID : ')
    encode = base64.b64encode(id.encode())
    print(blue + f'\n\n{encode}')

    input(red + '\n\n[!] PRESS ENTER TO RETURN TO MENU')