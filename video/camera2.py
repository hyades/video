import subprocess

def camera():
    command = "gst-launch v4l2src ! videorate  ! video/x-raw-yuv, width=320, height=240  ! theoraenc drop-frames=false ! oggmux ! queue !  tcpserversink port=5000"
    p = subprocess.Popen(command, stdout=subprocess.PIPE, bufsize=-1, shell=True)
    #print p.pid
    return p

    
    