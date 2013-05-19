from django.conf.urls import patterns, include, url
from django.contrib.gis import admin
from django.conf.urls.defaults import *
from tastypie.api import Api
from maps.api import PersonResource
from maps.views import *
from maps.models import Person
from django.conf import settings
from django.contrib.auth.views import login, logout

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
    (r'^filter/$', 'maps.views.search'),
    url(r'^api/', include(people.urls)),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
                {'document_root': settings.MEDIA_ROOT}),
    (r'^accounts/login/$', login),
    (r'^accounts/logout/$', logout,
            {'next_page': '/accounts/login'}),
    (r'^accounts/register/$', register),
    (r'^$', 'maps.views.index'),
    (r'^(?P<from_year>\d{4})-(?P<to_year>\d{4})$', 'maps.views.filter_year'),
    (r'^(?P<from_year>\d{4})', 'maps.views.filter_year'),
)
