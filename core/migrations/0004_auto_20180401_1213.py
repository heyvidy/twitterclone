# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-01 06:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20180401_1207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='dob',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
