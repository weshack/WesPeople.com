from django.contrib.gis.db import models

# Create your models here.
class Person(models.Model):
  # define the fields for your item here like:
  name = models.CharField(max_length=100)
  mid = models.IntegerField()
  page_url = models.URLField()
  preferred_email = models.EmailField()
  company_name = models.CharField(max_length=100)
  city = models.CharField(max_length=100)
  state = models.CharField(max_length=100)
  country = models.CharField(max_length=100)

  #wesleyan education
  wesleyan_degree_school_1 = models.CharField(max_length=100)
  wesleyan_degree_year_1 = models.IntegerField()
  wesleyan_degree_1 = models.CharField(max_length=100)
  wesleyan_degree_1_major_1 = models.CharField(max_length=100)
  wesleyan_degree_1_major_2 = models.CharField(max_length=100)
  wesleyan_degree_1_major_3 = models.CharField(max_length=100)

  # member information
  first_name = models.CharField(max_length=100)
  last_name = models.CharField(max_length=100)
  nickname = models.CharField(max_length=100)
  last_name_at_grad = models.CharField(max_length=100)
  preferred_class_year = models.IntegerField()
  preferred_email = models.CharField(max_length=100)

  #primary employment
  company_name = models.CharField(max_length=100)
  position_title = models.CharField(max_length=100)
  position_status = models.CharField(max_length=100)

  business_address_1 = models.CharField(max_length=100)
  business_address_2 = models.CharField(max_length=100)
  business_address_city = models.CharField(max_length=100)
  business_address_state = models.CharField(max_length=100)
  business_address_zip = models.CharField(max_length=100)
  business_address_country = models.CharField(max_length=100)
  occupation = models.CharField(max_length=100)
  industry = models.CharField(max_length=100)

  #geolocation
  latitude = models.PointField()
  longitude = models.PointField()
