from utilities.Program.utils.utils import *
################################################################

            # discord : uhq.s
            # tiktok  : https://tiktok.com/@paiementsecurise
            # serveur : https://discord.gg/wyUuYr9DEN
            # dev : uhq.s
            # owner : uhq.s

################################################################

async def uuidspoofer():
    os.system('cls')
    print(Fore.RED + """


▄• ▄▌▄• ▄▌▪  ·▄▄▄▄      .▄▄ ·  ▄▄▄·            ·▄▄▄▄▄▄ .▄▄▄  
█▪██▌█▪██▌██ ██▪ ██     ▐█ ▀. ▐█ ▄█▪     ▪     ▐▄▄·▀▄.▀·▀▄ █·
█▌▐█▌█▌▐█▌▐█·▐█· ▐█▌    ▄▀▀▀█▄ ██▀· ▄█▀▄  ▄█▀▄ ██▪ ▐▀▀▪▄▐▀▀▄ 
▐█▄█▌▐█▄█▌▐█▌██. ██     ▐█▄▪▐█▐█▪·•▐█▌.▐▌▐█▌.▐▌██▌.▐█▄▄▌▐█•█▌
 ▀▀▀  ▀▀▀ ▀▀▀▀▀▀▀▀•      ▀▀▀▀ .▀    ▀█▄▀▪ ▀█▄▀▪▀▀▀  ▀▀▀ .▀  ▀


""")
    choice = input('DO YOU WANT TO BUILD DE HWID SPOOFER ?[Y/N]  ')

    if choice =='Y':
        loc = r'utilities\Setup\uuid_spoofer_src.py'
        cmd = (rf'pyinstaller {loc} --onefile --uac-admin --name uuid_spoofer')
        subprocess.call(cmd)
        
        print(Fore.RED + '\n\n[INFO] LOCATION : dist')
        print(Fore.GREEN + '[INFO] OPERATION FINISH')
        os.remove('uuid_spoofer.spec')

        input(Fore.BLUE + '\n\nPRESS ENTER TO RETURN TO MENU')
  

    elif choice =="N":
        print(red + '[INFO] You have to compile the file as an .exe for it to work')

        input(blue + '\n\nPRESS ENTER TO RETURN TO MENU')