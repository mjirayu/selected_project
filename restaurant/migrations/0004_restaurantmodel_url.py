# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0003_auto_20151107_1601'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurantmodel',
            name='url',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
