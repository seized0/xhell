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
import time
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


async def statuschanger():
    os.system('cls')
    print(lred + """

╔═╗╔╦╗╔═╗╔╦╗╦ ╦╔═╗  ╦═╗╔═╗╔╦╗╔═╗╔╦╗╔═╗╦═╗
╚═╗ ║ ╠═╣ ║ ║ ║╚═╗  ╠╦╝║ ║ ║ ╠═╣ ║ ║ ║╠╦╝
╚═╝ ╩ ╩ ╩ ╩ ╚═╝╚═╝  ╩╚═╚═╝ ╩ ╩ ╩ ╩ ╚═╝╩╚═

""")

    token = input(red + '[!] YOUR ACCOUNT TOKEN : ')
    timex = float(input(blue + '[?] TIME TO CHANGE STATUS : ')) # 1 , 0.5 
    status1 = input(cyan + '[?] STATUS 1 : ')
    status2 = input(blue +'[?] STATUS 2 : ')
    status3 = input(cyan + '[?] STATUS 3 : ')
    cli = seizcord.Client(token=token)

    print(magenta + 'PRESS CTRL C TO STOP\n\n')
    x = input
    while True:
        cli.setStatus(text=f'{status1}')
        time.sleep(timex)
        cli.setStatus(text=f'{status2}')
        time.sleep(timex)
        cli.setStatus(text=f'{status3}')
        time.sleep(timex)



    