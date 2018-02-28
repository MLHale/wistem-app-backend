# @Author: Matthew Hale <matthale>
# @Date:   2018-02-28T00:25:25-06:00
# @Email:  mlhale@unomaha.edu
# @Filename: models.py
# @Last modified by:   matthale
# @Last modified time: 2018-02-28T11:59:10-06:00
# @Copyright: Copyright (C) 2018 Matthew L. Hale



from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from rest_framework_json_api import serializers


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

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    org = models.CharField(max_length=30, choices=ORG_CHOICES, default=UNO)
    college = models.CharField(max_length=1000, blank=True)
    dept = models.CharField(max_length=1000, blank=True)
    otherdetails = models.CharField(max_length=1000, blank=True)
    areasofinterest = models.ManyToManyField('AreaOfInterest',blank=True)

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
    awardlink = models.URLField(max_length=1000, blank=False)
    sponsororg = models.CharField(max_length=1000, blank=False)

    recurring = models.BooleanField(default=False)
    nomreq = models.BooleanField(default=False)
    recurinterval = models.CharField(max_length=1000, blank=False)
    opendate = models.DateTimeField()
    nomdeadline = models.DateTimeField()
    submdeadline = models.DateTimeField()

    additionalinfo = models.TextField(blank=True)
    source = models.CharField(max_length=30, choices=AWARD_SOURCE_CHOICES, default=SOURCE_OTHER)
    previousapplicants = models.IntegerField(default=0, blank=False)
    createdon = models.DateTimeField(auto_now_add=True)

    # Relationships
    stemfields = models.ManyToManyField('StemField', related_name='awards', blank=True)
    applicanttypes = models.ManyToManyField('ApplicantType', related_name='awards', blank=True)
    awardpurposes = models.ManyToManyField('AwardPurpose', related_name='awards', blank=True)
    createdby = models.ForeignKey('Profile', related_name='awards', on_delete=models.PROTECT)

    def __str__(self):
        return str(self.title)

	class JSONAPIMeta:
		resource_name = "awards"


class Applicanttype(models.Model):
    name = models.CharField(max_length=1000, blank=False, unique=True)

    def __str__(self):
        return str(self.name)

	class JSONAPIMeta:
		resource_name = "applicanttypes"

class ApplicanttypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Applicanttype
        fields = ('id','name')


class Stemfield(models.Model):
    name = models.CharField(max_length=1000, blank=False, unique=True)

    def __str__(self):
        return str(self.name)

	class JSONAPIMeta:
		resource_name = "stemfields"

class StemfieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stemfield
        fields = ('id','name')


class Awardpurpose(models.Model):
    name = models.CharField(max_length=1000, blank=False, unique=True)

    def __str__(self):
        return str(self.name)

	class JSONAPIMeta:
		resource_name = "awardpurposes"

class AwardpurposeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Awardpurpose
        fields = ('id','name')


class Areaofinterest(models.Model):
    name = models.CharField(max_length=1000, blank=False)

    def __str__(self):
        return str(self.name)

	class JSONAPIMeta:
		resource_name = "areaofinterests"

class AreaofinterestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Areaofinterest
        fields = ('id','name')


class UserSerializer(serializers.ModelSerializer):
    lastname = serializers.CharField(source='last_name')
    firstname = serializers.CharField(source='first_name')
    class Meta:
		resource_name = 'users'
		model = User
		fields = ('id', 'username', 'lastname', 'firstname', 'email',)


class ProfileSerializer(serializers.ModelSerializer):
    included_serializers = {
        'user': UserSerializer,
    }
    # Related fields
    # user = UserSerializer()
    #areasofinterest = AreaOfInterestSerializer(many=True)

    class Meta:
        model = Profile
        fields = ('id', 'org', 'college', 'dept', 'otherdetails','user')

        #'applicanttype','createdby','awardpurpose','stemfield'

    class JSONAPIMeta:
		included_resources = ['user']

class AwardSerializer(serializers.ModelSerializer):
    included_serializers = {
        'createdby': ProfileSerializer,
        'applicanttypes': ApplicanttypeSerializer,
        'awardpurposes': AwardpurposeSerializer,
        'stemfields': StemfieldSerializer
    }

    # Related fields
    # createdby = ProfileSerializer()
    # applicanttype = ApplicantTypeSerializer(many=True, read_only=True)
    # awardpurpose = AwardPurposeSerializer(many=True, read_only=True)
    # stemfield = StemFieldSerializer(many=True, read_only=True)

    class Meta:
        model = Award
        fields = ('id', 'title', 'description', 'awardlink','sponsororg', 'recurring','nomreq','recurinterval','opendate','nomdeadline','submdeadline','additionalinfo','source','previousapplicants','createdon','createdby','applicanttypes','awardpurposes','stemfields')


    class JSONAPIMeta:
		included_resources = ['createdby']
