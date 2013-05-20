from tastypie.contrib.gis.resources import ModelResource
from maps.models import Person
from tastypie.resources import ALL, ALL_WITH_RELATIONS
from tastypie.authorization import Authorization, ReadOnlyAuthorization
from tastypie.cache import SimpleCache

class PersonResource(ModelResource):
  class Meta:
    queryset = Person.geolocated.all()
    resource_name = 'geoperson'

    exclude = ['preferred_email']
    #fields = ['name', 'location', 'preferred_class_year']
    filtering = {
      'preferred_class_year': ('exact', 'gte', "range"),
      'state': ('exact', 'startswith'),
      'city': ('exact', 'startswith'),
      'wesleyan_degree_1_major_1': ('exact', 'startswith'),
      'wesleyan_degree_1_major_2': ('exact', 'startswith'),
      'wesleyan_degree_1_major_3': ('exact', 'startswith'),
      'location': ALL_WITH_RELATIONS,
      'pk': ('exact', 'gte', "range"),
    }

    limit = 348
    cache =  SimpleCache(timeout=60)
