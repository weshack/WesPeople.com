from django.conf.urls import patterns, include, url
from django.contrib.gis import admin
from tastypie.api import Api
from maps.api import PersonResource

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
    (r'^index/$', 'map.views.map_test'),
    url(r'^api/', include(people.urls)),
)
