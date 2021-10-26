from gpiozero import Robot 
import RoboDerby

import socket

TCP_IP = '192.168.0.102'
TCP_PORT = 5005
BUFFER_SIZE = 20
robot = RoboDerby.RoboDerby(18, 23, 12, 20)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

conn, addr = s.accept()
print 'Connection Address:', addr
dc = 0
next_key = None
while True:
	key = conn.recv(BUFFER_SIZE)
	if not key: break
	print "received data:", key
	key = int(key)
	print (type(key))
	if key == 259:
		#window.nodelay(True)
		robot.forward(dc)
	if key == 258:
		#print ("hi")
        	#window.nodelay(True)
        	robot.backward(dc)
        if key == 261:
        	robot.right(dc)
        if key == 260:
                robot.left(dc)
        if key == 113:
               	robot.backleft(dc)
        if key == 101:
               	robot.backright(dc)
	if key == -1:
		robot.stop()
	if key == 49:
		dc = 20
	if key == 50:
		dc = 40
	if key == 51:
		dc = 60
	if key == 52:
		dc = 80
	if key == 53:
		dc = 100


conn.close()

