################################################################

            # discord : uhq.s
            # tiktok  : https://tiktok.com/@uhq.s
            # server  : https://discord.gg/wyUuYr9DEN
            # dev     : uhq.s
            # owner   : uhq.s
            # github  : https://github.com/seized0

#################################################################


from utilities.Program.utils.utils import *
import os
import whois
import fade

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

ascii = """

 (                                (                              
 )\ )                             )\ )             )             
(()/(         )      ) (         (()/(          ( /(   (         
 /(_))  (    (    ( /( )\  (      /(_)) (    (  )\()) ))\ `  )   
(_))_   )\   )\  ')(_)|(_) )\ )  (_))   )\   )\((_)\ /((_)/(/(   
 |   \ ((_)_((_))((_)_ (_)_(_/(  | |   ((_) ((_) |(_|_))(((_)_\  
 | |) / _ \ '  \() _` || | ' \)) | |__/ _ \/ _ \ / /| || | '_ \) 
 |___/\___/_|_|_|\__,_||_|_||_|  |____\___/\___/_\_\ \_,_| .__/  
                                                         |_|     


"""

async def domainlookup():
    os.system('cls')
    os.system('cls')
    print(fade.water(text=ascii))

    url = input(cyan + '[+] URL : ')
    obj = whois.whois(url)

    print(obj)

    input(red + '\n\n[!] PRESS ENTER TO RETURN TO MENU')