from utilities.Program.utils.utils import *

################################################################

            # discord : uhq.s
            # tiktok  : https://tiktok.com/@uhq.s
            # server  : https://discord.gg/wyUuYr9DEN
            # dev     : uhq.s
            # owner   : uhq.s
            # github  : https://github.com/seized0

################################################################

async def menu2():
    os.system('cls')
    print(Colorate.Vertical(Colors.blue_to_purple, f'{bannermenu2}'))

    choice = input(Fore.RED + '[#] CHOICE : ')

    if choice == "0":
        await credits.credits()
        await menu2()

    
    elif choice == "11":
        await webhookspammer.webhookspammer()
        await menu2()

    elif choice == "12":
        await webhooksdeleter.webhookdeleter()
        await menu2()

    elif choice == "13":
        await tokenleaver.tokenleaver()
        await menu2()

    elif choice == "14":
        await tokenchecker.tokenchecker()
        await menu2()

    elif choice == "15":
        await accnuker.accnuker()
        await menu2()

    elif choice == "16":
        await hypesquadchanger.hypesquadchanger()
        await menu2()

    elif choice == "17":
        await idtotoken.idtotoken()
        await menu2()

    elif choice == "18":
        await statuschanger.statuschanger()
        await menu2()

    elif choice == "19":
        await seizuremode.flashbang()
        await menu2()

    elif choice == "20":
        await dmall.dmall()
        await menu2()


    elif choice =="00":
        os.system('cls')
        Write.Print(f"\n\n\n\n\n\n\n\n\n\n\n\n                                                 PLEASE WAIT...", Colors.red_to_yellow, interval=0.009)
        time.sleep(0.5)
        pass

    else:
        input(red +'[!] ERROR : INVALID CHOICE')
        await menu2()


contitle(txt)


def clear():
    os.system('cls')

allbanner = [banner, banner1, banner2, banner3]
bannerchoice = random.choice(allbanner)


Anime.Fade(Center.Center(bannerchoice), Colors.red_to_yellow, Colorate.Vertical, enter=True)


async def menu():
    while True:
        clear()
        print(Colorate.Vertical(Colors.red_to_yellow, f'{bannermenu}'))
        
        choice = input(Fore.RED + '[#] CHOICE : ')

        if choice =="1":
            await subdomainfinder.subdomainfinder()
            
        elif choice =="2":
            await srcdumper.dumper()

        elif choice =="3":
            await iplookup.iplookup()

        elif choice =="4":
            await phonelookup.phonelookup()

        elif choice =="5":
            await py2exe.py2exe()

        elif choice =="6":
            await obf.obf()

        elif choice =="7":
            await domainlookup.domainlookup()

        elif choice =="8":
            await toolinfo.toolinfo()

        elif choice =="9":
            await usernamesearcher.usernamesearcher()

        elif choice =="10":
            await doxtool.doxtool()
        
        elif choice =="0":
            await credits.credits()

     
        elif choice =="00":
            os.system('cls')
            Write.Print(f"\n\n\n\n\n\n\n\n\n\n\n\n                                                 PLEASE WAIT...", Colors.blue_to_purple, interval=0.009)
            time.sleep(0.5)
            await menu2()


        else:
            input(red +'[!] ERROR : INVALID CHOICE')
        








asyncio.run(menu())