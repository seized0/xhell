################################################################

            # discord : uhq.s
            # tiktok  : https://tiktok.com/@uhq.s
            # server  : https://discord.gg/wyUuYr9DEN
            # dev     : uhq.s
            # owner   : uhq.s
            # github  : https://github.com/seized0

#################################################################
pyfuscate_code = r"""


#!/usr/bin/env python
# coding: utf-8
# By Sandaru Ashen: https://github.com/Sl-Sanda-Ru, https://t.me/Sl_Sanda_Ru


import os
import sys
import subprocess
import argparse
import random
import time
import marshal
import lzma
import gzip
import bz2
import binascii
import zlib


def prett(text):
    return text.title().center(os.get_terminal_size().columns)


PYTHON_VERSION = "python" + ".".join(str(i) for i in sys.version_info[:2])
try:
    import requests
    import tqdm
    import colorama
    import pyfiglet
except ModuleNotFoundError:
    if (
        subprocess.run(
            [PYTHON_VERSION, "-m", "pip", "install", "-r", "requirements.txt"]
        ).returncode
        == 0
    ):
        print("\x1b[1m\x1b[92m" + prett("[+] dependencies installed"))
        sys.exit("\x1b[1m\x1b[92m" + prett("[+] run the program again"))
    elif subprocess.run(["pip3", "install", "-r", "requirements.txt"]).returncode == 0:
        print("\x1b[1m\x1b[92m" + prett("[+] dependencies installed"))
        sys.exit("\x1b[1m\x1b[92m" + prett("[+] run the program again"))
    else:
        print(
            "\x1b[1m\x1b[31m"
            + prett("[!] something error occured while installing dependencies")
        )
        sys.exit(
            "\x1b[1m\x1b[31m"
            + prett("maybe pip isn't installed or requirements.txt file not available?")
        )
BLU = colorama.Style.BRIGHT + colorama.Fore.BLUE
CYA = colorama.Style.BRIGHT + colorama.Fore.CYAN
GRE = colorama.Style.BRIGHT + colorama.Fore.GREEN
YEL = colorama.Style.BRIGHT + colorama.Fore.YELLOW
RED = colorama.Style.BRIGHT + colorama.Fore.RED
MAG = colorama.Style.BRIGHT + colorama.Fore.MAGENTA
LIYEL = colorama.Style.BRIGHT + colorama.Fore.LIGHTYELLOW_EX
LIRED = colorama.Style.BRIGHT + colorama.Fore.LIGHTRED_EX
LIMAG = colorama.Style.BRIGHT + colorama.Fore.LIGHTMAGENTA_EX
LIBLU = colorama.Style.BRIGHT + colorama.Fore.LIGHTBLUE_EX
LICYA = colorama.Style.BRIGHT + colorama.Fore.LIGHTCYAN_EX
LIGRE = colorama.Style.BRIGHT + colorama.Fore.LIGHTGREEN_EX
CLEAR = "cls" if os.name == "nt" else "clear"
COLORS = BLU, CYA, GRE, YEL, RED, MAG, LIYEL, LIRED, LIMAG, LIBLU, LICYA, LIGRE
FONTS = (
    "basic",
    "o8",
    "cosmic",
    "graffiti",
    "chunky",
    "epic",
    "poison",
    "doom",
    "avatar",
)

global LATEST_VER
colorama.init(autoreset=True)


def encode(source: str) -> str:
    selected_mode = random.choice((lzma, gzip, bz2, binascii, zlib))
    marshal_encoded = marshal.dumps(compile(source, "Py-Fuscate", "exec"))
    if selected_mode is binascii:
        return "import marshal,lzma,gzip,bz2,binascii,zlib;exec(marshal.loads(binascii.a2b_base64({})))".format(
            binascii.b2a_base64(marshal_encoded)
        )
    return "import marshal,lzma,gzip,bz2,binascii,zlib;exec(marshal.loads({}.decompress({})))".format(
        selected_mode.__name__, selected_mode.compress(marshal_encoded)
    )


def logo() -> None:
    _ = subprocess.run([CLEAR], shell=True)
    font = random.choice(FONTS)
    color1 = random.choice(COLORS)
    color2 = random.choice(COLORS)
    while color1 == color2:
        color2 = random.choice(COLORS)
    print(color1 + "_" * os.get_terminal_size().columns, end="\n" * 2)
    print(
        color2
        + pyfiglet.figlet_format(
            "Py\nFuscate",
            font=font,
            justify="center",
            width=os.get_terminal_size().columns,
        ),
        end="",
    )
    print(color1 + "_" * os.get_terminal_size().columns, end="\n" * 2)


def parse_args():
    parser = argparse.ArgumentParser(description="obfuscate python programs".title())
    parser._optionals.title = "syntax".title()
    parser.add_argument(
        "-i", "--input", type=str, help="input file name".title(), required=True
    )
    parser.add_argument(
        "-o", "--output", type=str, help="output file name".title(), required=True
    )
    parser.add_argument(
        "-c",
        "--complexity",
        type=int,
        help="complexity of obfuscation. 100 recomended".title(),
        required=True,
    )
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit()
    return parser.parse_args()




def main():
    args = parse_args()
    print(random.choice(COLORS) + "\t[+] encoding ".title() + args.input)
    with tqdm.tqdm(total=args.complexity) as pbar:
        with open(args.input) as iput:
            for i in range(args.complexity):
                if i == 0:
                    encoded = encode(source=iput.read())
                else:
                    encoded = encode(source=encoded)
                time.sleep(0.1)
                pbar.update(1)
    with open(args.output, "w") as output:
        output.write(
            f'# Encoded By Py-Fuscate\n# https://github.com/Sl-Sanda-Ru/Py-Fuscate\n# Make Sure You\'re Running The Program With {PYTHON_VERSION} Otherwise It May Crash\n# To Check Your Python Version Run "python -V" Command\ntry:\n\t{encoded}\nexcept KeyboardInterrupt:\n\texit()'
        )
    print(LIGRE + "\t[+] encoding successful!\n\tsaved as ".title() + args.output)


if __name__ == "__main__":
    logo()
    main()


"""
import colorama
from colorama import *
import os

