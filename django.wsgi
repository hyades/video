import os, sys  
  
  
sys.path.append("/home/hyades/Github/video")
sys.path.append("/home/hyades/Github/video/video")


   
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
  

import django.core.handlers.wsgi  


application = django.core.handlers.wsgi.WSGIHandler()
