from django.contrib.gis import admin
from models import Person

admin.site.register(Person, admin.GeoModelAdmin)
