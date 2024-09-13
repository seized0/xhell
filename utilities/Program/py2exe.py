################################################################

            # discord : uhq.s
            # tiktok  : https://tiktok.com/@uhq.s
            # server  : https://discord.gg/wyUuYr9DEN
            # dev     : uhq.s
            # owner   : uhq.s
            # github  : https://github.com/seized0

#################################################################

import colorama
from colorama import *
import os

red = Fore.RED
blue = Fore.BLUE
cyan = Fore.CYAN
magenta = Fore.MAGENTA
green = Fore.GREEN

async def py2exe():
    os.system('cls')
    print(magenta + """
   _ (`-.                        ('-.  ) (`-.        ('-.   
  ( (OO  )                     _(  OO)  ( OO ).    _(  OO)  
 _.`     \  ,--.   ,--..-----.(,------.(_/.  \_)-.(,------. 
(__...--''   \  `.'  // ,-.   \|  .---' \  `.'  /  |  .---' 
 |  /  | | .-')     / '-'  |  ||  |      \     /\  |  |     
 |  |_.' |(OO  \   /     .'  /(|  '--.    \   \ | (|  '--.  
 |  .___.' |   /  /\_  .'  /__ |  .--'   .'    \_) |  .--'  
 |  |      `-./  /.__)|       ||  `---. /  .'.  \  |  `---. 
 `--'        `--'     `-------'`------''--'   '--' `------' 

1. pyinstaller             2. cxfreeze (recommended)
""")
    method = input(magenta + 'METHOD :  ')
    if method =='1':     
        filename = input(magenta + '\n\nPYTHON FILE NAME : ')
        os.system(f'pyinstaller --onefile {filename}')


    elif method =='2':
        filename = input(magenta + '\n\nPYTHON FILE NAME : ')
        icon = input(magenta + 'ICON FILE NAME.ICO (PRESS ENTER TO ENTER NOTHING): ')
        if icon =="":
            os.system(f'cxfreeze --script {filename}')
        else:
            os.system(f'cxfreeze --icon={icon} --script {filename}')     

    print(red + '\n\n[+] FINISH ! ')
    input(red + '\n\n[!] PRESS ENTER TO RETURN TO MENU')