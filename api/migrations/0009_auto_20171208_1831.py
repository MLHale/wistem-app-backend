# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-08 18:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20171206_0050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stemfield',
            name='field',
            field=models.CharField(max_length=1000, unique=True),
        ),
    ]
