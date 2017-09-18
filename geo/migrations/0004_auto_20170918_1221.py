# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('geo', '0003_branch_point'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branch',
            name='point',
            field=django.contrib.gis.db.models.fields.PointField(default=b'Point(136 35)', srid=4326),
        ),
    ]
