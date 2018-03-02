# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-02 04:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0027_auto_20180228_1811'),
    ]

    operations = [
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('federal', 'Federal Government'), ('state', 'State Government'), ('local', 'Local Government'), ('internal', 'Internal'), ('private_industry', 'Private Industry'), ('other', 'Other')], max_length=100, unique=True)),
            ],
        ),
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
            name='source',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='awards', to='api.Source'),
        ),
        migrations.AlterField(
            model_name='award',
            name='stemfields',
            field=models.ManyToManyField(blank=True, related_name='awards', to='api.Stemfield'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='areasofinterest',
            field=models.ManyToManyField(blank=True, related_name='profiles', to='api.Areaofinterest'),
        ),
    ]
