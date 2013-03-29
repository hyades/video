import socket
import sys

#FOR CAM1 repete for other cameras
#START
try:
    sock2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address2 = ('localhost', 4500) #CAM1 IP ADDRESS
    print 'connecting to %s port %s' % server_address2
    sock2.connect(server_address2)
    try:
        sock2.sendall("$start")
    finally:
        sock2.close()
except:
    print "ERROR OCCURRED"

#STOP
try:
    
        
    sock2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address2 = ('localhost', 4500) #CAM1 IP ADDRESS
    print 'connecting to %s port %s' % server_address2
    sock2.connect(server_address2)
    try:
        sock2.sendall("$start")
    finally:
        sock2.close()
except:
    print "ERROR OCCURRED"

    