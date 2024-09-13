################################################################

            # discord : uhq.s
            # tiktok  : https://tiktok.com/@uhq.s
            # server  : https://discord.gg/wyUuYr9DEN
            # dev     : uhq.s
            # owner   : uhq.s
            # github  : https://github.com/seized0

#################################################################

import requests
from utilities.Program.utils.utils import *
# using MY library
import seizhooks

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


# url = 'https://discord.com/api/v9/channels/1269018586635047089/webhooks'
# hook = input('WEBHOOK : ')

# data = {
#     "url":hook
#     }

# x = requests.delete(url=hook,headers=data)

# print(x.status_code)

async def webhookdeleter():
    os.system('cls')
    print(f"""
                                                                                                              
{lred},--.   ,--.       ,--.   ,--.                   ,--.      {lmagenta}  ,------.         ,--.         ,--.                 
{lred}|  |   |  | ,---. |  |-. |  ,---.  ,---.  ,---. |  |,-.   {lmagenta}  |  .-.  \  ,---. |  | ,---. ,-'  '-. ,---. ,--.--. 
{lred}|  |.'.|  || .-. :| .-. '|  .-.  || .-. || .-. ||     /   {lmagenta}  |  |  \  :| .-. :|  || .-. :'-.  .-'| .-. :|  .--' 
{lred}|   ,'.   |\   --.| `-' ||  | |  |' '-' '' '-' '|  \  \   {lmagenta}  |  '--'  /\   --.|  |\   --.  |  |  \   --.|  |    
{lred}'--'   '--' `----' `---' `--' `--' `---'  `---' `--'`--'  {lmagenta}  `-------'  `----'`--' `----'  `--'   `----'`--'    
                                                                                                               


""")
    
    webhook = input(blue + 'WEBHOOK : ')

    h00k = seizhooks.Hook(webhook=f'{webhook}')
    print("\n")
    h00k.Delete()

    input(red + '\n\n[!] PRESS ENTER TO RETURN TO MENU')