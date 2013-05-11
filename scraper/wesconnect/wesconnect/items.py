# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class Alum(Item):
    # define the fields for your item here like:
    name = Field()
    mid = Field()
    page_url = Field()
    preferred_email = Field()
    company_name = Field()
    city = Field()
    state = Field()
    country = Field()

    #wesleyan education
    wesleyan_degree_school_1 = Field()
    wesleyan_degree_year_1 = Field()
    wesleyan_degree_1 = Field()
    wesleyan_degree_1_major_1 = Field()
    wesleyan_degree_1_major_2 = Field()
    wesleyan_degree_1_major_3 = Field()

    # member information
    first_name = Field()
    last_name = Field()
    nickname = Field()
    last_name_at_grad = Field()
    preferred_class_year = Field()
    preferred_email = Field()

    #primary employment
    company_name = Field()
    position_title = Field()
    position_status = Field()

    business_address_1 = Field()
    business_address_2 = Field()
    business_address_city = Field()
    business_address_state = Field()
    business_address_zip = Field()
    business_address_country = Field()
    occupation = Field()
    industry = Field()
