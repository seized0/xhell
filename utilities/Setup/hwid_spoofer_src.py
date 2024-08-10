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

def hwidspoofer():

    new_hwid = str(uuid.uuid4()).upper().replace("-", "")


    try:

            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Control\IDConfigDB\Hardware Profiles\0001", 0, winreg.KEY_ALL_ACCESS)
            winreg.SetValueEx(key, "HwProfileGuid", 0, winreg.REG_SZ, new_hwid)
            winreg.SetValueEx(key, "HARDWAREPROFILEGUID", 0, winreg.REG_SZ, new_hwid)
            winreg.CloseKey(key)

            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Control\SystemInformation", 0, winreg.KEY_ALL_ACCESS)
            winreg.SetValueEx(key, "ProcessorIdentifier", 0, winreg.REG_SZ, new_hwid)
            winreg.SetValueEx(key, "BaseBoardProduct", 0, winreg.REG_SZ, new_hwid)
            winreg.CloseKey(key)

            print(f"NEW HWID : {new_hwid}")
    except Exception as e:
            print(Fore.RED + f"[!] ERROR : {e}")


    input(Fore.BLUE + '\n\nHWID CHANGED SUCCESFULY')

hwidspoofer()