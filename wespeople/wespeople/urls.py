from django.conf.urls import patterns, include, url
from django.contrib.gis import admin
from django.conf.urls.defaults import *
from django.conf.urls.static import static
from tastypie.api import Api
from maps.api import PersonResource
from maps.views import register
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
    (r'^accounts/login/$', login,
            {'template_name':'login.html'}),
    (r'^accounts/login/$', login),
    (r'^accounts/logout/$', logout,
          {'next_page': '/'}),
    (r'^accounts/register/$', register),
    (r'^$', 'maps.views.index'),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static-admin/media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.ADMIN_MEDIA_ROOT, 'show_indexes': True}),
    )
