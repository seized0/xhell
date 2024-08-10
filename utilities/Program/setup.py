from colorama import *
import os
import time

################################################################

            # discord : uhq.s
            # tiktok  : https://tiktok.com/@paiementsecurise
            # serveur : https://discord.gg/wyUuYr9DEN
            # dev : uhq.s
            # owner : uhq.s

################################################################

green = Fore.GREEN
red = Fore.RED

def req():
    cmd ="start start.bat"
    print(green +'Installing colorama...')
    os.system('python -m pip install colorama')
    print(green +'Installing pyinstaller...')
    os.system('python -m pip install pyinstaller')
    print(green +'Installing discum...')
    os.system('python -m pip install discum')
    print(green +'Installing bs4...')
    os.system('python -m pip install bs4')
    print(green +'Installing requests...')
    os.system('python -m pip install requests') 
    print(green +'Installing pydumpck...')
    os.system('python -m pip install pydumpck') 
    print(green +'Installing discord...')
    os.system('python -m pip install discord')
    print(red + '\nPlease Run start.bat')
    time.sleep()


 
    
req()

