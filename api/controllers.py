# from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import *
from django.contrib.auth import *
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
# from django.shortcuts import render_to_response
from django.template import RequestContext
from django_filters.rest_framework import DjangoFilterBackend

from django.shortcuts import *

# Import models
from django.db import models
from django.contrib.auth.models import *
from api.models import *

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
import requests

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
        print('REQUEST DATA')
        print(str(request.data))

        awards = Award.objects.all()
        json_data = serializers.serialize('json', awards)
        content = {'awards': json_data}
        return HttpResponse(json_data, content_type='json')

    def post(self, request):
        title = bleach.clean(request.data.get('title'))
        description = bleach.clean(request.data.get('description'))
        award_link = bleach.clean(request.data.get('award_link'))
        sponsor_org = bleach.clean(request.data.get('sponsor_org'))
        stem_field = bleach.clean(request.data.get('stem_field'))
        recurring = bleach.clean(request.data.get('recurring'))
        nom_req = bleach.clean(request.data.get('nom_req'))
        recur_interval = bleach.clean(request.data.get('recur_interval'))
        open_date = int(request.data.get('open_date'))
        nom_deadline = int(request.data.get('nom_deadline'))
        subm_deadline = int(request.data.get('subm_deadline'))
        applicant_type = bleach.clean(request.data.get('applicant_type'))
        award_purpose = bleach.clean(request.data.get('award_purpose'))
        additional_info = bleach.clean(request.data.get('additional_info'))
        source = bleach.clean(request.data.get('source'))
        previous_applicants = int(request.data.get('previous_applicants'))
        created_by = bleach.clean(request.data.get('created_by'))
        created_on = int(request.data.get('created_on'))

        print("Creating new Page")

        newAward = Award(
            title=title,
            description=description,
            award_link=award_link,
            sponsor_org=sponsor_org,
            stem_field=stem_field,
            recurring=recurring,
            nom_req=nom_req,
            recur_interval=recur_interval,
            open_date=open_date,
            nom_deadline=nom_deadline,
            subm_deadline=subm_deadline,
            applicant_type=applicant_type,
            award_purpose=award_purpose,
            additional_info=additional_info,
            source=source,
            previous_applicants=previous_applicants,
            created_by=created_by,
            created_on=created_on
        )

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
        serializer = PageSerializer(award)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type='json')

    def put(self, request, id=None):
        print('REQUEST DATA')
        print(str(request.data))

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
            award.recurring= bleach.clean(request.data.get('recurring'))
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
        print('REQUEST DATA')
        print(str(request.data))

        Award.objects.get(pk=id).delete()
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