red = Fore.RED
blue = Fore.BLUE
cyan = Fore.CYAN
magenta = Fore.MAGENTA
green = Fore.GREEN


async def obf():
    os.system('cls')
    print(cyan + """

██████╗ ██╗   ██╗     ██████╗ ██████╗ ███████╗
██╔══██╗╚██╗ ██╔╝    ██╔═══██╗██╔══██╗██╔════╝
██████╔╝ ╚████╔╝     ██║   ██║██████╔╝█████╗  
██╔═══╝   ╚██╔╝      ██║   ██║██╔══██╗██╔══╝  
██║        ██║       ╚██████╔╝██████╔╝██║     
╚═╝        ╚═╝        ╚═════╝ ╚═════╝ ╚═╝     

1. PyObfuscator          2. Pyarmor         3. PyFuscate (BEST)                       
""")
    method = input('METHOD : ')
    if method =='1':
        filename = input(cyan + '\n\nPYTHON FILE NAME : ')
        os.system(f'PyObfuscator {filename}')
        print(red + f'FINISH \n\n OBF FILENAME : {filename}_obfu')

    elif method =='2':
        filename = input(cyan + '\n\nPYTHON FILE NAME : ')
        os.system(f'pyarmor gen {filename}')
        print(red + f'FINISH \n\nFOLDER : dist\nFILENAME : {filename}')

    elif method =='3':
        filename = input(cyan + '\n\nPYTHON FILE NAME : ')
        with open('py_fuscate.py', 'w') as f:
            f.write(pyfuscate_code)

        os.system(f'python py_fuscate.py -i {filename} -o obf_{filename} -c 100')
        os.remove('py_fuscate.py')

    
    input(red + '\n\n[!] PRESS ENTER TO RETURN TO MENU')