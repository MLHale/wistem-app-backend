#from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import *
from django.contrib.auth import *
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
#from django.shortcuts import render_to_response
from django.template import RequestContext
from django_filters.rest_framework import DjangoFilterBackend


from django.shortcuts import *

# Import models
from django.db import models
from django.contrib.auth.models import *
from api.models import *
from api.serializers import *

#REST API
from rest_framework import viewsets, filters, parsers, renderers
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth import authenticate, login, logout
from rest_framework.permissions import *
from rest_framework.decorators import *
from rest_framework.authentication import *

#filters
#from filters.mixins import *

from api.pagination import *
import json, datetime, pytz
from django.core import serializers
import requests


def home(request):
   """
   Send requests to / to the ember.js clientside app
   """
   return render_to_response('ember/index.html',
               {}, RequestContext(request))

class Register(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        # Login
        username = request.POST.get('username') #you need to apply validators to these
        print username
        password = request.POST.get('password') #you need to apply validators to these
        email = request.POST.get('email') #you need to apply validators to these
        gender = request.POST.get('gender') #you need to apply validators to these
        age = request.POST.get('age') #you need to apply validators to these
        educationlevel = request.POST.get('educationlevel') #you need to apply validators to these
        city = request.POST.get('city') #you need to apply validators to these
        state = request.POST.get('state') #you need to apply validators to these

        print request.POST.get('username')
        if User.objects.filter(username=username).exists():
            return Response({'username': 'Username is taken.', 'status': 'error'})
        elif User.objects.filter(email=email).exists():
            return Response({'email': 'Email is taken.', 'status': 'error'})

        #especially before you pass them in here
        newuser = User.objects.create_user(email=email, username=username, password=password)
        newprofile = Profile(user=newuser, gender=gender, age=age, educationlevel=educationlevel, city=city, state=state)
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

class Search(APIView):
    permission_classes = (AllowAny,)

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
        matches = Award.objects.filter(**search_dict)


        return HttpResponse('Placeholder')



class Events(APIView):
    permission_classes = (AllowAny,)
    parser_classes = (parsers.JSONParser,parsers.FormParser)
    renderer_classes = (renderers.JSONRenderer, )


class ActivateIFTTT(APIView):
    permission_classes = (AllowAny,)
    parser_classes = (parsers.JSONParser,parsers.FormParser)
    renderer_classes = (renderers.JSONRenderer, )
