# @Author: Matthew Hale <matthale>
# @Date:   2018-02-28T00:25:25-06:00
# @Email:  mlhale@unomaha.edu
# @Filename: models.py
# @Last modified by:   matthale
# @Last modified time: 2018-02-28T00:40:48-06:00
# @Copyright: Copyright (C) 2018 Matthew L. Hale



from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User


class Profile(models.Model):
    UNL = 'unl'
    UNO = 'uno'
    UNMC = 'unmc'
    UNK = 'unk'
    ORG_OTHER = 'other'
    ORG_CHOICES = (
        (UNL, 'University of Nebraska - Lincoln'),
        (UNO, 'University of Nebraska - Omaha'),
        (UNMC, 'University of Nebraska Medical Center'),
        (UNK, 'University of Nebraska - Kearney'),
        (ORG_OTHER, 'Other'),
    )

    user = models.ForeignKey(
        User,
        models.CASCADE
    )
    org = models.CharField(max_length=30, choices=ORG_CHOICES, default=UNO)
    college = models.CharField(max_length=1000, blank=True)
    dept = models.CharField(max_length=1000, blank=True)
    other_details = models.CharField(max_length=1000, blank=True)
    areas_of_interest = models.ManyToManyField('AreaOfInterest',blank=True)

    def __str__(self):
        return str(self.user.username)

class Award(models.Model):
        # Award Source choices
    FED = 'federal'
    LOCAL = 'local'
    STATE = 'state'
    PRIV = 'private_industry'
    INT = 'internal'
    SOURCE_OTHER = 'other'
    AWARD_SOURCE_CHOICES = (
        (FED, 'Federal Government'),
        (STATE,'State Government'),
        (LOCAL, 'Local Government'),
        (INT, 'Internal'),
        (PRIV, 'Private Industry'),
        (SOURCE_OTHER, 'Other')
    )

    title = models.CharField(max_length=1000, blank=False)
    description = models.TextField(blank=True)
    award_link = models.URLField(max_length=1000, blank=False)
    sponsor_org = models.CharField(max_length=1000, blank=False)
    stem_field = models.ManyToManyField('StemField', blank=True)
    recurring = models.BooleanField(default=False)
    nom_req = models.BooleanField(default=False)
    recur_interval = models.CharField(max_length=1000, blank=False)
    open_date = models.DateTimeField()
    nom_deadline = models.DateTimeField()
    subm_deadline = models.DateTimeField()
    applicant_type = models.ManyToManyField('ApplicantType', blank=True)
    award_purpose = models.ManyToManyField('AwardPurpose', blank=True)
    additional_info = models.TextField(blank=True)
    source = models.CharField(max_length=30, choices=AWARD_SOURCE_CHOICES, default=SOURCE_OTHER)
    previous_applicants = models.IntegerField(default=0, blank=False)
    created_by = models.ForeignKey('Profile', on_delete=models.PROTECT)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title)


class ApplicantType(models.Model):
    appType = models.CharField(max_length=1000, blank=False, unique=True)

    def __str__(self):
        return str(self.appType)


class StemField(models.Model):
    field = models.CharField(max_length=1000, blank=False, unique=True)

    def __str__(self):
        return str(self.field)

class AwardPurpose(models.Model):
    purpose = models.CharField(max_length=1000, blank=False, unique=True)

    def __str__(self):
        return str(self.purpose)

class AreaOfInterest(models.Model):
    area = models.CharField(max_length=1000, blank=False)

    def __str__(self):
        return str(self.area)
