from django.contrib.auth.models import User
from django.contrib.gis.db import models
from django.utils.translation import ugettext as _
from userena.models import UserenaBaseProfile
from django.contrib.sites.models import Site

class PersonLocationManager(models.GeoManager):
  def get_query_set(self):
    return super(PersonLocationManager,
        self).get_query_set().filter(location__isnull=False).exclude(first_name='').exclude(last_name='')

class PersonNameManager(models.GeoManager):
  def get_query_set(self):
    return super(PersonNameManager, self).get_query_set().filter(name='')

# Create your models here.
class Person(UserenaBaseProfile):
  # define the fields for your item here like:
  name = models.CharField(max_length=100, null=True, blank=True)
  mid = models.CharField(max_length=100, null=True, blank=True)
  page_url = models.URLField(null=True, blank=True)
  preferred_email = models.EmailField(null=True, blank=True)
  company_name = models.CharField(max_length=100, null=True, blank=True)
  city = models.CharField(max_length=100, null=True, blank=True)
  state = models.CharField(max_length=100, null=True, blank=True)
  country = models.CharField(max_length=100, null=True, blank=True)

  #wesleyan education
  wesleyan_degree_school_1 = models.CharField(max_length=100, null=True, blank=True)
  wesleyan_degree_year_1 = models.CharField(max_length=100, null=True, blank=True)
  wesleyan_degree_1 = models.CharField(max_length=100, null=True, blank=True)
  wesleyan_degree_1_major_1 = models.CharField(max_length=100, null=True, blank=True)
  wesleyan_degree_1_major_2 = models.CharField(max_length=100, null=True, blank=True)
  wesleyan_degree_1_major_3 = models.CharField(max_length=100, null=True)

  # member information
  first_name = models.CharField(max_length=100, null=True, blank=True)
  last_name = models.CharField(max_length=100, null=True, blank=True)
  nickname = models.CharField(max_length=100, null=True, blank=True)
  last_name_at_grad = models.CharField(max_length=100, null=True, blank=True)
  preferred_class_year = models.CharField(max_length=100, null=True, blank=True)
  preferred_email = models.CharField(max_length=100, null=True, blank=True)

  #primary employment
  company_name = models.CharField(max_length=100, null=True, blank=True)
  position_title = models.CharField(max_length=100, null=True, blank=True)
  position_status = models.CharField(max_length=100, null=True, blank=True)

  business_address_1 = models.CharField(max_length=100, null=True, blank=True)
  business_address_2 = models.CharField(max_length=100, null=True, blank=True)
  business_address_city = models.CharField(max_length=100, null=True,
      blank=True)
  business_address_state = models.CharField(max_length=100, null=True,
      blank=True)
  business_address_zip = models.CharField(max_length=100, null=True, blank=True)
  business_address_country = models.CharField(max_length=100, null=True,
      blank=True)
  occupation = models.CharField(max_length=100, null=True, blank=True)
  industry = models.CharField(max_length=100, null=True, blank=True)

  #geolocation
  location = models.PointField(null=True, blank=True)

  # Override the default manager with GeoManager instance
  objects = models.GeoManager()

  people = models.Manager()
  geolocated = PersonLocationManager()
  names = PersonNameManager()

  user = models.OneToOneField(User, null=True, blank=True, unique=True, verbose_name=_('user'))

  #sites = models.ManyToManyField(Site)

  def makeName(self):
    n = self.name.split(',')
    self.first_name = n[1]
    self.last_name = n[0]

  def __unicode__(self):
    if self.first_name and self.last_name:
      return self.last_name + ", " + self.first_name
    elif self.name:
      self.makeName()
      return self.last_name + ', ' + self.first_name
    else:
      return u"Person object pk=%s" % self.pk

class AuthUser(models.Model):
  person = models.OneToOneField(Person, primary_key=True)
