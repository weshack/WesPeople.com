from django.conf.urls import patterns, include, url
from django.contrib.gis import admin
from django.conf.urls.defaults import *
from tastypie.api import Api
from maps.api import PersonResource
from maps.models import Person
from django.conf import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
admin.autodiscover()

people = PersonResource()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'wespeople.views.home', name='home'),
    # url(r'^wespeople/', include('wespeople.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    (r'^index/$', 'maps.views.map_test'),
    (r'^map/$', 'maps.views.map_test'),
    url(r'^api/', include(people.urls)),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
                {'document_root': settings.MEDIA_ROOT}),
    # (r'^admin/(?P<path>.*)$', 'django.views.static.serve',
    #             {'document_root': settings.ADMIN_MEDIA_PREFIX}),
)
