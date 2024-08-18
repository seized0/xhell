import asyncio
from pystyle import *
from colorama import *
import os
import time
from utilities.Program import phonelookup, subdomainfinder, srcdumper, dmall, accnuker, iplookup, credits,hypesquadchanger, usernamesearcher, statuschanger, idtotoken
import ctypes
import sys
import random
import requests
import discord
import subprocess
import seizcord
################################################################

            # discord : uhq.s
            # tiktok  : https://tiktok.com/@uhq.s
            # server  : https://discord.gg/wyUuYr9DEN
            # dev     : uhq.s
            # owner   : uhq.s

################################################################


green = Fore.GREEN
red = Fore.RED
magenta = Fore.MAGENTA
blue = Fore.BLUE
r = Fore.WHITE
lmagenta = Fore.LIGHTMAGENTA_EX
lred = Fore.LIGHTRED_EX
yellow = Fore.YELLOW
cyan = Fore.CYAN
lgreen = Fore.LIGHTGREEN_EX




def contitle(title):
    ctypes.windll.kernel32.SetConsoleTitleW(title)

txt = "⭐ By uhq.s    |    Xhell V2 ❤️"


banner = """
                                                     
@@@  @@@     @@@  @@@  @@@@@@@@  @@@       @@@       
@@@  @@@     @@@  @@@  @@@@@@@@  @@@       @@@       
@@!  !@@     @@!  @@@  @@!       @@!       @@!        PRESS ENTER
!@!  @!!     !@!  @!@  !@!       !@!       !@!        
 !@@!@!      @!@!@!@!  @!!!:!    @!!       @!!        V2
  @!!!       !!!@!!!!  !!!!!:    !!!       !!!       
 !: :!!      !!:  !!!  !!:       !!:       !!:       
:!:  !:!     :!:  !:!  :!:        :!:       :!:      
 ::  :::     ::   :::   :: ::::   :: ::::   :: ::::  
 :   ::       :   : :  : :: ::   : :: : :  : :: : :  
                                                    
"""

banner1 = """
                                                     

    )      )       (     (     
 ( /(   ( /(       )\ )  )\ )  
 )\())  )\()) (   (()/( (()/(  
((_)\  ((_)\  )\   /(_)) /(_)) 
__((_)  _((_)((_) (_))  (_))      PRESS ENTER
\ \/ / | || || __|| |   | |       
 >  <  | __ || _| | |__ | |__     V2
/_/\_\ |_||_||___||____||____| 
                               

                                                    
"""


banner2 = """


      :::    :::          :::    ::: :::::::::: :::        :::  
     :+:    :+:          :+:    :+: :+:        :+:        :+:   
     +:+  +:+           +:+    +:+ +:+        +:+        +:+    
     +#++:+            +#++:++#++ +#++:++#   +#+        +#+     
   +#+  +#+           +#+    +#+ +#+        +#+        +#+          PRESS ENTER
 #+#    #+#          #+#    #+# #+#        #+#        #+#        
###    ###          ###    ### ########## ########## ##########     V2


"""


banner3 = """

=======================================================
=   ==   =======  ====  ==        ==  ========  =======   PRESS ENTER
==  ==  ========  ====  ==  ========  ========  =======
==  ==  ========  ====  ==  ========  ========  =======
===    =========  ====  ==  ========  ========  =======
====  ==========        ==      ====  ========  =======
===    =========  ====  ==  ========  ========  =======
==  ==  ========  ====  ==  ========  ========  =======   V2
==  ==  ========  ====  ==  ========  ========  =======
=  ====  =======  ====  ==        ==        ==        =
=======================================================

"""


bannermenu = rf"""


                              ▀████    ▐████▀         ▄█    █▄       ▄████████  ▄█        ▄█       
                                ███▌   ████▀         ███    ███     ███    ███ ███       ███        
                                 ███  ▐███           ███    ███     ███    █▀  ███       ███        V2
                                 ▀███▄███▀          ▄███▄▄▄▄███▄▄  ▄███▄▄▄     ███       ███       
                                 ████▀██▄          ▀▀███▀▀▀▀███▀  ▀▀███▀▀▀     ███       ███       
                                ▐███  ▀███           ███    ███     ███    █▄  ███       ███       
                               ▄███     ███▄         ███    ███     ███    ███ ███▌    ▄ ███▌    ▄                
                              ████       ███▄        ███    █▀      ██████████ █████▄▄██ █████▄▄██ 
                                                                               ▀         ▀                        
[!] https://tiktok.com/@uhq.s
[+] https://github.com/seized0/xhell                  
[-] https://discord.gg/wyUuYr9DEN    

    ════════════════════════════════════════════════════════════════════════════════════════════════════════════════════
                                
              {lred}[1] SUBDOMAIN FINDER               {yellow}[5] ACCOUNT NUKER                  {green}[9]  USERNAME SEARCHER
                                                                                                                   
              {red}[2] SRC DUMPER                     {yellow}[6] HYPESQUAD CHANGER              {green}[10] ID TO TOKEN
                                                                                                                    
              {lred}[3] IP LOOKUP                      {yellow}[7] DM ALL                         {green}[0] CREDITS
                                                                                                                   
              {red}[4] PHONE LOOKUP                   {yellow}[8] STATUS ROTATOR                 {red}[00] NEXT PAGE- >
           
    ════════════════════════════════════════════════════════════════════════════════════════════════════════════════════

"""


bannermenu2 = rf"""


                              ▀████    ▐████▀         ▄█    █▄       ▄████████  ▄█        ▄█       
                                ███▌   ████▀         ███    ███     ███    ███ ███       ███        
                                 ███  ▐███           ███    ███     ███    █▀  ███       ███        V2
                                 ▀███▄███▀          ▄███▄▄▄▄███▄▄  ▄███▄▄▄     ███       ███       
                                 ████▀██▄          ▀▀███▀▀▀▀███▀  ▀▀███▀▀▀     ███       ███       
                                ▐███  ▀███           ███    ███     ███    █▄  ███       ███       
                               ▄███     ███▄         ███    ███     ███    ███ ███▌    ▄ ███▌    ▄                
                              ████       ███▄        ███    █▀      ██████████ █████▄▄██ █████▄▄██ 
                                                                               ▀         ▀                        
[!] https://tiktok.com/@uhq.s
[+] https://github.com/seized0/xhell                  
[-] https://discord.gg/wyUuYr9DEN    

    ════════════════════════════════════════════════════════════════════════════════════════════════════════════════════
                                
              {lred}[11] SOON                    {yellow}[15] SOON                  {green}[19] SOON
                                                                                                                   
              {red}[12] SOON                    {yellow}[16] SOON                  {green}[20] SOON
                                                                                                                    
              {lred}[13] SOON                    {yellow}[17] SOON                  {green}[0] CREDITS  
                                                                                                                   
              {red}[14] SOON                    {yellow}[18] SOON                  {red}[00] <- PREV PAGE 
           
    ════════════════════════════════════════════════════════════════════════════════════════════════════════════════════

"""



