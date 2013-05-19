from wespeople import settings
from django.core.management import setup_environ
setup_environ(settings)
import simplejson
import pickle
from django.contrib.gis.geos.point import Point

count = 0

from maps.models import Person

for p in Person.objects.all():
    # Not sure how to exactly filter out weird names.
    if p.name:
        print p.name, " : "+p.first_name
        print "first: ", p.name.split()[0]
        print "last: ", p.name.split()[2]