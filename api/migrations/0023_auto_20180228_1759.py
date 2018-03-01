# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-28 17:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0022_auto_20180228_1758'),
    ]

    operations = [
        migrations.AlterField(
            model_name='award',
            name='applicanttypes',
            field=models.ManyToManyField(blank=True, related_name='awards', to='api.Applicanttype'),
        ),
        migrations.AlterField(
            model_name='award',
            name='awardpurposes',
            field=models.ManyToManyField(blank=True, related_name='awards', to='api.Awardpurpose'),
        ),
        migrations.AlterField(
            model_name='award',
            name='createdby',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='awards', to='api.Profile'),
        ),
        migrations.AlterField(
            model_name='award',
            name='stemfields',
            field=models.ManyToManyField(blank=True, related_name='awards', to='api.Stemfield'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='areasofinterest',
            field=models.ManyToManyField(blank=True, to='api.Areaofinterest'),
        ),
    ]