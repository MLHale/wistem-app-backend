from rest_framework import serializers
from api.models import *

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

class AwardSerializer(serializers.Serializer):
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

    title = serializers.CharField(max_length=1000, allow_blank=False)
    description = serializers.CharField(allow_blank=True)
    award_link = serializers.URLField(max_length=1000, allow_blank=False)
    sponsor_org = serializers.CharField(max_length=1000, allow_blank=False)
    stem_field = StemFieldSerializer(many=True)
    recurring = serializers.BooleanField()
    nom_req = serializers.BooleanField()
    recur_interval = serializers.CharField(max_length=1000, allow_blank=False)
    open_date = serializers.DateTimeField()
    nom_deadline = serializers.DateTimeField()
    subm_deadline = serializers.DateTimeField()
    applicant_type = serializers.ChoiceField(choices=APPLICANT_TYPE_CHOICES)
    award_purpose = AwardPurposeSerializer(many=True)
    additional_info = serializers.CharField(allow_blank=True)
    source = serializers.ChoiceField(choices=AWARD_SOURCE_CHOICES)
    previous_applicants = serializers.IntegerField()
    created_by = models.ForeignKey('Profile', on_delete=models.PROTECT)
    created_on = serializers.DateTimeField()

class StemFieldSerializer(serializers.Serializer):
    field = serializers.CharField(max_length=1000, allow_blank=False)

class AwardPurposeSerializer(serializers.Serializer):
    purpose = serializers.CharField(max_length=1000, allow_blank=False)

class AreaOfInterestSerializer(serializers.Serializer):
    area = serializers.CharField(max_length=1000, allow_blank=False)
