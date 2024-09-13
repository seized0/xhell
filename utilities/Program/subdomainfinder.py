################################################################

            # discord : uhq.s
            # tiktok  : https://tiktok.com/@uhq.s
            # server  : https://discord.gg/wyUuYr9DEN
            # dev     : uhq.s
            # owner   : uhq.s
            # github  : https://github.com/seized0

#################################################################

from utilities.Program.utils.utils import *
import requests
 
# DOC : https://developer.mozilla.org/fr/docs/Web/HTTP/Status

green = Fore.GREEN
red = Fore.RED
magenta = Fore.MAGENTA
blue = Fore.BLUE
reset = Fore.WHITE
lmagenta = Fore.LIGHTMAGENTA_EX


banner = lmagenta + r"""

⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⣤⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⡤⠤⣦⢴⠟⠋⠁⠀⢻⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⣠⡶⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⣘⣿⣀⠀⠀⠀⠀⠀⠀⢠⣦⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⠉⠀⠀⠀⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢉⡀⠀⠀⠀⠀⠀⢴⣾⡙⣻⡷⠂⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣆⠀⠀⠀⠀⠀⠘⢿⡏⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣻⠀⠀⠀⠀⠀⠀⠀⠀⠀⢒⠆⠀⠀⢰⣿⣦⠤⠔⠀⢹⣧⣀⣀⠀⠀⠀⠈⠀⡀⠀⠀⠀
⠀⠀⣸⣆⠀⠀⠀⠀⠀⢸⡏⠀⠀⠀⣀⡀⠀⠀⠀⠀⠾⠂⠀⠀⠀⢻⡏⠀⠀⢾⡛⠻⣯⣉⠁⠀⠀⠀⢀⡿⣤⣀⡀
⠠⣴⣟⣻⡷⢶⠀⠀⠀⣾⠀⠀⠀⢰⣿⣿⠆⠀⠀⠀⠀⠀⠀⠀⠀⠈⠓⠠⠀⠈⠛⠛⠛⣿⠛⠂⠀⠐⠻⣷⣼⠟⠉   uhq.s <3  
⠀⠀⠹⡿⠀⠀⠀⠀⠀⣿⣠⣀⣒⠀⢋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡿⠔⠀⠀⠀⠀⠈⠋⠀⠀
⠀⣠⠀⠀⠀⠀⠀⢀⣤⣿⠟⣿⡉⠀⠘⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣠⡿⢶⣤⡀⠀⠘⠟⢁⣿⡞⠛⠉⠀⠀⠀⠀⠀⠀⠀⣰⣤⣤⡶⠤⣤⣄⠀⠀⠀⠀⠺⣧⡀⠀⠀⣴⠟⢿⡆⠀⠀⠀
⠛⢷⣾⠋⠀⠀⠀⠀⣾⠛⢷⣤⣀⡀⠀⠀⠀⠀⠀⣼⠋⡁⢻⡀⢀⠀⠉⠀⠀⠀⠀⠀⠈⢻⣤⠀⣿⠐⢸⡇⠀⠀⠀
⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠻⣷⠄⠀⠀⠀⠁⠀⢀⣸⡷⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣷⡏⠀⣾⠇⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡏⠀⠀⠀⠀⠀⠀⠀⠘⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣷⣼⡏⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⠋⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

"""
async def subdomainfinder():
    os.system('cls')
    print(banner)
    ask = input('[?] URL : ').rstrip('/')

    with open('words.txt', 'r') as f:  # CHANGE words.txt IF YOU HAVE YOUR OWN WORDLIST  CHANGE words.txt SI TU AS TA PROPRE WORDLIST
        keywords = [line.strip() for line in f]

    urls = [f'{ask}/{kw}' for kw in keywords]

    responses = [requests.get(url) for url in urls]

    for i, response in enumerate(responses):
        if response.status_code == 200:
            print(green + f'\n200 Ok FOR : {urls[i]}')
        elif response.status_code == 400:
            print(red + f'\n400 Bas request FOR : {urls[i]}')
        elif response.status_code ==500:
            print(blue + f'500 Internal Server Error FOR : {urls[i]}')
        elif response.status_code ==403:
            print(red + f'403 Forbidden FOR : {urls[i]}')
        elif response.status_code ==401:
            print(red + f'401 UNAUTHORIZED FOR : {urls[i]}')
        elif response.status_code ==404:
            print(red + f'404 Not Found FOR : {urls[i]}')
        elif response.status_code ==408:
            print(blue + f'408 Request Timeout FOR : {urls[i]}')
        elif response.status_code ==429:
            print(blue + f'429 Too Many Requests FOR : {urls[i]}')
        elif response.status_code ==502:
            print(red + f'502 Bad Gateway FOR : {urls[i]}')
    print(reset)
    input(lmagenta + '\n[!] PRESS ENTER TO RETURN TO MENU')

