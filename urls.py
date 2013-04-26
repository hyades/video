from django.conf.urls import patterns,url
from video.views import *   
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    

    url(r'^video/', video),
    url(r'^cam1/', cam1),
    #url(r'^cam2/', cam2),

    #add for extra cameras

    
)
