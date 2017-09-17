from django.db import models


class Restaurant(models.Model):
    name = models.CharField(max_length=255, null=False)


class Branch(models.Model):
    name = models.CharField(max_length=255, null=False)
    restaurant = models.ForeignKey(Restaurant, null=False)
