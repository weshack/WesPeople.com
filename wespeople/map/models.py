from django.contrib.gis.db import models

# Create your models here.
class Person(models.Model):
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
  wesleyan_degree_school_1 = models.CharField(max_length=100, null=True,
      blank=True)
  wesleyan_degree_year_1 = models.CharField(max_length=100, null=True,
      blank=True)
  wesleyan_degree_1 = models.CharField(max_length=100, null=True, blank=True)
  wesleyan_degree_1_major_1 = models.CharField(max_length=100, null=True,
      blank=True)
  wesleyan_degree_1_major_2 = models.CharField(max_length=100, null=True,
      blank=True)
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
  latitude = models.PointField(null=True, blank=True)
  longitude = models.PointField(null=True, blank=True)

  # Override the default manager with GeoManager instance
  objects = models.GeoManager()
