################################################################

            # discord : uhq.s
            # tiktok  : https://tiktok.com/@uhq.s
            # server  : https://discord.gg/wyUuYr9DEN
            # dev     : uhq.s
            # owner   : uhq.s
            # github  : https://github.com/seized0

#################################################################

from utilities.Program.utils.utils import *
from bs4 import BeautifulSoup as htmlparser
import requests
import os

green = Fore.GREEN
red = Fore.RED
magenta = Fore.MAGENTA
blue = Fore.BLUE
r = Fore.WHITE
lmagenta = Fore.LIGHTMAGENTA_EX
lred = Fore.LIGHTRED_EX
yellow = Fore.YELLOW
cyan = Fore.CYAN


def lookup(phone_number):
    http = requests.get(f"https://free-lookup.net/{phone_number}")
    html = htmlparser(http.text, "html.parser")
    infos = html.findChild("ul", {"class": "report-summary__list"}).findAll("div")

    return {k.text.strip(): infos[i+1].text.strip() if infos[i+1].text.strip() else "No information" for i, k in enumerate(infos) if not i % 2}

async def phonelookup():
    os.system('cls')
    print(cyan + """

__________.__                           .__                 __                 
\______   \  |__   ____   ____   ____   |  |   ____   ____ |  | ____ ________  
 |     ___/  |  \ /  _ \ /    \_/ __ \  |  |  /  _ \ /  _ \|  |/ /  |  \____ \ 
 |    |   |   Y  (  <_> )   |  \  ___/  |  |_(  <_> |  <_> )    <|  |  /  |_> >
 |____|   |___|  /\____/|___|  /\___  > |____/\____/ \____/|__|_ \____/|   __/ 
               \/            \/     \/                          \/     |__|    



""")
    try:
        
        phone_number = input(blue + "Phone number(with 33) : ").strip().replace("-", "").replace(" ", "").replace("+", "")
    except KeyboardInterrupt:
        return

    try:
        infos = lookup(phone_number)
    except AttributeError:
        print("Error: Invalid phone number\n")

    [print(f"{info}: {infos[info]}") for info in infos]

    input(cyan + '\n\n[!] PRESS ENTER TO RETURN TO MENU')
    
    