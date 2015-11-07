import scrapy
from scrapy_djangoitem import DjangoItem

from restaurant.models import RestaurantModel


class SitItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    desc = scrapy.Field()


class WongNaiItem(DjangoItem):
    django_model = RestaurantModel
