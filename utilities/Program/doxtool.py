from utilities.Program.utils.utils import *
import fade
import os
import requests

red = Fore.RED
blue = Fore.BLUE
cyan = Fore.CYAN
magenta = Fore.MAGENTA
green = Fore.GREEN

ascii = r"""

________                 ___________           .__   
\______ \   _______  ___ \__    ___/___   ____ |  |  
 |    |  \ /  _ \  \/  /   |    | /  _ \ /  _ \|  |  
 |    `   (  <_> >    <    |    |(  <_> |  <_> )  |__
/_______  /\____/__/\_ \   |____| \____/ \____/|____/
        \/            \/                             


"""
async def doxtool():
    os.system('cls')
    print(fade.water(text=ascii))


    username = input(cyan + 'USERNAME : ')
    ip = input('IP : ')

    insta = requests.get(url=f'\n\nhttps://www.instagram.com/{username}')
    tiktok = requests.get(url=f'https://tiktok.com/@{username}')
    x = requests.get(url=f'https://x.com/{username}')
    pinterest = requests.get(url=f'https://www.pinterest.fr/{username}')
    github = requests.get(url=f'https://github.com/{username}')
    snap = requests.get(url=f'https://www.snapchat.com/add/{username}')

    if insta.status_code ==200:
        print(green + f'{username} : FIND INSTAGRAM : https://www.instagram.com/{username}')
    else:
        print(red + 'INSTAGRAM : NOT FOUND')

    if tiktok.status_code ==200:
        print(green + f'{username} : FIND TIKTOK : https://tiktok.com/@{username}')
    else:
        print(red + 'TIKTOK : NOT FOUND')

    if x.status_code ==200:
        print(green + f'{username} : FIND TWITTER : https://x.com/{username}')

    else:
        print(red + 'TWITTER : NOT FOUND')

    if pinterest.status_code ==200:
        print(green + f'{username} : FIND PINTEREST : https://www.pinterest.fr/{username}')

    else:
        print(red + 'PINTEREST : NOT FOUND')

    if github.status_code ==200:
        print(green + f'{username} : FIND GITHUB : https://github.com/{username}')

    else:
        print(red + 'GITHUB : NOT FOUND')

    if snap.status_code ==200:
        print(green + f'{username} : FIND SNAPCHAT : https://www.snapchat.com/add/{username}')
    else:
        print(red + 'SNAPCHAT : NOT FOUND')

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

    input(blue + '\n\n[!] PRESS ENTER TO RETURN TO MENU')