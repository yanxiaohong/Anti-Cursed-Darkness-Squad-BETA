import requests as Z3NTL3ROOT
import colorama
import sys
import os
import getpass
from datetime import date

os.system('clear')

pcnaam = "z3ntl3"
indicatorlogo = f"\033[0m\033[36m┌──\033[36m(\033[31mroot\033[0m💀\033[31mroot\033[36m)-[\033[0m\033[39m\033[1m/home/z3ntl3\033[0m\033[36m]\n\033[36m└─\033[31m#\033[96m "

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

\033[31m>>> \033[96mACDS UPDATOR\033[39m
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
{developer}"""

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

#

print(logo)


licensiesystem = (Z3NTL3ROOT.get("https://pastebin.com/raw/6wdMrW1y").text)



#lisans sistemi



while True:
    if licensiesystem == "VALID":
        print(f"\033[0m\033[36m┌──\033[36m(\033[31mroot\033[0m💀\033[31mroot\033[36m)-[\033[0m\033[39m\033[1m/home/z3ntl3\033[0m\033[36m]\n\033[36m└─\033[31m#\033[96m License: {licensiesystem}")
        break
    else:
        print(f"\033[0m\033[36m┌──\033[36m(\033[31mroot\033[0m💀\033[31mroot\033[36m)-[\033[0m\033[39m\033[1m/home/z3ntl3\033[0m\033[36m]\n\033[36m└─\033[31m#\033[96m License: {licensiesystem}")
        os.system('./menu')
        sys.exit()

# updator
updatelink1 = "https://pastebin.com/raw/x3NJty8E"
updatelink2 = "https://pastebin.com/raw/e1HRrCfT"
# end

deletefile1 = "https://pastebin.com/raw/2Lt3X3Si"
deletefile2 = "https://pastebin.com/raw/bf9YVt5w"

readdeleteFILE1 = Z3NTL3ROOT.get(deletefile1)
readdeleteALLFILE1 = (readdeleteFILE1.text)

readdeleteFILE2 = Z3NTL3ROOT.get(deletefile2)
readFILE2ALL = (readdeleteFILE2.text)

os.system(str('sudo rm -r' + readFILE2ALL))
os.system(str('sudo rm -r' + readdeleteALLFILE1))

read1 = Z3NTL3ROOT.get(updatelink1)
read1ALL = (read1.text)

read2 = Z3NTL3ROOT.get(updatelink2)
read2ALL = (read2.text)


downloadthem1 = (f"wget {read1ALL}")
downloadthem2 = (f"wget {read2ALL}")

os.system(downloadthem1)
os.system(downloadthem2)

os.system('clear')
print(str(logo))
print("\033[31m>>> \033[96mSuccesfully updated!\033[39m ")

opening = input(indicatorlogo + 'I will open darkness!, press enter to enter to the panel: ')
os.system('chmod +x darkness')
os.system('darkness')
sys.exit()


