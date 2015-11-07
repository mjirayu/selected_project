# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_auto_20151106_1321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurantmodel',
            name='image',
            field=models.CharField(max_length=200),
        ),
    ]
