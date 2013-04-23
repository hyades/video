#!/usr/bin/python

import subprocess
from datetime import datetime
import os,signal



class Server():
    def __init__(self):
        host='localhost'
        port='5000'
        name = "activity_" + str(datetime.now().day) + "_" + str(datetime.now().month) + "_" + str(datetime.now().day) + "_" + str(datetime.now().hour) + "_" + str(datetime.now().minute) + "_" + str(datetime.now().second)
        f = open(name,"w")
        f.close()
        
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