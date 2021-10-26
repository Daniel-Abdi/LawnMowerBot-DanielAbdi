import socket
import curses
from gpiozero import Robot
TCP_IP = '192.168.0.102'
TCP_PORT = 5005
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

def main(window):
    window.nodelay(True)
    key = ""
    while True:

        key = window.getch()
        val = str.encode(str(key))
        curses.halfdelay(3)
        print(val)
        s.send(val)



curses.wrapper(main)
s.close()