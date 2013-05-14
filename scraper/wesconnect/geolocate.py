"""
Geolocate the alum data
"""

import csv
from collections import Counter
import simplejson, urllib
import pickle
import time

pickle_file = "addresses.pickle"
f = open(pickle_file, "rb")

addresses = pickle.load(f)

print "Adddresses currently has %s entries" % len(addresses)

def clean(s):
  return s.strip().replace("\xc2\xa0", "")

GEOCODE_BASE_URL = 'http://maps.googleapis.com/maps/api/geocode/json'

def geocode(address, sensor="false", **geo_args):
    geo_args.update({
        'address': address,
        'sensor': sensor
    })

    url = GEOCODE_BASE_URL + '?' + urllib.urlencode(geo_args)
    result = simplejson.load(urllib.urlopen(url))
    print simplejson.dumps([s['formatted_address'] for s in result['results']], indent=2)
    return result

locations = {}
address_counter = Counter()
with open('alums50-13.csv') as csvfile:
  alumreader = csv.reader(csvfile, delimiter=",")
  for row in alumreader:
    city = clean(row[15])
    country = clean(row[18])
    state = clean(row[22])

    address = ""

    if city:
      address += city
    if state:
      if address:
        address += (", " + state)
      else:
        address += state
    if country:
      if address:
        address += (", " + country)
      else:
        address += country

    address = address.replace(" ", "+")
    address_counter[address] += 1


geocode_count = 1710
for address in address_counter.most_common(geocode_count):
  if address[0] not in addresses:
    result = geocode(address[0])
    if result['status'] == "OK":
      addresses[address] = result
      time.sleep(.3)
    elif result['status'] == "ZERO_RESULTS":
      continue
    else:
      print "encountered error"
      print result
      break

with open(pickle_file, "wb") as picklefile:
  pickle.dump(addresses, picklefile)

f.close()
