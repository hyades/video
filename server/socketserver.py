import socket
import sys
from server import *
import os,signal
sock1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = 'localhost'
port = 4501
server_address1 = (ip,port)
print "STARTING SERVER ON SERVER: "+ str(server_address1)
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
            #print data[0:5], data[0:4]
            if data[0:6] == "$start":
                server = Server()
                print "-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n" + "-=-=-=-=-STARING RECORDING-=-=-=-=-=-\n" + "-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-="
                #gtk.main()
            elif data[0:5] == "$stop":
                #start.pause()
                print "-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n" + "-=-=-=-=-STOPING RECORDING-=-=-=-=-=-\n" + "-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-="
                server.kill()                
            else:
                print >>sys.stderr,  "UNRECOGNISED DATA",client_address1
                connection1.close()
    except:
        print "CLOSING CONNECTION"
        connection1.close()