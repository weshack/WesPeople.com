from tastypie.contrib.gis.resources import ModelResource
from maps.models import Person
from tastypie.resources import ALL, ALL_WITH_RELATIONS
from tastypie.authorization import Authorization, ReadOnlyAuthorization

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
    }

    limit = 1000
    #list_allowed_methods = ['get', 'post']
    #authorization = ReadOnlyAuthorization

    #def get_object_list(self, request):
    #  return super(PersonResource, self).get_object_list(request).filter(location__isnull=False)

    #filtering = {
    #    'first_name': ALL,
    #    }
