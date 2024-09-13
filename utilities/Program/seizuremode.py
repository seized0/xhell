################################################################

            # discord : uhq.s
            # tiktok  : https://tiktok.com/@uhq.s
            # server  : https://discord.gg/wyUuYr9DEN
            # dev     : uhq.s
            # owner   : uhq.s
            # github  : https://github.com/seized0

#################################################################

from pystyle import *
from colorama import *
import os
import seizcord

from utilities.Program.utils.utils import *






async def flashbang():
    os.system('cls')
    print(Fore.CYAN + """
                   
  █████▒██▓    ▄▄▄        ██████  ██░ ██  ▄▄▄▄    ▄▄▄       ███▄    █   ▄████ 
▓██   ▒▓██▒   ▒████▄    ▒██    ▒ ▓██░ ██▒▓█████▄ ▒████▄     ██ ▀█   █  ██▒ ▀█▒
▒████ ░▒██░   ▒██  ▀█▄  ░ ▓██▄   ▒██▀▀██░▒██▒ ▄██▒██  ▀█▄  ▓██  ▀█ ██▒▒██░▄▄▄░
░▓█▒  ░▒██░   ░██▄▄▄▄██   ▒   ██▒░▓█ ░██ ▒██░█▀  ░██▄▄▄▄██ ▓██▒  ▐▌██▒░▓█  ██▓
░▒█░   ░██████▒▓█   ▓██▒▒██████▒▒░▓█▒░██▓░▓█  ▀█▓ ▓█   ▓██▒▒██░   ▓██░░▒▓███▀▒
 ▒ ░   ░ ▒░▓  ░▒▒   ▓▒█░▒ ▒▓▒ ▒ ░ ▒ ░░▒░▒░▒▓███▀▒ ▒▒   ▓▒█░░ ▒░   ▒ ▒  ░▒   ▒ 
 ░     ░ ░ ▒  ░ ▒   ▒▒ ░░ ░▒  ░ ░ ▒ ░▒░ ░▒░▒   ░   ▒   ▒▒ ░░ ░░   ░ ▒░  ░   ░ 
 ░ ░     ░ ░    ░   ▒   ░  ░  ░   ░  ░░ ░ ░    ░   ░   ▒      ░   ░ ░ ░ ░   ░ 
           ░  ░     ░  ░      ░   ░  ░  ░ ░            ░  ░         ░       ░ 
                                               ░                              
                                 [BETA]              
                                   
""")
    
    token = input(Fore.BLUE + '[+] TOKEN ACCOUNT : ')
    cli = seizcord.Client(token=f'{token}')

    print(Fore.RED +'PRESS CTRL C TO STOP')
    while True:
        cli.setTheme(theme='light')
        time.sleep(0.5)
        cli.setTheme(theme='dark')
        
