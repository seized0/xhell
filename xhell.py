from utilities.Setup.utils import *


################################################################

            # discord : uhq.s
            # tiktok  : https://tiktok.com/@paiementsecurise
            # serveur : https://discord.gg/wyUuYr9DEN
            # dev : uhq.s
            # owner : uhq.s

################################################################

contitle(txt)
def get_latest_release_version(repo_owner, repo_name):
    url = f'https://api.github.com/repos/{repo_owner}/{repo_name}/releases/latest'
    response = requests.get(url)
    
    if response.status_code == 200:
        release_info = response.json()
        latest_version = release_info['tag_name']
        return latest_version
    else:
        print(f"Error in the request : {response.status_code}")
        return None

def update_application(repo_owner, repo_name, current_version):
    latest_version = get_latest_release_version(repo_owner, repo_name)

    if latest_version is not None and current_version < latest_version:
        print(f"A new version is available : {latest_version}")
        
        download_url = f'https://github.com/{repo_owner}/{repo_name}/archive/{latest_version}.zip'
        download_path = 'latest_version.zip'
        
        with requests.get(download_url, stream=True) as response:
            with open(download_path, 'wb') as file:
                for chunk in response.iter_content(chunk_size=8192):
                    file.write(chunk)
        

        
        
        print("Update Finished.")
        exit()
    else:
        pass
        

repo_owner = 'seized0'
repo_name = 'xhell'
current_version = 'v0.0.1'

update_application(repo_owner, repo_name, current_version)

def clear():
    os.system('cls')

banner = """
⠀⢰⣶⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⣀⣀⣠⣤⣤⣤⣤⣤⣤⣤⣦⣤⣤⣤⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢀⣸⣿⣧⣀⣀⣀⣀⣠⡾⣿⠿⠿⣿⣿⣿⣿⣶⣿⣷⣾⣿⣿⣿⣿⣿⣿⣿⣿⣟⣻⣛⣛⣿⣻⣿⣛⣛⣛⣻⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠘⠻⢿⡿⠟⠛⠿⠿⠿⠷⠟⠓⠛⠛⢿⣿⣿⣿⣿⣧⣼⣿⣤⣾⣟⣿⣿⣿⣿⠿⣿⣿⣛⣻⣿⣿⡛⢛⡿⢿⠿⢿⠿⣿⣿⣿⣶⣶⡤⣴⠒⠒⠶⠤⠤⣄⣀⣀⣀⠀⠀
⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠛⠏⠉⠉⠙⣿⣟⣿⣿⣿⣿⡟⠛⢻⣿⣿⣷⣾⣿⡿⠿⣿⣿⣿⠿⢾⢉⠁⠐⠂⣲⡀⢤⣤⢩⣹⣇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⠋⠿⠳⠤⠯⠼⢿⣭⣿⢿⠁⠀⠀⠉⠙⠳⠷⣦⣤⣤⣬⣙⠛⠲⠾⣶⣿⠁
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⡏⠀⠀⠀⠀⠀⠀⠈⢿⡙⣌⣧⠀⠀⠀⠀⠀⠀⠉⠙⠛⠿⣿⣦⣴⣶⣾⣿⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠈⣧⠹⣼⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠿⣿⡿⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⣾⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠿⠿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠁⠀
PRESS ENTER            ⠀⠹⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

"""
Anime.Fade(Center.Center(banner), Colors.red_to_yellow, Colorate.Vertical, enter=True)


async def menu():
    while True:
        clear()
        print(Colorate.Vertical(Colors.red_to_yellow, f"""
                                              ..                                   ..       .. 
                                    .H88x.  :~)88:      .uef^"               x .d88"  x .d88"  
                                   x888888X ~:8888    :d88E                   5888R    5888R         
                                  ~   "8888X  %88"    `888E            .u     '888R    '888R     
                                       X8888           888E .z8k    ud8888.    888R     888R         
                                    .xxX8888xxxd>      888E~?888L :888'8888.   888R     888R   
                                   :88888888888"       888E  888E d888 '88%"   888R     888R         
                                   ~   '8888           888E  888E 8888.+"      888R     888R   
                                  xx.  X8888:    .     888E  888E 8888L        888R     888R         
                                 X888  X88888x.x"      888E  888E '8888c. .+  .888B .  .888B . 
                                 X88% : '%8888"       m888N= 888>  "88888%    ^*888%   ^*888%  
                                  "*=~    `""          `Y"   888     "YP'       "%       "%    
[#] https://discord.gg/wyUuYr9DEN                       J88"                               
[$] https://github.com/seized0                          @%                                 
[!] https://tiktok.com/paiementsecurise                 :"                                   
    ════════════════════════════════════════════════════════════════════════════════════════════════════════════════════  
                                
                                 {lred}[1] SUBDOMAIN FINDER{r}                {yellow}[5] ACCOUNT NUKER            
                                                                                                                   
                                 {red}[2] SRC DUMPER{r}                      {yellow}[6] HWID SPOOFER              
                                                                                                                    
                                 {lred}[3] HYPESQUAD CHANGER{r}               {yellow}[7] UUID SPOOFER                           
                                                                                                                   
                                 {red}[4] DM ALL{r}                          {yellow}[8] CREDITS
           
    ════════════════════════════════════════════════════════════════════════════════════════════════════════════════════  
"""))
        
        choice = input(Fore.RED + '\n[#] CHOICE : ')

        if choice =="1":
            await subdomainfinder.subdomainfinder()
            
        elif choice =="2":
            await srcdumper.dumper()

        elif choice =="3":
            await hypesquadchanger.hypesquadchanger()

        elif choice =="4":
            await dmall.dmall()

        elif choice =="5":
            await accnuker.accnuker()

        elif choice =="6":
            await hwidspoofer.hwidspoofer()

        elif choice =="7":
            await uuidspoofer.uuidspoofer()

        elif choice =="8":
            await credits.credits()

        else:
            input(red +'[!] ERROR : INVALID CHOICE')
        








asyncio.run(menu())