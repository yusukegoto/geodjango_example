from django.contrib.gis.db import models
from django.contrib.gis.geos import Point


class Restaurant(models.Model):
    name = models.CharField(max_length=255, null=False)

    def __unicode__(self):
        return self.name


class Branch(models.Model):
    name = models.CharField(max_length=255, null=False)
    restaurant = models.ForeignKey(Restaurant, null=False)
    point = models.PointField(default='Point(136 35)')

    def __unicode__(self):
        return self.name
