import winreg
import uuid
from colorama import *
################################################################

            # discord : uhq.s
            # tiktok  : https://tiktok.com/@paiementsecurise
            # serveur : https://discord.gg/wyUuYr9DEN
            # dev : uhq.s
            # owner : uhq.s

################################################################
def uuidspoofer():
    try:
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Cryptography", 0, winreg.KEY_READ)
        old_uuid = winreg.QueryValueEx(key, "MachineGuid")[0]
        winreg.CloseKey(key)

        new_uuid = str(uuid.uuid4()).upper()
        
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Cryptography", 0, winreg.KEY_WRITE)
        
        winreg.SetValueEx(key, "MachineGuid", 0, winreg.REG_SZ, new_uuid)
        winreg.CloseKey(key)
        
        print(f"OLD UUID : {old_uuid}")
        print(f"NEW UUID : {new_uuid}")
    except Exception as e:
        print(f"ERREUR : {e}")
    
    

    input(Fore.BLUE + '\n\nUUID CHANGED SUCCESFULY')

uuidspoofer()