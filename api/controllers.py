# from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import *
from django.contrib.auth import *
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import JSONRenderer
# from django.shortcuts import render_to_response
from django.template import RequestContext
from django_filters.rest_framework import DjangoFilterBackend

from django.shortcuts import *

# Import models
from django.db import models
from django.contrib.auth.models import *
from api.models import *
from api.serializers import *

# REST API
from rest_framework import viewsets, filters, parsers, renderers
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth import authenticate, login, logout
from rest_framework.permissions import *
from rest_framework.decorators import *
from rest_framework.authentication import *

# filters
# from filters.mixins import *

from api.pagination import *
import json, datetime, pytz
from django.core import serializers
from django.core.exceptions import *
import requests
from django.shortcuts import get_object_or_404
import bleach


def home(request):
    """
    Send requests to / to the ember.js clientside app
    """
    return render_to_response('ember/index.html',
                              {}, RequestContext(request))


def xss_example(request):
    """
    Send requests to xss-example/ to the insecure client app
    """
    return render_to_response('dumb-test-app/index.html',
                              {}, RequestContext(request))


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

        awards = Award.objects.all()
        json_data = serializers.serialize('json', awards)
        return HttpResponse(json_data, content_type='json')

    def post(self, request):
        if not request.user.is_superuser or not request.user.is_authenticated:
            raise Http404
        print('REQUEST DATA')
        print(str(request.data))
        title = bleach.clean(request.data.get('title'))
        description = bleach.clean(request.data.get('description'))
        award_link = bleach.clean(request.data.get('award_link'))
        sponsor_org = bleach.clean(request.data.get('sponsor_org'))
        stem_field = bleach.clean(request.data.get('stem_field'))
        print("stem field request data",stem_field)
        stem_field_object = StemField.objects.get_or_create(field=stem_field)
        print("stem field " + str(stem_field_object))
        recurring = bool(bleach.clean(request.data.get('recurring')))
        nom_req = bool(bleach.clean(request.data.get('nom_req')))
        recur_interval = bleach.clean(request.data.get('recur_interval'))
        open_date = datetime.datetime.fromtimestamp(request.data.get('open_date'),pytz.utc)
        print("opendate",open_date)
        nom_deadline = datetime.datetime.fromtimestamp(request.data.get('nom_deadline'),pytz.utc)
        subm_deadline = datetime.datetime.fromtimestamp(request.data.get('subm_deadline'),pytz.utc)
        applicant_type = bleach.clean(request.data.get('applicant_type'))
        applicant_type_object = ApplicantType.objects.get_or_create(appType=applicant_type)
        award_purpose = bleach.clean(request.data.get('award_purpose'))
        award_purpose_object = AwardPurpose.objects.get_or_create(purpose=award_purpose)
        print("award purpose = " + str(award_purpose_object))
        additional_info = bleach.clean(request.data.get('additional_info'))
        source = bleach.clean(request.data.get('source'))
        previous_applicants = int(request.data.get('previous_applicants'))
        created_by = "1"#request.user.id  # TODO input validation - make this take user from request - cant get postman to work
        print("created by:", created_by)
        user = get_object_or_404(User, pk=created_by)
        print("user=" + str(user))
        profile = Profile.objects.get(user=user)
        print(profile)
        # created_on = int(request.data.get('created_on'))

        print("Creating new Award")

        newAward = Award.objects.create(
            title=title,
            description=description,
            award_link=award_link,
            sponsor_org=sponsor_org,
            # stem_field=stem_field_object,
            recurring=recurring,
            nom_req=nom_req,
            recur_interval=recur_interval,
            open_date=open_date,
            nom_deadline=nom_deadline,
            subm_deadline=subm_deadline,
            # applicant_type=applicant_type_object,
            # award_purpose=award_purpose_object,
            additional_info=additional_info,
            source=source,
            previous_applicants=previous_applicants,
            created_by=profile,
            # created_on=created_on
        )
        # Award.stem_field.add(stem_field_object)
        try:
            newAward.clean_fields()
        except ValidationError as e:
            print(e)
            return Response({'success': False, 'error': e}, status=status.HTTP_400_BAD_REQUEST)

        newAward.save()
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
            raise Http404
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
        if request.data.get('sponsor_org') != None:
            award.sponsor_org = bleach.clean(request.data.get('sponsor_org'))
        if request.data.get('stem_field') != None:
            award.stem_field = bleach.clean(request.data.get('stem_field'))
        if request.data.get('recurring') != None:
            award.recurring = bleach.clean(request.data.get('recurring'))
        if request.data.get('nom_req') != None:
            award.nom_req = bleach.clean(request.data.get('nom_req'))
        if request.data.get('recur_interval') != None:
            award.recur_interval = bleach.clean(request.data.get('recur_interval'))
        if request.data.get('open_date') != None:
            award.open_date = int(request.data.get('open_date'))
        if request.data.get('nom_deadline') != None:
            award.nom_deadline = int(request.data.get('nom_deadline'))
        if request.data.get('subm_deadline') != None:
            award.subm_deadline = int(request.data.get('subm_deadline'))
        if request.data.get('applicant_type') != None:
            award.applicant_type = bleach.clean(request.data.get('applicant_type'))
        if request.data.get('award_purpose') != None:
            award.award_purpose = bleach.clean(request.data.get('award_purpose'))
        if request.data.get('additional_info') != None:
            award.additional_info = bleach.clean(request.data.get('additional_info'))
        if request.data.get('source') != None:
            award.source = bleach.clean(request.data.get('source'))
        if request.data.get('previous_applicants') != None:
            award.previous_applicants = int(request.data.get('previous_applicants'))
        if request.data.get('created_by') != None:
            award.created_by = bleach.clean(request.data.get('created_by'))
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
            raise Http404
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
            raise Http404
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
            raise Http404
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
            raise Http404
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
            raise Http404
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
            raise Http404
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
            raise Http404
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
            raise Http404
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
            raise Http404
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
            raise Http404
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
            raise Http404
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
            raise Http404
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
            raise Http404
        print('REQUEST DATA')
        print(str(request.data))

        ApplicantType.objects.get(pk=id).delete()
        return Response({'success': True}, status=status.HTTP_200_OK)


