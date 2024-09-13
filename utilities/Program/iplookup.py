################################################################

            # discord : uhq.s
            # tiktok  : https://tiktok.com/@uhq.s
            # server  : https://discord.gg/wyUuYr9DEN
            # dev     : uhq.s
            # owner   : uhq.s
            # github  : https://github.com/seized0

#################################################################

from utilities.Program.utils.utils import *
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

async def iplookup():
    os.system('cls')
    print(red + """

 ██▓ ██▓███      ██▓     ▒█████   ▒█████   ██ ▄█▀ █    ██  ██▓███  
▓██▒▓██░  ██▒   ▓██▒    ▒██▒  ██▒▒██▒  ██▒ ██▄█▒  ██  ▓██▒▓██░  ██▒
▒██▒▓██░ ██▓▒   ▒██░    ▒██░  ██▒▒██░  ██▒▓███▄░ ▓██  ▒██░▓██░ ██▓▒
░██░▒██▄█▓▒ ▒   ▒██░    ▒██   ██░▒██   ██░▓██ █▄ ▓▓█  ░██░▒██▄█▓▒ ▒
░██░▒██▒ ░  ░   ░██████▒░ ████▓▒░░ ████▓▒░▒██▒ █▄▒▒█████▓ ▒██▒ ░  ░
░▓  ▒▓▒░ ░  ░   ░ ▒░▓  ░░ ▒░▒░▒░ ░ ▒░▒░▒░ ▒ ▒▒ ▓▒░▒▓▒ ▒ ▒ ▒▓▒░ ░  ░
 ▒ ░░▒ ░        ░ ░ ▒  ░  ░ ▒ ▒░   ░ ▒ ▒░ ░ ░▒ ▒░░░▒░ ░ ░ ░▒ ░     
 ▒ ░░░            ░ ░   ░ ░ ░ ▒  ░ ░ ░ ▒  ░ ░░ ░  ░░░ ░ ░ ░░       
 ░                  ░  ░    ░ ░      ░ ░  ░  ░      ░              
                                                                   


""")
    ip = input (f'{red}[+] ENTER IP : ')
    api_key = 'c59217a31a2c34' 
    url = f'https://ipinfo.io/{ip}/json?token={api_key}'
  
    try:
          response = requests.get(url)
          response.raise_for_status()
          if response.status_code == 200:
            data = response.json()
            print(red + "\nIP : " + ip)
            print(red + "Pays :", data.get("country"))
            print(red + "Ville :", data.get("city"))
            print(red + "Région :", data.get("region"))
            print(red + "Code Postal :", data.get("postal"))
            print(red+ "Longitude :", data.get("loc").split(",")[1])
            print(red + "Latitude :", data.get("loc").split(",")[0])
            print(red + "ISP :", data.get("org"))

    except Exception as e:
        print(red + f"ERREUR : {str(e)}")


    input(lred + '\n\n[!] PRESS ENTER TO RETURN TO MENU')

