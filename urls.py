from django.conf.urls import patterns,url
from video.views import *   
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'video.views.home', name='home'),
    url(r'^video/', video),
    url(r'^cam1/', cam1),
    url(r'^cam2/', cam2),
    url(r'^init/', init),
    url(r'^end1/', end1),
    url(r'^end2/', end2),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
