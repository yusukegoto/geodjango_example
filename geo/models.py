from django.contrib.gis.db import models


class Restaurant(models.Model):
    name = models.CharField(max_length=255, null=False)

    def __unicode__(self):
        return self.name


class Branch(models.Model):
    name = models.CharField(max_length=255, null=False)
    restaurant = models.ForeignKey(Restaurant, null=False)

    def __unicode__(self):
        return self.name
