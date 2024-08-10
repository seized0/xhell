from utilities.Program.utils.utils import *
################################################################

            # discord : uhq.s
            # tiktok  : https://tiktok.com/@paiementsecurise
            # serveur : https://discord.gg/wyUuYr9DEN
            # dev : uhq.s
            # owner : uhq.s

################################################################

async def hwidspoofer():
    os.system('cls')
    print(Fore.RED + """



 ██░ ██  █     █░ ██▓▓█████▄      ██████  ██▓███   ▒█████   ▒█████    █████▒▓█████  ██▀███  
▓██░ ██▒▓█░ █ ░█░▓██▒▒██▀ ██▌   ▒██    ▒ ▓██░  ██▒▒██▒  ██▒▒██▒  ██▒▓██   ▒ ▓█   ▀ ▓██ ▒ ██▒
▒██▀▀██░▒█░ █ ░█ ▒██▒░██   █▌   ░ ▓██▄   ▓██░ ██▓▒▒██░  ██▒▒██░  ██▒▒████ ░ ▒███   ▓██ ░▄█ ▒
░▓█ ░██ ░█░ █ ░█ ░██░░▓█▄   ▌     ▒   ██▒▒██▄█▓▒ ▒▒██   ██░▒██   ██░░▓█▒  ░ ▒▓█  ▄ ▒██▀▀█▄  
░▓█▒░██▓░░██▒██▓ ░██░░▒████▓    ▒██████▒▒▒██▒ ░  ░░ ████▓▒░░ ████▓▒░░▒█░    ░▒████▒░██▓ ▒██▒
 ▒ ░░▒░▒░ ▓░▒ ▒  ░▓   ▒▒▓  ▒    ▒ ▒▓▒ ▒ ░▒▓▒░ ░  ░░ ▒░▒░▒░ ░ ▒░▒░▒░  ▒ ░    ░░ ▒░ ░░ ▒▓ ░▒▓░
 ▒ ░▒░ ░  ▒ ░ ░   ▒ ░ ░ ▒  ▒    ░ ░▒  ░ ░░▒ ░       ░ ▒ ▒░   ░ ▒ ▒░  ░       ░ ░  ░  ░▒ ░ ▒░
 ░  ░░ ░  ░   ░   ▒ ░ ░ ░  ░    ░  ░  ░  ░░       ░ ░ ░ ▒  ░ ░ ░ ▒   ░ ░       ░     ░░   ░ 
 ░  ░  ░    ░     ░     ░             ░               ░ ░      ░ ░             ░  ░   ░     
                      ░                                                                     
                                                                                                                   

""")
    
    
    choice = input('DO YOU WANT TO BUILD DE HWID SPOOFER ?[Y/N]  ')

    if choice =='Y':
        loc = 'utilities\Setup\hwid_spoofer_src.py'
        cmd = (rf'pyinstaller {loc} --onefile --uac-admin --name hwid_spoofer')
        subprocess.call(cmd)
        
        print(Fore.RED + '[INFO] LOCATION : dist')
        print(Fore.GREEN + '\n\n[INFO] OPERATION FINISH')
        os.remove('hwid_spoofer.spec')

        input(Fore.BLUE + '\n\nPRESS ENTER TO RETURN TO MENU')
  

    elif choice =="N":
        print(red + '[INFO] You have to compile the file as an .exe for it to work')

        input(blue + 'PRESS ENTER TO RETURN TO MENU')