import httpx
import sys,subprocess
from concurrent.futures import Future
from concurrent.futures import as_completed
from concurrent.futures import ThreadPoolExecutor
import auth.twofactorAUTH
import time
import os
import platform, json

'''
An improved version of the old ACDS. 

What it does is safely overload your CPU and run several priv/pub scripts simultaneously on your server. 

Please use a spoof for the best experience.
'''

SECRET = auth.twofactorAUTH.SECRETKEY_AT_LOAD

def Validate(inputCode):
   val = auth.twofactorAUTH.PinAuthorization(inputCode, SECRET).Validate()
   return val

LOGO = """ 
      \033[38;5;129m╔═╗╔╗╔╔╦╗╦   ╔═╗╦ ╦╦═╗╔═╗╔═╗╔╦╗\033[0m       
      \033[38;5;128m╠═╣║║║ ║ ║───║  ║ ║╠╦╝╚═╗║╣  ║║\033[0m       
      \033[38;5;127m╩ ╩╝╚╝ ╩ ╩   ╚═╝╚═╝╩╚═╚═╝╚═╝═╩╝\033[0m       
  \033[38;5;126m╔╦╗╔═╗╦═╗╦╔═╔╗╔╔═╗╔═╗╔═╗  ╔═╗╔═╗ ╦ ╦╔═╗╔╦╗\033[0m
   \033[38;5;125m║║╠═╣╠╦╝╠╩╗║║║║╣ ╚═╗╚═╗  ╚═╗║═╬╗║ ║╠═╣ ║║\033[0m
  \033[38;5;124m═╩╝╩ ╩╩╚═╩ ╩╝╚╝╚═╝╚═╝╚═╝  ╚═╝╚═╝╚╚═╝╩ ╩═╩╝\033[0m"""

def BeginScreen():
    logoLineByLine = LOGO.split('\n')

    for line in logoLineByLine:
        sys.stdout.flush()
        sys.stdout.write(line+'\n')
        time.sleep(0.1)

    sys.stdout.flush()
    CheckOS()

    CONTINUEtxt = f"""\n        \033[38;5;129m╔══════════\033[38;5;128m════\033[38;5;127m══════\033[38;5;128m═══════\033[38;5;129m══╗\033[0m
        \033[38;5;128m║   \033[38;5;124mPRESS  \033[38;5;126mENTER \033[38;5;124mTO CONTINUE  \033[38;5;128m║\033[0m
        \033[38;5;128m╚═\033[38;5;129m═════\033[38;5;128m════════\033[38;5;129m══════════\033[38;5;128m═════\033[38;5;127m╝\033[0m"""
    for cont in CONTINUEtxt.split('\n'):
        sys.stdout.flush()
        sys.stdout.write(cont+'\n')
        time.sleep(0.2)

    sys.stdout.write('\r\n\n')
    try:
        inputWaitable = input(f"\033[38;5;128m$\033[38;5;127m-\033[38;5;128m[\033[38;5;127m{os.getcwd()}\033[38;5;128m]\033[38;5;127m--\033[38;5;129m> \033[38;5;124m")
    except KeyboardInterrupt:
        sys.exit('\n\033[31mSoftware Exited\033[0m')
    sys.stdout.write('\033[0m')

    if inputWaitable:
        return

def Clear():
    PIPE = subprocess.PIPE
    cmd = subprocess.run('clear', shell=True, stderr=PIPE)
    if cmd.stderr != None:
        subprocess.run('cls',shell=True, stderr=subprocess.DEVNULL)

def CheckOS():
    OS = platform.system()

    if 'linux' in OS.lower():
        return
    else:
        sys.exit('\033[31mPlatform Unsupported: You require a linux OS.\033[0m\n')

class Tools:
    def SpeedTest():
        command = 'speedtest'
        execCmd = subprocess.run(command, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)

        if execCmd:
            upload = execCmd.stdout.decode('utf-8').split('\n')[4]
            download =  execCmd.stdout.decode('utf-8').split('\n')[6]

        return [ [upload] , [download] ]

    def LimitFixer():
        slash = "\\"
        
        with open("config.json","r") as fileread:
            content = fileread.read().decode('utf-8')
        
        filename = json.loads(content)
        command = f"bash {os.getcwd() + slash}{filename['filename_limiter']}"

class HubScripts:
    pass

if __name__ == '__main__':
    Clear()
    BeginScreen()