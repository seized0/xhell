################################################################

            # discord : uhq.s
            # tiktok  : https://tiktok.com/@uhq.s
            # server  : https://discord.gg/wyUuYr9DEN
            # dev     : uhq.s
            # owner   : uhq.s
            # github  : https://github.com/seized0

#################################################################

import asyncio
from pystyle import *
from colorama import *
import os
import time
from utilities.Program import phonelookup, toolinfo,subdomainfinder, srcdumper, accnuker, iplookup, credits,hypesquadchanger, usernamesearcher, statuschanger, idtotoken, webhooksdeleter, webhookspammer,tokenchecker,py2exe,obf,tokenleaver,seizuremode,domainlookup,doxtool,dmall
import ctypes
import sys
import random
import requests
import subprocess
import seizcord
import seizhooks




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
lblue = Fore.LIGHTBLUE_EX



def contitle(title):
    ctypes.windll.kernel32.SetConsoleTitleW(title)

txt = "⭐ By uhq.s    |    Xhell V3 🐬"


banner = """
                                                     
@@@  @@@     @@@  @@@  @@@@@@@@  @@@       @@@       
@@@  @@@     @@@  @@@  @@@@@@@@  @@@       @@@       
@@!  !@@     @@!  @@@  @@!       @@!       @@!        PRESS ENTER
!@!  @!!     !@!  @!@  !@!       !@!       !@!        
 !@@!@!      @!@!@!@!  @!!!:!    @!!       @!!        V3
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
 >  <  | __ || _| | |__ | |__     V3
/_/\_\ |_||_||___||____||____| 
                               

                                                    
"""


banner2 = """


      :::    :::          :::    ::: :::::::::: :::        :::  
     :+:    :+:          :+:    :+: :+:        :+:        :+:   
     +:+  +:+           +:+    +:+ +:+        +:+        +:+    
     +#++:+            +#++:++#++ +#++:++#   +#+        +#+     
   +#+  +#+           +#+    +#+ +#+        +#+        +#+          PRESS ENTER
 #+#    #+#          #+#    #+# #+#        #+#        #+#        
###    ###          ###    ### ########## ########## ##########     V3


"""


banner3 = """

=======================================================
=   ==   =======  ====  ==        ==  ========  =======   PRESS ENTER
==  ==  ========  ====  ==  ========  ========  =======
==  ==  ========  ====  ==  ========  ========  =======
===    =========  ====  ==  ========  ========  =======
====  ==========        ==      ====  ========  =======
===    =========  ====  ==  ========  ========  =======
==  ==  ========  ====  ==  ========  ========  =======   V3
==  ==  ========  ====  ==  ========  ========  =======
=  ====  =======  ====  ==        ==        ==        =
=======================================================

"""


bannermenu = rf"""

                              ▀████    ▐████▀         ▄█    █▄       ▄████████  ▄█        ▄█       
                                ███▌   ████▀         ███    ███     ███    ███ ███       ███        
                                 ███  ▐███           ███    ███     ███    █▀  ███       ███        
                                 ▀███▄███▀          ▄███▄▄▄▄███▄▄  ▄███▄▄▄     ███       ███       
                                 ████▀██▄          ▀▀███▀▀▀▀███▀  ▀▀███▀▀▀     ███       ███       
                                ▐███  ▀███           ███    ███     ███    █▄  ███       ███       
                               ▄███     ███▄         ███    ███     ███    ███ ███▌    ▄ ███▌    ▄                
                              ████       ███▄        ███    █▀      ██████████ █████▄▄██ █████▄▄██ 
                                                                               ▀         ▀                        
[!] https://tiktok.com/@uhq.s                              
                                                      discord.gg/xhell  
[+] https://github.com/seized0/xhell                    [ UTILITIES ]

    ════════════════════════════════════════════════════════════════════════════════════════════════════════════════════
                                
              {lred}[1] SUBDOMAIN FINDER               {yellow}[5] PY TO EXE                {green}[9]  USERNAME TRACKER
                                                                                                                   
             {red} [2] SRC DUMPER                     {yellow}[6] OBFUSCATOR               {green}[10] DOX TOOL
                                                                                                                    
              {lred}[3] IP LOOKUP                      {yellow}[7] DOMAIN LOOKUP            {green}[0]  CREDITS    
                                                                                                                   
             {red} [4] PHONE LOOKUP                   {yellow}[8] TOOLS INFOS              {red}[00] NEXT PAGE -->        
           
    ════════════════════════════════════════════════════════════════════════════════════════════════════════════════════

"""


bannermenu2 = rf"""
                              ▀████    ▐████▀         ▄█    █▄       ▄████████  ▄█        ▄█       
                                ███▌   ████▀         ███    ███     ███    ███ ███       ███        
                                 ███  ▐███           ███    ███     ███    █▀  ███       ███        
                                 ▀███▄███▀          ▄███▄▄▄▄███▄▄  ▄███▄▄▄     ███       ███       
                                 ████▀██▄          ▀▀███▀▀▀▀███▀  ▀▀███▀▀▀     ███       ███       
                                ▐███  ▀███           ███    ███     ███    █▄  ███       ███       
                               ▄███     ███▄         ███    ███     ███    ███ ███▌    ▄ ███▌    ▄                
                              ████       ███▄        ███    █▀      ██████████ █████▄▄██ █████▄▄██ 
                                                                               ▀         ▀                        
[!] https://tiktok.com/@uhq.s
                                                discord.gg/xhell               
                                                  [ DISCORD ]
[+] https://github.com/seized0/xhell                                       
    ════════════════════════════════════════════════════════════════════════════════════════════════════════════════════
                                
              {blue}[11] WEBHOOK SPAMMER         {cyan}[15] ACCOUNT NUKER          {lmagenta}[19] SEIZURE MODE
                                                                                                                   
              {blue}[12] WEBHOOK DELETER         {cyan}[16] HYPESQUAD CHANGER      {lmagenta}[20] RATE LIMIT   
                                                                                                                    
              {blue}[13] TOKEN LEAVER            {cyan}[17] ID TO TOKEN            {lmagenta}[0] CREDITS  
                                                                                                                   
              {blue}[14] TOKEN CHECKER           {cyan}[18] STATUS CHANGER         {cyan}[00] <- PREV PAGE 
           
    ════════════════════════════════════════════════════════════════════════════════════════════════════════════════════

"""

