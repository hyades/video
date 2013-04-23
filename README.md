video
=====
README


DEPENDENCIES



Camera

1. Gstreamer gst-launch
2. v4l2


Server

1. Django-1.4
2. libapache2-mod-wsgi for django deployment



Client

1. Web brwoser compatible with HTML 5.
2. VLC Media Player


INSTALLATION

1. Configure Django on server machine.
2. Copy the camera folder to the camera machine.
3. On the camera, compile the files camera.c and camera-rec-socket.c and run their executables
4. To simulate recording, run the executable of camera-rec-socket.c with arguments 
  	0 = start recording
		1 = stop recording
5. Execute socketserver.py on the server.
