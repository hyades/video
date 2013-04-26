import socket
import sys


from constants import *

#--------------------
port = 4500
#--------------------



def stop():
	for x in ip:
		try:
	    	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	        server_address = (ip,port) #CAM1 IP ADDRESS
	        print 'connecting to %s port %s' % server_address
	        sock2.connect(server_address)
	        try:
	            sock.sendall("$stop")
	        finally:
	            sock.close()
    	except:
        	print "ERROR OCCURRED"