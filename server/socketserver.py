import socket
import sys
from server import *
import os,signal
import subprocess
from datetime import datetime

sock1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = 'localhost'
port = 4501
server_address1 = (ip,port)
print "STARTING SERVER ON SERVER: "+ str(server_address1)
sock1.bind(server_address1)
sock1.listen(1)



class Server():
    def __init__(self):
        host='localhost'
        port='5000'
        name = "activity_" + str(datetime.now().day) + "_" + str(datetime.now().month) + "_" + str(datetime.now().day) + "_" + str(datetime.now().hour) + "_" + str(datetime.now().minute) + "_" + str(datetime.now().second)
        #f = open(name,"w")
        #f.close()
        
        self.command = """gst-launch  tcpclientsrc host=%s port=%s ! filesink location='/home/hyades/videologs/%s'"""  %(host , port ,name)
        print("running command: %s" % (self.command, ))
        
        self.p = subprocess.Popen(self.command, stdout=subprocess.PIPE, bufsize=-1, shell=True)
    def kill(self):
        try:
            self.p.kill()
            print "PROCESS EXCITED"
        except:
            res = os.kill(int(self.p.pid)+1,signal.SIGKILL)
            if res:
                print "PROCESS EXCITED"
            else:
                print "ERROR OCCURRED IN STOPPING PID:",self.p.pid



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