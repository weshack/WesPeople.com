from tastypie.contrib.gis.resources import ModelResource
from maps.models import Person
from tastypie.resources import ALL, ALL_WITH_RELATIONS
from tastypie.authorization import Authorization, ReadOnlyAuthorization

class PersonResource(ModelResource):
  class Meta:
    queryset = Person.geolocated.all()
    resource_name = 'geoperson'

    #fields = ['name', 'location', 'preferred_class_year']
    filtering = {
      'preferred_class_year': 'exact',
    }

    limit = 0
    #list_allowed_methods = ['get', 'post']
    #authorization = ReadOnlyAuthorization

    #def get_object_list(self, request):
    #  return super(PersonResource, self).get_object_list(request).filter(location__isnull=False)

    #filtering = {
    #    'first_name': ALL,
    #    }
