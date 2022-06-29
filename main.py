import httpx
import sys,subprocess
from concurrent.futures import Future
from concurrent.futures import as_completed
from concurrent.futures import ThreadPoolExecutor
import auth.twofactorAUTH
import time
import os
import platform, json
import socket
import rsa 
from datetime import date
import threading
import keyboard

'''
An improved version of the old ACDS. 

What it does is safely overload your CPU and run several priv/pub scripts simultaneously on your server. 

Please use a spoof for the best experience.
'''

public, private = rsa.newkeys(612)

HOSTNAME = socket.gethostname()
IP = rsa.encrypt(socket.gethostbyname(HOSTNAME).encode('utf-8'),public)
SECRET = auth.twofactorAUTH.SECRETKEY_AT_LOAD
CURSOR = f"\n\033[38;5;129m╔\033[38;5;128m═\033[38;5;123m[\033[38;5;125m{os.getcwd()}\033[38;5;123m]\033[38;5;128m-\033[38;5;123m[\033[38;5;127m{socket.gethostname()}\033[38;5;123m]\n\033[38;5;129m╚══\033[38;5;128m══\033[38;5;124m➤ \033[38;5;123m"

class AvailableMethods:
    # The only method I (aka Z3NTL3) have developed is in `my_l4` folder and is called z3slam in the panel.
    Layer4 = ['z3slam'] # This is
    Layer7 = ['ultra-bypass','http-nuke','http-get','http-post'] # These methods arent mine
    Tools = ['speedtest']

class Encryption():
    # Always encrypt logs, logs can only be viewed from 'log_viewer.py'
    def __init__(self,obj):
        self.obj = obj
    def Encrypt(self):
        encrypted_content = rsa.encrypt(self.obj.encode('utf-8'), public)
        return encrypted_content
    def Decrypt(self):
        decrypted_content = rsa.decrypt(self.obj.encode('utf-8'),private)
        return decrypted_content
class Logger:
    def AddLog(msg):
        msg = f"{CurrentDate()} {msg}\n"
        with open("logs\log.txt","a+")as file:
            content = Encryption(msg).Encrypt()
            file.write(content)
        return
def CurrentDate():
    today = date.today()
    d1 = today.strftime("%d/%m/%Y %H:%M:%S")
    return d1

def Validate(inputCode):
   val = auth.twofactorAUTH.PinAuthorization(inputCode, rsa.decrypt(SECRET,auth.twofactorAUTH.priv).decode()).Validate()
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

def Error(msg):
    sys.stdout.flush()
    sys.stdout.write(f"\n\033[31m[ \033[0mError \033[31m]\033[0m: \033[31m{msg}\033[0m\n")

