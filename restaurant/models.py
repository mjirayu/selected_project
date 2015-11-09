from django.db import models


class RestaurantModel(models.Model):
    title = models.CharField(max_length=60, unique=True)
    average = models.FloatField()
    province = models.CharField(max_length=200)
    category = models.CharField(max_length=60)
    image = models.CharField(max_length=200)
    url = models.CharField(max_length=200, null=True)
