from wespeople import settings
from django.core.management import setup_environ
setup_environ(settings)
import simplejson
import pickle
from django.contrib.gis.geos.point import Point

count = 0

from maps.models import Person

pickle_file = "addresses.pickle"
f = open(pickle_file, "rb")

addresses = pickle.load(f)

def clean(s):
  return s.strip().replace("\xc2\xa0", "")

for p in Person.objects.all():
  address = ""

  if p.city:
    address += p.city
  if p.state:
    if address:
      address += (", " + p.state)
    else:
      address += p.state
  if p.country:
    if address:
      address += (", " + p.country)
    else:
      address += p.country

  address = address.replace(" ", "+")

  if address in addresses:
    print address
    print addresses[address]
    lat = addresses[address]['results'][0]['geometry']['location']['lat']
    lng = addresses[address]['results'][0]['geometry']['location']['lng']
    p.location = Point(lng, lat)
    p.save()
    count += 1

print "done %s" % count

