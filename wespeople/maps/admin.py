from django.contrib.gis import admin
from models import Person

class PersonAdmin(admin.GeoModelAdmin):
  #fieldsets = (
  #  (None, {
  #    'fields': (('last_name', 'first_name', 'nickname'),
  #      'wesleyan_degree_school_1',
  #      ('city', 'state', 'country'),
  #      'preferred_email',
  #      'page_url',
  #      'occupation',
  #      'industry',
  #      'company_name',
  #      'position_title',
  #      'position_status',
  #      'business_address_1',
  #      'business_address_2',
  #      'location',
  #    )
  #  }),
  #)
  pass

admin.site.register(Person, PersonAdmin)
