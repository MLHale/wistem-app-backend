# @Author: Matthew Hale <matthale>
# @Date:   2018-02-28T00:25:25-06:00
# @Email:  mlhale@unomaha.edu
# @Filename: models.py
# @Last modified by:   matthale
# @Last modified time: 2018-02-28T02:04:15-06:00
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

class UserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150, allow_blank=False)
    first_name = serializers.CharField(max_length=30, allow_blank=True)
    last_name = serializers.CharField(max_length=30, allow_blank=True)
    email = serializers.EmailField(allow_blank=True)


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
    stemfield = models.ManyToManyField('StemField', blank=True)
    recurring = models.BooleanField(default=False)
    nomreq = models.BooleanField(default=False)
    recurinterval = models.CharField(max_length=1000, blank=False)
    opendate = models.DateTimeField()
    nomdeadline = models.DateTimeField()
    submdeadline = models.DateTimeField()
    applicanttype = models.ManyToManyField('ApplicantType', blank=True)
    awardpurpose = models.ManyToManyField('AwardPurpose', blank=True)
    additionalinfo = models.TextField(blank=True)
    source = models.CharField(max_length=30, choices=AWARD_SOURCE_CHOICES, default=SOURCE_OTHER)
    previous_applicants = models.IntegerField(default=0, blank=False)
    createdby = models.ForeignKey('Profile', on_delete=models.PROTECT)
    createdon = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title)

	class JSONAPIMeta:
		resource_name = "awards"

class ApplicantType(models.Model):
    appType = models.CharField(max_length=1000, blank=False, unique=True)

    def __str__(self):
        return str(self.appType)

class ApplicantTypeSerializer(serializers.Serializer):
    appType = serializers.CharField(max_length=1000, allow_blank=False)

class StemField(models.Model):
    field = models.CharField(max_length=1000, blank=False, unique=True)

    def __str__(self):
        return str(self.field)

class StemFieldSerializer(serializers.Serializer):
    field = serializers.CharField(max_length=1000, allow_blank=False)

class AwardPurpose(models.Model):
    purpose = models.CharField(max_length=1000, blank=False, unique=True)

    def __str__(self):
        return str(self.purpose)

class AwardPurposeSerializer(serializers.Serializer):
    purpose = serializers.CharField(max_length=1000, allow_blank=False)

class AreaOfInterest(models.Model):
    area = models.CharField(max_length=1000, blank=False)

    def __str__(self):
        return str(self.area)

class AreaOfInterestSerializer(serializers.Serializer):
    area = serializers.CharField(max_length=1000, allow_blank=False)

class ProfileSerializer(serializers.Serializer):
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

    user = UserSerializer()
    org = serializers.ChoiceField(choices=ORG_CHOICES)
    college = serializers.CharField(max_length=1000, allow_blank=True)
    dept = serializers.CharField(max_length=1000, allow_blank=True)
    other_details = serializers.CharField(max_length=1000, allow_blank=True)
    areas_of_interest = AreaOfInterestSerializer(many=True)

class AwardSerializerAdmin(serializers.Serializer):
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

    title = serializers.CharField(max_length=1000, allow_blank=False)
    description = serializers.CharField(allow_blank=True)
    awardlink = serializers.URLField(max_length=1000, allow_blank=False)
    sponsororg = serializers.CharField(max_length=1000, allow_blank=False)
    recurring = serializers.BooleanField()
    nomreq = serializers.BooleanField()
    recurinterval = serializers.CharField(max_length=1000, allow_blank=False)
    opendate = serializers.DateTimeField()
    nomdeadline = serializers.DateTimeField()
    submdeadline = serializers.DateTimeField()
    additionalinfo = serializers.CharField(allow_blank=True)
    source = serializers.ChoiceField(choices=AWARD_SOURCE_CHOICES)
    previousapplicants = serializers.IntegerField()
    createdon = serializers.DateTimeField()

    # Related fields
    createdby = ProfileSerializer()
    applicant_type = ApplicantTypeSerializer(many=True)
    award_purpose = AwardPurposeSerializer(many=True)
    stem_field = StemFieldSerializer(many=True)

    class Meta:
        model = Award
        fields = ('id', 'title', 'description', 'awardlink','sponsororg', 'recurring','nomreq','recurinterval','opendate','nomdeadline','submdeadline','additionalinfo','source','previousapplicants','createdby','ccreatedon')

class AwardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Award
        depth = 1
        fields = "__all__"
