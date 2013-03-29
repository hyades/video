import socket
import sys
from django.shortcuts import render_to_response
#from django.core.context_processors import request

def video(request):
    page = 'index.html'
    variables = {}
    return render_to_response(page,variables)
    
def cam1(request):
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
    
    page = 'cam.html'
    n = 1
    variables = {'number':n}
    return render_to_response(page,variables)

def init(request):
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
    page = 'index.html'
    variables = {}
    return render_to_response(page,variables)
def end1(request):  
    #STOP
    try:
        
            
        sock2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_address2 = ('localhost', 4500) #CAM1 IP ADDRESS
        print 'connecting to %s port %s' % server_address2
        sock2.connect(server_address2)
        try:
            sock2.sendall("$stop")
        finally:
            sock2.close()
    except:
        print "ERROR OCCURRED"
    page = 'index.html'
    variables = {}
    return render_to_response(page,variables)
    

def cam2(request):
    page = 'cam.html'
    n = 2
    variables = {'number':n}
    return render_to_response(page,variables)

def end2(request):  
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
    page = 'index.html'
    variables = {}
    return render_to_response(page,variables)
    