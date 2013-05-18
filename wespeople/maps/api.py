from tastypie.contrib.gis.resources import ModelResource
from maps.models import Person
from tastypie.resources import ALL, ALL_WITH_RELATIONS
from tastypie.authorization import Authorization

class GeoPerson(ModelResource):
  class Meta:
    queryset = Person.objects.all()
    resource_name = 'geoperson'

    #filtering = {
    #    'polys': ALL,
    #    }
