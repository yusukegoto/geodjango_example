# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('geo', '0002_branch'),
    ]

    operations = [
        migrations.AddField(
            model_name='branch',
            name='point',
            field=django.contrib.gis.db.models.fields.PointField(srid=4326, null=True),
        ),
    ]
