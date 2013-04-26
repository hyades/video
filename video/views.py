import socket
import sys
from django.shortcuts import render_to_response,redirect
from settings import ip
#from django.core.context_processors import request


#------------------------------
port = 4500
#don't change port

#------------------------------

def video(request):
    page = 'index.html'
    variables = {}
    return render_to_response(page,variables)



    
def cam1(request):
    #Repete for other cameras

    n = 1

    page = 'cam.html'
    variables = {'number':n,'ip':ip[n-1]}
    return render_to_response(page,variables)
