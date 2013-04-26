#!/usr/bin/env python
import socket
import sys

from ipconfig import ip

#--------------------
port = 4500
#--------------------



def stop():
	for x in ip:
		try:
			sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			server_address = (x, port) #CAM1 IP ADDRESS
			print 'connecting to %s port %s' % server_address
			sock.connect(server_address)
			try:
			    sock.sendall("$stop")
			except:
			    print "ERROR OCCURRED WHILE SENDING STOP SIGNAL TO" , x
			sock.close()
		except:
			print "ERROR OCCURRED"

stop()