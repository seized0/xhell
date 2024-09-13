################################################################

            # discord : uhq.s
            # tiktok  : https://tiktok.com/@uhq.s
            # server  : https://discord.gg/wyUuYr9DEN
            # dev     : uhq.s
            # owner   : uhq.s
            # github  : https://github.com/seized0

#################################################################

from utilities.Program.utils.utils import *
import subprocess

blue = Fore.BLUE
magenta = Fore.MAGENTA
red = Fore.RED

async def dumper():
  os.system('cls')
  print(f"""
                                                      

  {blue} /$$   /$$           /$$ /$$   {red}    /$$$$$$$                                                       
  {blue}| $$  | $$          | $$| $$   {red}   | $$__  $$                                                      
  {blue}| $$  | $$  /$$$$$$ | $$| $$   {red}   | $$  \ $$ /$$   /$$ /$$$$$$/$$$$   /$$$$$$   /$$$$$$   /$$$$$$ 
  {blue}| $$$$$$$$ /$$__  $$| $$| $$   {red}   | $$  | $$| $$  | $$| $$_  $$_  $$ /$$__  $$ /$$__  $$ /$$__  $$
  {blue}| $$__  $$| $$$$$$$$| $$| $$   {red}   | $$  | $$| $$  | $$| $$ \ $$ \ $$| $$  \ $$| $$$$$$$$| $$  \__/
  {blue}| $$  | $$| $$_____/| $$| $$   {red}   | $$  | $$| $$  | $$| $$ | $$ | $$| $$  | $$| $$_____/| $$      
  {blue}| $$  | $$|  $$$$$$$| $$| $$   {red}   | $$$$$$$/|  $$$$$$/| $$ | $$ | $$| $$$$$$$/|  $$$$$$$| $$      
  {blue}|__/  |__/ \_______/|__/|__/   {red}   |_______/  \______/ |__/ |__/ |__/| $$____/  \_______/|__/      
  {blue}                               {red}                                     | $$                          
  {blue}                               {red}                                     | $$                          
  {blue}                               {red}                                     |__/                          

  
[INFO] SI DES FENETRES D'ERREUR S'OUVRENT NE LES FERMES PAS, C'EST NORMAL ELLES SE FERMERONT TOUTE SEULES
[INFO] IF ERROR WINDOWS OPEN DO NOT CLOSE THEM, IT'S NORMAL THEY WILL CLOSE THEMSELVES

  """)

  file = input(red + '\n\n[#] FILE : ')
  cmd = f"pydumpck {file}"
  print('\n\n')
  subprocess.call(cmd)
  os.remove('log.log')
  input(blue + '\n\n[INFO] OPERATION FINISHED.')
