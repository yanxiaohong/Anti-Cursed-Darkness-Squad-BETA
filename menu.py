# -*- coding: utf-8 -*-
# usr/env/bin/python3.6
import colorama
import sys
import os
import getpass
from datetime import date
import requests as r





pcnaam = "z3ntl3"
indicatorlogo = f"\033[39m┌─\033[96m[\033[31mz3ntl3\033[96mroot\033[33m@\033[36mEfdal\033[96m]\033[31m─\033[36m[\033[32m/\033[96mr00t\033[32m/\033[39mAnti-Cursed-Darkness-Squad\033[32m/\033[31m{pcnaam}\033[36m]\033[36m\n\033[39m└──\033[31m╼\033[31m╼ \033[33m$\033[36m"

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
"""

space = "          "

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
#
os.system('clear')
print(logo2)


licensiesystem = (r.get("https://pastebin.com/raw/6wdMrW1y").text)



#sifre sistemi


while True:
    if licensiesystem == "VALID":
        print(f"\033[39m┌─\033[96m[\033[31mz3ntl3\033[96mroot\033[33m@\033[36mEfdal\033[96m]\033[31m─\033[36m[\033[32m/\033[96mr00t\033[32m/\033[39mLicense-SYSTEM\033[32m/\033[31m\033[36m]\033[36m\n\033[39m└──\033[31m╼\033[31m╼ \033[33m$\033[36mLICENSE: {licensiesystem}")
        break
    else:
        print(f"\033[39m┌─\033[96m[\033[31mz3ntl3\033[96mroot\033[33m@\033[36mEfdal\033[96m]\033[31m─\033[36m[\033[32m/\033[96mr00t\033[32m/\033[39mInvalid-LICENSE\033[32m/\033[31m\033[36m]\033[36m\n\033[39m└──\033[31m╼\033[31m╼ \033[33m$\033[36mLICENSE: {licensiesystem}")
        sys.exit()


options = f"""
\033[31m[\033[96mOPTIONS\033[31m]\033[0m

\033[31m>>> \033[39m darkness \033[36m Opens the main software \033[31m[\033[96mdarkness\033[31m]\033[0m
\033[31m>>> \033[39m exit \033[36m Exits the software \033[31m[\033[96mexit\033[31m]\033[0m

"""
print(options)
kies = input(indicatorlogo)


while True:
  if kies == "darkness":
    os.system('chmod +x darkness.py')
    os.system('python3 darkness.py')
    sys.exit()
  else:
    os.system('chmod +x menu.py')
    os.system('python3 menu.py')
