import socket
import sys
from camera import *
sock1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address1 = ('localhost',4500)
print "STARTING SERVER ON "+ str(server_address1)
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
                start = Main()
                print "STARTING"
                #gtk.main()
            elif data[0] == "$stop":
                start.pause()
                print "ENDING"
                
            else:
                print "UNRECOGNISED DATA",client_address1
                connection1.close()
    except:
        print "CLOSING CONNECTION"
        connection1.close()