def PentestHub():
    hubMenu = """ 
      \033[38;5;129m╔═══════════════\033[38;5;127m═════════════\033[38;5;124m➤
      \033[38;5;129m║ \033[38;5;123mOptions\033[38;5;124m:
      \033[38;5;129m║      \033[38;5;124m1 \033[38;5;124m- \033[38;5;123mlayer7
      \033[38;5;129m║      \033[38;5;124m2 \033[38;5;124m- \033[38;5;123mlayer4 
      \033[38;5;129m║      \033[38;5;124m3 \033[38;5;124m- \033[38;5;123mtools
      \033[38;5;129m╚═══\033[38;5;127m══════════\033[38;5;124m➤"""
    hub = LOGO +'\n'+ hubMenu
    
    sys.stdout.flush()
    sys.stdout.write(hub)
    sys.stdout.write('\n'*2)
    
    hubLoop = True
    
    while hubLoop:
        try:
            th = ThreadPoolExecutor()
            option = input(CURSOR).lower()
            argv = option.split(' ')

            if argv.__len__() == 1:
                if option == "exit" or option == "close":
                    sys.exit('\033[31mExited ACDS.\033[0m\n')
                elif option == "clear" or option == "clear" or option == "clear":
                    Clear()
                    time.sleep(0.2)
                    sys.stdout.flush()
                    sys.stdout.write(hub)
                elif option == "1" or option == "layer7":
                    part1 = """\033[38;5;129m╔═══\033[38;5;128m══════\033[38;5;127m══════\033[38;5;124m➤"""
                    part2 = """\033[38;5;129m║ \033[38;5;123mL7 Methods\033[38;5;129m:"""
                    part3 = "\033[38;5;129m║"
                    partend = "\033[38;5;129m╚═════\033[38;5;128m═════\033[38;5;127m═════\033[38;5;124m➤\033[0m"

                    stdoutbuilder = ""
                    stdoutbuilder+= part1+'\n'+part2+'\n'
                    for method in AvailableMethods.Layer7:
                        stdoutbuilder+= part3 + ' ' + method + '\n' 
                    stdoutbuilder+= partend
                    time.sleep(0.2)
                    sys.stdout.flush()
                    sys.stdout.write(stdoutbuilder)
                elif option == "3" or option == "tools":
                    part1 = """\033[38;5;129m╔═══\033[38;5;128m══════\033[38;5;127m══════\033[38;5;124m➤"""
                    part2 = """\033[38;5;129m║ \033[38;5;123mTools\033[38;5;129m:"""
                    part3 = "\033[38;5;129m║"
                    partend = "\033[38;5;129m╚═════\033[38;5;128m═════\033[38;5;127m═════\033[38;5;124m➤\033[0m"

                    stdoutbuilder = ""
                    stdoutbuilder+= part1+'\n'+part2+'\n'
                    for tools in AvailableMethods.Tools:
                        stdoutbuilder+= part3 + ' ' + tools + '\n' 
                    stdoutbuilder+= partend
                    time.sleep(0.2)
                    sys.stdout.flush()
                    sys.stdout.write(stdoutbuilder)
                elif option == "speedtest":
                    sys.stdout.write("\033[38;5;129m[ \033[38;5;123mINFO \033[38;5;129m] \033[38;5;123mThis could take a little while, will send the results after some seconds.\n")
                    ftr = th.submit(Tools.GetSpeed)
                    while ftr.running():
                        continue
                    if ftr.done():
                        th.shutdown()
                        
                else:
                    Error("Command not found")
            elif argv.__len__() == 3:
                
                pass
            elif argv.__len__() == 4:
                pass
            else:
                Error("Command not found")
        except RuntimeError:
            pass
        except KeyboardInterrupt:
            sys.exit('\033[31mExited ACDS\033[0m')

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
            upload = execCmd.stdout.decode('utf-8').split('\n')[6]
            download =  execCmd.stdout.decode('utf-8').split('\n')[8]

        return [ [upload] , [download] ]
    def GetSpeed():
        speed = Tools.SpeedTest()
        upload = speed[0][0]
        download = speed[1][0]

        part1 = """\n\033[38;5;129m╔═══\033[38;5;128m══════\033[38;5;127m══════\033[38;5;124m➤"""
        part2 = """\033[38;5;129m║ \033[38;5;123mSpeedTest\033[38;5;129m:"""
        part3 = "\033[38;5;129m║"
        partend = "\033[38;5;129m╚═════\033[38;5;128m═════\033[38;5;127m═════\033[38;5;124m➤\033[0m"

        stdoutbuilder = ""
        stdoutbuilder+= part1+'\n'+part2+'\n'
        stdoutbuilder+= part3 + ' ' + upload + '\n' 
        stdoutbuilder+= part3 + ' ' + download + '\n' 
        stdoutbuilder+= partend
        time.sleep(0.2)
        sys.stdout.flush()
        sys.stdout.write(stdoutbuilder)
        keyboard.press_and_release('enter')
        sys.stdout.flush()

    def LimitFixer():
        slash = "\\"
        
        with open("config.json","r") as fileread:
            content = fileread.read().decode('utf-8')
        
        filename = json.loads(content)
        command = f"bash {os.getcwd() + slash}{filename['filename_limiter']}"
        result = subprocess.run(command,shell=True,stderr=subprocess.PIPE,stdout=subprocess.PIPE)
        stdout,stderr = (result.stdout, result.stderr)

        return [stdout,stderr]

class HubScripts:
    pass

if __name__ == '__main__':
    # Clear()
    # BeginScreen()
    # PentestHub()
    pass
