from utilities.Program.utils.utils import *


################################################################

            # discord : uhq.s
            # tiktok  : https://tiktok.com/@uhq.s
            # server  : https://discord.gg/wyUuYr9DEN
            # dev     : uhq.s
            # owner   : uhq.s

################################################################

async def menu2():
    os.system('cls')
    print(Colorate.Vertical(Colors.red_to_yellow, f'{bannermenu2}'))

    choice = input(Fore.RED + '\n[#] CHOICE : ')

    if choice == "0":
        await credits.credits()
        await menu2()

    
    elif choice == "11":
        os.system('cls')
        print(red + 'SOON...')
        input(blue + '\n\nPRESS ENTER TO RETURN TO MENU')
        await menu2()

    elif choice == "12":
        os.system('cls')
        print(red + 'SOON...')
        input(blue + '\n\nPRESS ENTER TO RETURN TO MENU')
        await menu2()

    elif choice == "13":
        os.system('cls')
        print(red + 'SOON...')
        input(blue + '\n\nPRESS ENTER TO RETURN TO MENU')
        await menu2()

    elif choice == "14":
        os.system('cls')
        print(red + 'SOON...')
        input(blue + '\n\nPRESS ENTER TO RETURN TO MENU')
        await menu2()

    elif choice == "15":
        os.system('cls')
        print(red + 'SOON...')
        input(blue + '\n\nPRESS ENTER TO RETURN TO MENU')
        await menu2()

    elif choice == "16":
        os.system('cls')
        print(red + 'SOON...')
        input(blue + '\n\nPRESS ENTER TO RETURN TO MENU')
        await menu2()

    elif choice == "17":
        os.system('cls')
        print(red + 'SOON...')
        input(blue + '\n\nPRESS ENTER TO RETURN TO MENU')
        await menu2()

    elif choice == "18":
        os.system('cls')
        print(red + 'SOON...')
        input(blue + '\n\nPRESS ENTER TO RETURN TO MENU')
        await menu2()

    elif choice == "19":
        os.system('cls')
        print(red + 'SOON...')
        input(blue + '\n\nPRESS ENTER TO RETURN TO MENU')
        await menu2()

    elif choice == "20":
        os.system('cls')
        print(red + 'SOON...')
        input(blue + '\n\nPRESS ENTER TO RETURN TO MENU')
        await menu2()


    elif choice == "00":
        os.system('cls')
        print(blue + 'WAIT....')
        time.sleep(1)
        pass


contitle(txt)


def clear():
    os.system('cls')

allbanner = [banner, banner1, banner2]
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
            await accnuker.accnuker()

        elif choice =="6":
            await hypesquadchanger.hypesquadchanger()

        elif choice =="7":
            await dmall.dmall()

        elif choice =="8":
            await statuschanger.statuschanger()

        elif choice =="9":
            await usernamesearcher.usernamesearcher()

        elif choice =="10":
            await idtotoken.idtotoken()
        
        elif choice =="0":
            await credits.credits()

        elif choice =="00":
            os.system('cls')
            print(blue + 'WAIT....')
            time.sleep(1)
            await menu2()


        else:
            input(red +'[!] ERROR : INVALID CHOICE')
        








asyncio.run(menu())