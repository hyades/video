#!/usr/bin/python

import subprocess

#gst-launch tcpclientsrc port=5001 ! multipartdemux ! multipartmux ! tcpserversink port=5000




command = "gst-launch tcpclientsrc port=5001 ! multipartdemux ! multipartmux ! tcpserversink port=5000"
print("running command: %s" % (command, ))

p = subprocess.Popen(command, stdout=subprocess.PIPE, bufsize=-1, shell=True)
