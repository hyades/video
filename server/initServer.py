import socket
import sys


from constants import *

#--------------------
port = 4500
#--------------------

def start():
    for x in ip:
        try:    
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                server_address = (x, port) #CAM1 IP ADDRESS
                print 'connecting to %s port %s' % server_address
                sock.connect(server_address)
                try:
                    sock.sendall("$start")
                finally:
                    sock.close()
        except:
            print "ERROR OCCURRED"

start()