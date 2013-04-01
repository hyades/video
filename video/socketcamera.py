import socket
import sys
from camera import *
from camera2 import *
import os,signal,sys


sock1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = 'localhost'
port = 4500
server_address1 = (ip,port)
print "STARTING SERVER ON CAMERA:"+ str(server_address1)
sock1.bind(server_address1)
sock1.listen(1)


while 1:
    print "WAITING FOR CONNECTION"
    connection1,client_address1 = sock1.accept()
    try:
        print "connection from",client_address1

        while 1:
            data = connection1.recv(20)
            print "RECIEVED %s" %data
            data = data.split()
            if data[0] == "$start":
                p = camera()
                print "STARTING"
                #gtk.main()
            elif data[0] == "$stop":
                #start.pause()
                try:
                    #print p.pid
                    os.kill(p.pid+1,signal.SIGTERM)
                    #p.kill()
                    print "PROCESS ENDED"
                except:
                    print >>sys.stderr,  "ERROR OCCURRED WHILE KILLING PROCESS"
                
            else:
                print >>sys.stderr,  "UNRECOGNISED DATA",client_address1
                connection1.close()
    except:
        print "CLOSING CONNECTION"
        connection1.close()