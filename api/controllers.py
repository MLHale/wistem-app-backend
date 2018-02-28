# @Author: Matthew Hale <matthale>
# @Date:   2018-02-28T00:25:25-06:00
# @Email:  mlhale@unomaha.edu
# @Filename: controllers.py
# @Last modified by:   matthale
# @Last modified time: 2018-02-28T02:09:45-06:00
# @Copyright: Copyright (C) 2018 Matthew L. Hale


# Handy Django Functions
from django.shortcuts import get_object_or_404, render
from django.contrib.auth import authenticate, login, logout
import datetime, pytz

# Models and serializers
from django.contrib.auth.models import User
import api.models as api

# REST API Libraries
from rest_framework import viewsets, parsers, renderers
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import JSONRenderer
from django_filters.rest_framework import DjangoFilterBackend




from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import list_route
from rest_framework.authentication import *
#email
from templated_email import send_templated_mail
# filters
# from filters.mixins import *

from api.pagination import *

from django.core import serializers
from django.core.exceptions import ValidationError


import bleach


def home(request):
	"""
	Send requests to '/' to the ember.js clientside app
	"""

	return render(request, 'index.html')

class AwardViewSet(viewsets.ModelViewSet):
    """
    Profile Endpoint, loaded upon login typically alongside User
    """
    resource_name = 'awards'
    queryset = api.Award.objects.all()
    serializer_class = api.AwardSerializer
    permission_classes = (AllowAny,)

    def create(self, request):
        if not request.user.is_superuser:
            return Response({'success': False},status=status.HTTP_401_UNAUTHORIZED)

        serializer = api.AwardSerializerAdmin(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()

        return Response(serializer.data)


        # title = bleach.clean(request.data.get('title'))
        # description = bleach.clean(request.data.get('description'))
        # award_link = bleach.clean(request.data.get('award_link'))
        # sponsor_org = bleach.clean(request.data.get('sponsor_org'))
        # recurring = bool(bleach.clean(request.data.get('recurring')))
        # nom_req = bool(bleach.clean(request.data.get('nom_req')))
        # recur_interval = bleach.clean(request.data.get('recur_interval'))
        # open_date = datetime.datetime.fromtimestamp(request.data.get('open_date'),pytz.utc)
        # nom_deadline = datetime.datetime.fromtimestamp(request.data.get('nom_deadline'),pytz.utc)
        # subm_deadline = datetime.datetime.fromtimestamp(request.data.get('subm_deadline'),pytz.utc)
        # additional_info = bleach.clean(request.data.get('additional_info'))
        # source = bleach.clean(request.data.get('source'))
        # previous_applicants = int(request.data.get('previous_applicants'))
        # created_by = get_object_or_404(api.Profile,user=get_object_or_404(User,pk=request.user.id))
        #
        # newAward = api.Award.objects.create(
        #     title=title,
        #     description=description,
        #     award_link=award_link,
        #     sponsor_org=sponsor_org,
        #     recurring=recurring,
        #     nom_req=nom_req,
        #     recur_interval=recur_interval,
        #     open_date=open_date,
        #     nom_deadline=nom_deadline,
        #     subm_deadline=subm_deadline,
        #     additional_info=additional_info,
        #     source=source,
        #     previous_applicants=previous_applicants,
        #     created_by=created_by,
        #     created_on= datetime.datetime.now()
        #
        # )
        # try:
        #     newAward.clean_fields()
        # except ValidationError as e:
        #     print(e)
        #     return Response({'success': False, 'error': e}, status=status.HTTP_400_BAD_REQUEST)
        #
        # newAward.save()
        #
        # # Related fields
        # applicant_type = bleach.clean(request.data.get('applicant_type'))
        # applicant_type_object = api.ApplicantType.objects.get_or_create(appType=applicant_type)
        # newAward.applicant_type.add(applicant_type_object)
        #
        # award_purpose = bleach.clean(request.data.get('award_purpose'))
        # award_purpose_object = api.AwardPurpose.objects.get_or_create(purpose=award_purpose)
        # newAward.award_purpose.add(award_purpose_object)
        #
        # stem_field = bleach.clean(request.data.get('stem_field'))
        # stem_field_object = api.StemField.objects.get_or_create(field=stem_field)
        # newAward.stem_field.add(stem_field_object)
        #
        # serializer = api.AwardSerializerAdmin(newAward)
        # return Response(serializer.data)

class AwardList(APIView):
    permission_classes = (AllowAny,)
    parser_classes = (parsers.JSONParser, parsers.FormParser)
    renderer_classes = (renderers.JSONRenderer,)

    def get(self, request):
        if not request.user.is_authenticated:
            print(request.user)
        if request.user.is_superuser:
            print(request.user.groups)
        print('REQUEST DATA')
        print(str(request.data))

        awards = api.Award.objects.all()
        json_data = serializers.serialize('json', awards)
        return HttpResponse(json_data, content_type='json')

    def post(self, request):
        if not request.user.is_superuser or not request.user.is_authenticated:
            return Response({'success': False},status=HTTP_401_UNAUTHORIZED)
        print('REQUEST DATA')
        print(str(request.data))
        title = bleach.clean(request.data.get('title'))
        description = bleach.clean(request.data.get('description'))
        award_link = bleach.clean(request.data.get('award_link'))
        sponsor_org = bleach.clean(request.data.get('sponsor_org'))
        stem_field = bleach.clean(request.data.get('stem_field'))
        print("stem field request data", stem_field)
        stem_field_object = api.StemField.objects.get_or_create(field=stem_field)
        print("stem field " + str(stem_field_object))
        recurring = bool(bleach.clean(request.data.get('recurring')))
        nom_req = bool(bleach.clean(request.data.get('nom_req')))
        recur_interval = bleach.clean(request.data.get('recur_interval'))
        open_date = datetime.datetime.fromtimestamp(request.data.get('open_date'),pytz.utc)
        print("opendate",open_date)
        nom_deadline = datetime.datetime.fromtimestamp(request.data.get('nom_deadline'),pytz.utc)
        subm_deadline = datetime.datetime.fromtimestamp(request.data.get('subm_deadline'),pytz.utc)
        applicant_type = bleach.clean(request.data.get('applicant_type'))
        applicant_type_object = api.ApplicantType.objects.get_or_create(appType=applicant_type)
        award_purpose = bleach.clean(request.data.get('award_purpose'))
        award_purpose_object = api.AwardPurpose.objects.get_or_create(purpose=award_purpose)
        print("award purpose = " + str(award_purpose_object))
        additional_info = bleach.clean(request.data.get('additional_info'))
        source = bleach.clean(request.data.get('source'))
        previous_applicants = int(request.data.get('previous_applicants'))
        created_by = "1"#request.user.id  # TODO input validation - make this take user from request - cant get postman to work
        print("created by:", created_by)
        user = get_object_or_404(User, pk=created_by)
        print("user=" + str(user))
        profile = api.Profile.objects.get(user=user)
        print(profile)
        # created_on = int(request.data.get('created_on'))

        print("Creating new Award")

        newAward = api.Award.objects.create(
            title=title,
            description=description,
            award_link=award_link,
            sponsor_org=sponsor_org,
            recurring=recurring,
            nom_req=nom_req,
            recur_interval=recur_interval,
            open_date=open_date,
            nom_deadline=nom_deadline,
            subm_deadline=subm_deadline,
            additional_info=additional_info,
            source=source,
            previous_applicants=previous_applicants,
            created_by=profile,
            created_on= datetime.datetime.now()

        )
        try:
            newAward.clean_fields()
        except ValidationError as e:
            print(e)
            return Response({'success': False, 'error': e}, status=status.HTTP_400_BAD_REQUEST)

        newAward.save()
        newAward.stem_field.add(api.StemField.objects.get(field=request.data.get('stem_field')))
        newAward.applicant_type.add(api.ApplicantType.objects.get(appType=request.data.get('applicant_type')))
        newAward.award_purpose.add(api.AwardPurpose.objects.get(purpose=request.data.get('award_purpose')))

        print('New Page added: ' + title)
        return Response({'success': True}, status=status.HTTP_200_OK)


class AwardDetail(APIView):
    permission_classes = (AllowAny,)
    parser_classes = (parsers.JSONParser, parsers.FormParser)
    renderer_classes = (renderers.JSONRenderer,)

    def get(self, request, id=None, format=None):
        print('REQUEST DATA')
        print(str(request.data))

        try:
            award = Award.objects.get(pk=id)
        except ObjectDoesNotExist as e:
            return Response({'success': False, 'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        serializer = AwardSerializer(award)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type='json')

    def put(self, request, id=None):
        if not request.user.is_superuser:
            return Response({'success': False},status=HTTP_401_UNAUTHORIZED)
        try:
            award = Award.objects.get(pk=id)
        except ObjectDoesNotExist as e:
            return Response({'success': False, 'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        if request.data.get('title') != None:
            award.title = bleach.clean(request.data.get('title'))
        if request.data.get('description') != None:
            award.description = bleach.clean(request.data.get('description'))
        if request.data.get('award_link') != None:
            award.award_link = bleach.clean(request.data.get('award_link'))
        if request.data.get('stem_field') != None:
            stem_field = bleach.clean(request.data.get('stem_field'))
            stem_field_object = StemField.objects.get_or_create(field=stem_field)
            award.stem_field.clear()
            award.stem_field.add(stem_field_object[0])
        if request.data.get('sponsor_org') != None:
            award.sponsor_org = bleach.clean(request.data.get('sponsor_org'))
        if request.data.get('recurring') != None:
            award.recurring = bool(bleach.clean(request.data.get('recurring')))
        if request.data.get('nom_req') != None:
            award.nom_req = bool(bleach.clean(request.data.get('nom_req')))
        if request.data.get('recur_interval') != None:
            award.recur_interval = bleach.clean(request.data.get('recur_interval'))
        if request.data.get('open_date') != None:
            award.open_date = datetime.datetime.fromtimestamp(request.data.get('open_date'),pytz.utc)
        if request.data.get('nom_deadline') != None:
            award.nom_deadline = datetime.datetime.fromtimestamp(request.data.get('nom_deadline'),pytz.utc)
        if request.data.get('subm_deadline') != None:
            award.subm_deadline = datetime.datetime.fromtimestamp(request.data.get('subm_deadline'),pytz.utc)
        if request.data.get('applicant_type') != None:
            applicant_type = bleach.clean(request.data.get('applicant_type'))
            applicant_type_object = ApplicantType.objects.get_or_create(appType=applicant_type)
            award.applicant_type.clear()
            award.applicant_type.add(applicant_type_object[0])
        if request.data.get('award_purpose') != None:
            award_purpose = bleach.clean(request.data.get('award_purpose'))
            award_purpose_object = AwardPurpose.objects.get_or_create(purpose=award_purpose)
            award.award_purpose.clear()
            award.award_purpose.add(award_purpose_object[0])
        if request.data.get('additional_info') != None:
            award.additional_info = bleach.clean(request.data.get('additional_info'))
        if request.data.get('source') != None:
            award.source = bleach.clean(request.data.get('source'))
        if request.data.get('previous_applicants') != None:
            award.previous_applicants = int(request.data.get('previous_applicants'))
        if request.data.get('created_by') != None:
            created_by = "1"  # request.user.id  # TODO input validation - make this take user from request - cant get postman to work
            print("created by:", created_by)
            user = get_object_or_404(User, pk=created_by)
            print("user=" + str(user))
            profile = Profile.objects.get(user=user)
            award.created_by = profile
        if request.data.get('created_on') != None:
            award.created_on = int(request.data.get('created_on'))

        try:
            award.clean_fields()
        except ValidationError as e:
            print(e)
            return Response({'success': False, 'error': e}, status=status.HTTP_400_BAD_REQUEST)

        award.save()
        print('Award updated: ' + award.title)
        return Response({'success': True}, status=status.HTTP_200_OK)

    def delete(self, request, id=None):
        if not request.user.is_superuser:
            return Response({'success': False},status=HTTP_401_UNAUTHORIZED)
        print('REQUEST DATA')
        print(str(request.data))

        Award.objects.get(pk=id).delete()
        return Response({'success': True}, status=status.HTTP_200_OK)


class StemFieldList(APIView):
    permission_classes = (AllowAny,)
    parser_classes = (parsers.JSONParser, parsers.FormParser)
    renderer_classes = (renderers.JSONRenderer,)

    def get(self, request):
        print('REQUEST DATA')
        print(str(request.data))

        field = StemField.objects.all()
        json_data = serializers.serialize('json', field)
        return HttpResponse(json_data, content_type='json')

    def post(self, request):
        if not request.user.is_superuser or not request.user.is_authenticated:
            return Response({'success': False},status=HTTP_401_UNAUTHORIZED)
        field = bleach.clean(request.data.get('field'))

        newStemField = StemField(
            field=field
        )
        try:
            newStemField.clean_fields()
        except ValidationError as e:
            print(e)
            return Response({'success': False, 'error': e}, status=status.HTTP_400_BAD_REQUEST)

        newStemField.save()
        print('New Stem Field added: ' + field)
        return Response({'success': True}, status=status.HTTP_200_OK)


class StemFieldDetail(APIView):
    def get(self, request, id=None, format=None):
        print('REQUEST DATA')
        print(str(request.data))

        try:
            stemfield = StemField.objects.get(pk=id)
        except ObjectDoesNotExist as e:
            return Response({'success': False, 'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        serializer = StemFieldSerializer(stemfield)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type='json')

    def put(self, request, id=None):
        if not request.user.is_superuser:
            return Response({'success': False},status=HTTP_401_UNAUTHORIZED)
        print('REQUEST DATA')
        print(str(request.data))

        try:
            stemfield = StemField.objects.get(pk=id)
        except ObjectDoesNotExist as e:
            return Response({'success': False, 'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        if request.data.get('field') != None:
            stemfield.field = bleach.clean(request.data.get('field'))
        try:
            stemfield.clean_fields()
        except ValidationError as e:
            print(e)
            return Response({'success': False, 'error': e}, status=status.HTTP_400_BAD_REQUEST)

        stemfield.save()
        print('Stem Field updated: ' + stemfield.field)
        return Response({'success': True}, status=status.HTTP_200_OK)

    def delete(self, request, id=None):
        if not request.user.is_superuser:
            return Response({'success': False},status=HTTP_401_UNAUTHORIZED)
        print('REQUEST DATA')
        print(str(request.data))

        StemField.objects.get(pk=id).delete()
        return Response({'success': True}, status=status.HTTP_200_OK)


class AwardPurposeList(APIView):
    permission_classes = (AllowAny,)
    parser_classes = (parsers.JSONParser, parsers.FormParser)
    renderer_classes = (renderers.JSONRenderer,)

    def get(self, request):
        print('REQUEST DATA')
        print(str(request.data))

        purpose = AwardPurpose.objects.all()
        json_data = serializers.serialize('json', purpose)
        return HttpResponse(json_data, content_type='json')

    def post(self, request):
        if not request.user.is_superuser or not request.user.is_authenticated:
            return Response({'success': False},status=HTTP_401_UNAUTHORIZED)
        purpose = bleach.clean(request.data.get('purpose'))

        newAwardPurpose = AwardPurpose(
            purpose=purpose
        )
        try:
            newAwardPurpose.clean_fields()
        except ValidationError as e:
            print(e)
            return Response({'success': False, 'error': e}, status=status.HTTP_400_BAD_REQUEST)

        newAwardPurpose.save()
        print('New Award Purpose added: ' + purpose)
        return Response({'success': True}, status=status.HTTP_200_OK)


class AwardPurposeDetail(APIView):
    def get(self, request, id=None, format=None):
        print('REQUEST DATA')
        print(str(request.data))

        try:
            awardpurpose = AwardPurpose.objects.get(pk=id)
        except ObjectDoesNotExist as e:
            return Response({'success': False, 'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        serializer = AwardPurposeSerializer(awardpurpose)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type='json')

    def put(self, request, id=None):
        if not request.user.is_superuser:
            return Response({'success': False},status=HTTP_401_UNAUTHORIZED)
        print('REQUEST DATA')
        print(str(request.data))

        try:
            awardpurpose = AwardPurpose.objects.get(pk=id)
        except ObjectDoesNotExist as e:
            return Response({'success': False, 'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

        if request.data.get('purpose') != None:
            awardpurpose.purpose = bleach.clean(request.data.get('purpose'))
        try:
            awardpurpose.clean_fields()
        except ValidationError as e:
            print(e)
            return Response({'success': False, 'error': e}, status=status.HTTP_400_BAD_REQUEST)

        awardpurpose.save()
        print('Award Purpose updated: ' + awardpurpose.purpose)
        return Response({'success': True}, status=status.HTTP_200_OK)

    def delete(self, request, id=None):
        if not request.user.is_superuser:
            return Response({'success': False},status=HTTP_401_UNAUTHORIZED)
        print('REQUEST DATA')
        print(str(request.data))

        AwardPurpose.objects.get(pk=id).delete()
        return Response({'success': True}, status=status.HTTP_200_OK)


class AreaOfInterestList(APIView):
    permission_classes = (AllowAny,)
    parser_classes = (parsers.JSONParser, parsers.FormParser)
    renderer_classes = (renderers.JSONRenderer,)

    def get(self, request):
        print('REQUEST DATA')
        print(str(request.data))

        area = AreaOfInterest.objects.all()
        json_data = serializers.serialize('json', area)
        return HttpResponse(json_data, content_type='json')

    def post(self, request):
        if not request.user.is_superuser or not request.user.is_authenticated:
            return Response({'success': False},status=HTTP_401_UNAUTHORIZED)
        area = bleach.clean(request.data.get('area'))

        newAreaOfInterest = AreaOfInterest(
            area=area
        )
        try:
            newAreaOfInterest.clean_fields()
        except ValidationError as e:
            print(e)
            return Response({'success': False, 'error': e}, status=status.HTTP_400_BAD_REQUEST)

        newAreaOfInterest.save()
        print('New Area of Interest added: ' + area)
        return Response({'success': True}, status=status.HTTP_200_OK)


class AreaOfInterestDetail(APIView):
    def get(self, request, id=None, format=None):
        print('REQUEST DATA')
        print(str(request.data))

        try:
            areaofinterest = AreaOfInterest.objects.get(pk=id)
        except ObjectDoesNotExist as e:
            return Response({'success': False, 'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        serializer = AreaOfInterestSerializer(areaofinterest)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type='json')

    def put(self, request, id=None):
        if not request.user.is_superuser:
            return Response({'success': False},status=HTTP_401_UNAUTHORIZED)
        print('REQUEST DATA')
        print(str(request.data))

        try:
            areaofinterest = AreaOfInterest.objects.get(pk=id)
        except ObjectDoesNotExist as e:
            return Response({'success': False, 'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        if request.data.get('area') != None:
            areaofinterest.area = bleach.clean(request.data.get('area'))
        try:
            areaofinterest.clean_fields()
        except ValidationError as e:
            print(e)
            return Response({'success': False, 'error': e}, status=status.HTTP_400_BAD_REQUEST)

        areaofinterest.save()
        print('Area of Interest updated: ' + areaofinterest.area)
        return Response({'success': True}, status=status.HTTP_200_OK)

    def delete(self, request, id=None):
        if not request.user.is_superuser:
            return Response({'success': False},status=HTTP_401_UNAUTHORIZED)
        print('REQUEST DATA')
        print(str(request.data))

        AreaOfInterest.objects.get(pk=id).delete()
        return Response({'success': True}, status=status.HTTP_200_OK)


class ApplicantTypeList(APIView):
    permission_classes = (AllowAny,)
    parser_classes = (parsers.JSONParser, parsers.FormParser)
    renderer_classes = (renderers.JSONRenderer,)

    def get(self, request):
        print('REQUEST DATA')
        print(str(request.data))

        appType = ApplicantType.objects.all()
        json_data = serializers.serialize('json', appType)
        return HttpResponse(json_data, content_type='json')

    def post(self, request):
        if not request.user.is_superuser or not request.user.is_authenticated:
            return Response({'success': False},status=HTTP_401_UNAUTHORIZED)
        print('REQUEST DATA')
        print(str(request.data))
        appType = bleach.clean(request.data.get('appType'))

        newApplicantType = ApplicantType(
            appType=appType
        )
        try:
            newApplicantType.clean_fields()
        except ValidationError as e:
            print(e)
            return Response({'success': False, 'error': e}, status=status.HTTP_400_BAD_REQUEST)

        newApplicantType.save()
        print('New Applicant Type added: ' + appType)
        return Response({'success': True}, status=status.HTTP_200_OK)


class ApplicantTypeDetail(APIView):
    def get(self, request, id=None, format=None):
        print('REQUEST DATA')
        print(str(request.data))

        try:
            applicanttype = ApplicantType.objects.get(pk=id)
        except ObjectDoesNotExist as e:
            return Response({'success': False, 'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        serializer = ApplicantTypeSerializer(applicanttype)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type='json')

    def put(self, request, id=None):
        if not request.user.is_superuser:
            return Response({'success': False},status=HTTP_401_UNAUTHORIZED)
        print('REQUEST DATA')
        print(str(request.data))

        try:
            applicanttype = ApplicantType.objects.get(pk=id)
        except ObjectDoesNotExist as e:
            return Response({'success': False, 'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        if request.data.get('appType') != None:
            applicanttype.appType = bleach.clean(request.data.get('appType'))
        try:
            applicanttype.clean_fields()
        except ValidationError as e:
            print(e)
            return Response({'success': False, 'error': e}, status=status.HTTP_400_BAD_REQUEST)

        applicanttype.save()
        print('Applicatant type updated: ' + applicanttype.appType)
        return Response({'success': True}, status=status.HTTP_200_OK)

    def delete(self, request, id=None):
        if not request.user.is_superuser:
            return Response({'success': False},status=HTTP_401_UNAUTHORIZED)
        print('REQUEST DATA')
        print(str(request.data))

        ApplicantType.objects.get(pk=id).delete()
        return Response({'success': True}, status=status.HTTP_200_OK)


class Register(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        # Login
        username = request.POST.get('username')  # you need to apply validators to these
        #print username
        password = request.POST.get('password')  # you need to apply validators to these
        email = request.POST.get('email')  # you need to apply validators to these
        #gender = request.POST.get('gender')  # you need to apply validators to these
        #age = request.POST.get('age')  # you need to apply validators to these
        #educationlevel = request.POST.get('educationlevel')  # you need to apply validators to these
        #city = request.POST.get('city')  # you need to apply validators to these
        #state = request.POST.get('state')  # you need to apply validators to these
        org = request.POST.get('org')  # you need to apply validators to these
        college = request.POST.get('college')  # you need to apply validators to these
        dept = request.POST.get('dept')  # you need to apply validators to these
        other_details = request.POST.get('other_details')  # you need to apply validators to these
        areas_of_interest = request.POST.get('areas_of_interest')
        areas_of_interest = AreaOfInterest.objects.get_or_create(area=areas_of_interest)

        print request.POST.get('username')
        if User.objects.filter(username=username).exists():
            return Response({'username': 'Username is taken.', 'status': 'error'})
        elif User.objects.filter(email=email).exists():
            return Response({'email': 'Email is taken.', 'status': 'error'})
        # especially before you pass them in here
        newuser = User.objects.create_user(email=email, username=username, password=password)

        newprofile = Profile(user=newuser, org=org, college=college, dept=dept, other_details=other_details)
                           #  areas_of_interest=areas_of_interest)
        newprofile.save()
        # Send email msg
        send_templated_mail(
        template_name='welcome',
        from_email='from@example.com',
        recipient_list=[email],
        context={
            'username':username,
            'email':email,
        },
        # Optional:
        # cc=['cc@example.com'],
        # bcc=['bcc@example.com'],
        )
        return Response({'status': 'success', 'userid': newuser.id, 'profile': newprofile.id})


class Session(APIView):
	"""
	Returns a JSON structure: {'isauthenticated':<T|F>,'userid': <int:None>,'username': <string|None>,'profileid': <int|None>}
	"""
	permission_classes = (AllowAny,)
	def form_response(self, isauthenticated, userid, username, profileid, error=""):
		data = {
			'isauthenticated': 	isauthenticated,
			'userid': 			userid,
			'username': 		username,
			'profileid':		profileid,
		}
		if error:
			data['message'] = error

		return Response(data)

	def get(self, request, *args, **kwargs):
		# Get the current user
		user = request.user
		if user.is_authenticated():
			profile = get_object_or_404(api.Profile,user__username=user.username)
			return self.form_response(True, user.id, user.username, profile.id)
		return self.form_response(False, None, None, None)

	def post(self, request, *args, **kwargs):
		print(request.data)
		# Login
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				profile = get_object_or_404(api.Profile,user__username=user.username)
				return self.form_response(True, user.id, user.username, profile.id)
			return self.form_response(False, None, None, None, "Account is suspended")
		return self.form_response(False, None, None, None, "Invalid username or password")

	def delete(self, request, *args, **kwargs):
		# Logout
		logout(request)
		return Response(status=status.HTTP_204_NO_CONTENT)

class Search(APIView):
    permission_classes = (AllowAny,)
    parser_classes = (parsers.JSONParser,parsers.FormParser)
    renderer_classes = (renderers.JSONRenderer, )

    def get_valid_fields(self, request, valid_fields):
        query_dict = {}
        for query_param in request.query_params:
            if query_param in valid_fields:
                query_dict[query_param] = request.query_params[query_param]
        return query_dict

    def build_date_search(self,date_params,search_dict):
        for date_param in date_params:
            if 'start' in date_param:
                start_date = datetime.datetime.fromtimestamp(float(date_params[date_param]), pytz.utc)
                search_dict[date_param.split('start')[0] + '_range'] = (start_date,datetime.datetime.max)
            if 'end' in date_param:
                end_date = datetime.datetime.fromtimestamp(float(date_params[date_param]), pytz.utc)
                search_dict[date_param.split('end')[0] + '_range'] = (datetime.datetime.min, end_date)
        return search_dict

    def build_model_search(self, model_params,search_dict):
        for model_param in model_params:
            if model_param == 'stem_field':
                search_dict[model_param + '__field'] = model_params[model_param]
            elif model_param == 'applicant_type':
                search_dict[model_param + '__appType'] = model_params[model_param]
            elif model_param == 'award_purpose':
                search_dict[model_param + '__purpose'] = model_params[model_param]
        return search_dict

    def get(self, request, *args, **kwargs):
        matches = Award.objects.all()
        model_fields = ['stem_field', 'applicant_type', 'award_purpose']
        normal_fields =['title', 'description', 'award_link','sponsor_org','recurring', 'nom_req',
                        'recur_interval', 'additional_info', 'source', 'previous_applicants' ,'created_by' ]
        date_fields = ['open_date_start', 'open_date_end', 'nom_deadline_start', 'nom_deadline_end', 'subm_deadline_start',
                      'subm_deadline_end', 'created_on_start', 'created_on_end' ]

        search_dict = self.get_valid_fields(request, normal_fields)
        search_dict = self.build_date_search(self.get_valid_fields(request, date_fields),search_dict)
        search_dict = self.build_model_search(self.get_valid_fields(request, model_fields),search_dict)

        try:
            matches = Award.objects.filter(**search_dict)
        except ObjectDoesNotExist as e:
            return Response({'success': False, 'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

        json_data = serializers.serialize('json',matches)
        content = {'matches': json_data}
        return HttpResponse(json_data, content_type='json')
