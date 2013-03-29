import os, sys  
  
  
sys.path.append("/home/hyades/Documents/Aptana Studio 3 Workspace/video")
sys.path.append("/home/hyades/Documents/Aptana Studio 3 Workspace/video/video")


   
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
  

import django.core.handlers.wsgi  


application = django.core.handlers.wsgi.WSGIHandler()
