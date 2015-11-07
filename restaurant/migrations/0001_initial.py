# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RestaurantModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=60)),
                ('average', models.FloatField()),
                ('province', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=60)),
                ('image', models.ImageField(upload_to=b'')),
            ],
        ),
    ]
