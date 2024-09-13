################################################################

            # discord : uhq.s
            # tiktok  : https://tiktok.com/@uhq.s
            # server  : https://discord.gg/wyUuYr9DEN
            # dev     : uhq.s
            # owner   : uhq.s
            # github  : https://github.com/seized0

#################################################################

from utilities.Program.utils.utils import *
import seizcord
import requests

green = Fore.GREEN
red = Fore.RED
magenta = Fore.MAGENTA
blue = Fore.BLUE
r = Fore.WHITE
lmagenta = Fore.LIGHTMAGENTA_EX
lred = Fore.LIGHTRED_EX
yellow = Fore.YELLOW
lgreen = Fore.LIGHTGREEN_EX
cyan = Fore.CYAN



async def hypesquadchanger():
    os.system('cls')
    print(blue + f"""

                                                                                      
 _____             _____               _    _____ _____ _____ _____ _____ _____ _____ 
|  |  |_ _ ___ ___|   __|___ _ _ ___ _| |  |     |  |  |  _  |   | |   __|   __| __  |
|     | | | . | -_|__   | . | | | .'| . |  |   --|     |     | | | |  |  |   __|    -|
|__|__|_  |  _|___|_____|_  |___|__,|___|  |_____|__|__|__|__|_|___|_____|_____|__|__|
      |___|_|             |_|                                                         


{magenta} BRAVERY : 1
{lred} BRILLANCE : 2
{cyan} BALANCE : 3
""")
    token = input(blue + '\nYOUR ACCOUNT TOKEN : ')
    cli = seizcord.Client(token=f'{token}')

    choix = float(input(lred + 'HOUSE : '))

    if choix == 1:
        cli.setHypeSquad(houseid=1)

    elif choix == 2:
        cli.setHypeSquad(houseid=2)

    elif choix == 3:
        cli.setHypeSquad(houseid=3)




    input(red + '\n\n[!] PRESS ENTER TO RETURN TO MENU')