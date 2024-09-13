################################################################

            # discord : uhq.s
            # tiktok  : https://tiktok.com/@uhq.s
            # server  : https://discord.gg/wyUuYr9DEN
            # dev     : uhq.s
            # owner   : uhq.s
            # github  : https://github.com/seized0

#################################################################

import seizhooks
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

async def webhookspammer():
    os.system('cls')
    print(f"""

{blue}▄▄▌ ▐ ▄▌▄▄▄ .▄▄▄▄·  ▄ .▄            ▄ •▄   {red}  .▄▄ ·  ▄▄▄· ▄▄▄· • ▌ ▄ ·. • ▌ ▄ ·. ▄▄▄ .▄▄▄  
{blue}██· █▌▐█▀▄.▀·▐█ ▀█▪██▪▐█▪     ▪     █▌▄▌▪  {red}  ▐█ ▀. ▐█ ▄█▐█ ▀█ ·██ ▐███▪·██ ▐███▪▀▄.▀·▀▄ █·
{blue}██▪▐█▐▐▌▐▀▀▪▄▐█▀▀█▄██▀▐█ ▄█▀▄  ▄█▀▄ ▐▀▀▄·  {red}  ▄▀▀▀█▄ ██▀·▄█▀▀█ ▐█ ▌▐▌▐█·▐█ ▌▐▌▐█·▐▀▀▪▄▐▀▀▄ 
{blue}▐█▌██▐█▌▐█▄▄▌██▄▪▐███▌▐▀▐█▌.▐▌▐█▌.▐▌▐█.█▌  {red}  ▐█▄▪▐█▐█▪·•▐█ ▪▐▌██ ██▌▐█▌██ ██▌▐█▌▐█▄▄▌▐█•█▌
{blue} ▀▀▀▀ ▀▪ ▀▀▀ ·▀▀▀▀ ▀▀▀ · ▀█▄▀▪ ▀█▄▀▪·▀  ▀  {red}   ▀▀▀▀ .▀    ▀  ▀ ▀▀  █▪▀▀▀▀▀  █▪▀▀▀ ▀▀▀ .▀  ▀
                                                                                                              

""")
    
    webhook = input(lred + '[\] WEBHOOK : ')
    message = input(cyan + '[/] MESSAGE : ')
    name = input(lred + '[!] NAME : ')
    avatar = input(cyan + '[$] AVATAR URL (press enter to skip) : ')


    h00k = seizhooks.Hook(webhook=f'{webhook}')
    print("\n")

    if avatar == "":
        print(red + 'PRESS CTRL C TO STOP')
        while True:
            h00k.SendMessage(message=f'{message}',name=f'{name}',avatar=None)

    else:
        print(red + 'PRESS CTRL C TO STOP')
        while True:
            h00k.SendMessage(message=f'{message}',name=f'{name}',avatar=f'{avatar}')
            