class Register(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        # Login
        username = request.POST.get('username')  # you need to apply validators to these
        print
        username
        password = request.POST.get('password')  # you need to apply validators to these
        email = request.POST.get('email')  # you need to apply validators to these
        gender = request.POST.get('gender')  # you need to apply validators to these
        age = request.POST.get('age')  # you need to apply validators to these
        educationlevel = request.POST.get('educationlevel')  # you need to apply validators to these
        city = request.POST.get('city')  # you need to apply validators to these
        state = request.POST.get('state')  # you need to apply validators to these

        print
        request.POST.get('username')
        if User.objects.filter(username=username).exists():
            return Response({'username': 'Username is taken.', 'status': 'error'})
        elif User.objects.filter(email=email).exists():
            return Response({'email': 'Email is taken.', 'status': 'error'})

        # especially before you pass them in here
        newuser = User.objects.create_user(email=email, username=username, password=password)
        newprofile = Profile(user=newuser, gender=gender, age=age, educationlevel=educationlevel, city=city,
                             state=state)
        newprofile.save()

        return Response({'status': 'success', 'userid': newuser.id, 'profile': newprofile.id})


class Session(APIView):
    permission_classes = (AllowAny,)

    def form_response(self, isauthenticated, userid, username, error=""):
        data = {
            'isauthenticated': isauthenticated,
            'userid': userid,
            'username': username
        }
        if error:
            data['message'] = error

        return Response(data)

    def get(self, request, *args, **kwargs):
        # Get the current user
        if request.user.is_authenticated():
            return self.form_response(True, request.user.id, request.user.username)
        return self.form_response(False, None, None)

    def post(self, request, *args, **kwargs):
        # Login
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return self.form_response(True, user.id, user.username)
            return self.form_response(False, None, None, "Account is suspended")
        return self.form_response(False, None, None, "Invalid username or password")

    def delete(self, request, *args, **kwargs):
        # Logout
        logout(request)
        return Response(status=status.HTTP_204_NO_CONTENT)


class Events(APIView):
    permission_classes = (AllowAny,)
    parser_classes = (parsers.JSONParser, parsers.FormParser)
    renderer_classes = (renderers.JSONRenderer,)


class ActivateIFTTT(APIView):
    permission_classes = (AllowAny,)
    parser_classes = (parsers.JSONParser, parsers.FormParser)
    renderer_classes = (renderers.JSONRenderer,)
