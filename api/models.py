from __future__ import unicode_literals

from django.db import models
from django.core.validators import *

from django.contrib.auth.models import User, Group

from django.contrib import admin
import base64

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
    areas_of_interest = models.ManyToManyField('AreaOfInterest')

    def __str__(self):
        return str(self.user.username)

class Award(models.Model):
    # Applicant Type Choices
    STAFF = 'staff'
    PROF_FAC = 'faculty_professor'
    TENURED_FAC = 'tenured_faculty'
    NON_TENURED_FAC = 'non_tenured_faculty'
    PHD = 'phd'
    GRAD_FAC = 'graduate_faculty'
    GRAD_STUD = 'graduate_student'
    UGRAD_STUD = 'undergraduate_student'
    TYPE_OTHER = 'other'
    APPLICANT_TYPE_CHOICES = (
        (STAFF, 'Staff'),
        (PROF_FAC, 'Faculty - Professor'),
        (TENURED_FAC, 'Faculty - Tenured'),
        (NON_TENURED_FAC, 'Faculty - Non-Tenured'),
        (GRAD_FAC, 'Faculty - Graduate'),
        (PHD, 'PhD Required'),
        (GRAD_STUD, 'Student - Graduate'),
        (UGRAD_STUD, 'Student - Undergraduate'),
        (TYPE_OTHER, 'Other')
    )

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
    stem_field = models.ManyToManyField('StemField')
    recurring = models.BooleanField()
    nom_req = models.BooleanField()
    recur_interval = models.CharField(max_length=1000, blank=False)
    open_date = models.DateTimeField()
    nom_deadline = models.DateTimeField()
    subm_deadline = models.DateTimeField()
    applicant_type = models.CharField(max_length=30, choices=APPLICANT_TYPE_CHOICES, default=TYPE_OTHER)
    award_purpose = models.ManyToManyField('AwardPurpose')
    additional_info = models.TextField(blank=True)
    source = models.CharField(max_length=30, choices=AWARD_SOURCE_CHOICES, default=SOURCE_OTHER)
    previous_applicants = models.IntegerField(default=0, blank=False)
    created_by = models.ForeignKey('Profile', on_delete=models.PROTECT)
    created_on = models.DateTimeField()

    def __str__(self):
        return str(self.title)

class StemField(models.Model):
    field = models.CharField(max_length=1000, blank=False)

    def __str__(self):
        return str(self.field)

class AwardPurpose(models.Model):
    purpose = models.CharField(max_length=1000, blank=False)

    def __str__(self):
        return str(self.purpose)

class AreaOfInterest(models.Model):
    area = models.CharField(max_length=1000, blank=False)
