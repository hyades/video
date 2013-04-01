import socket
import sys
input  = raw_input() #get input from background C program instead

try:    
    sock2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ip='localhost'
    port=4501
    server_address2 = (ip,port) #SERVER IP ADDRESS
    print 'connecting to %s port %s' % server_address2
    sock2.connect(server_address2)
    data = input.split()[0]
    try:
        sock2.sendall(data)
    finally:
        sock2.close()
except:
    print >>sys.stderr,  "ERROR OCCURRED WHILE SENDING TO SERVER."