# @Author: Matthew Hale <matthale>
# @Date:   2018-02-28T00:25:25-06:00
# @Email:  mlhale@unomaha.edu
# @Filename: controllers.py
# @Last modified by:   matthale
# @Last modified time: 2018-02-28T11:53:53-06:00
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

def staff_or_401(request):
    if not request.user.is_staff:
        return Response({'success': False},status=status.HTTP_401_UNAUTHORIZED)

def super_user_or_401(request):
    if not request.user.is_superuser:
        return Response({'success': False},status=status.HTTP_401_UNAUTHORIZED)

def admin_or_401(request):
    if not (request.user.is_staff or request.user.is_superuser):
        return Response({'success': False},status=status.HTTP_401_UNAUTHORIZED)

class AwardViewSet(viewsets.ModelViewSet):
    """
    Profile Endpoint, loaded upon login typically alongside User
    """
    resource_name = 'awards'
    queryset = api.Award.objects.all()
    serializer_class = api.AwardSerializer
    permission_classes = (AllowAny,)
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('id', 'title', 'description', 'awardlink','sponsororg', 'recurring','nomreq','recurinterval','opendate','nomdeadline','submdeadline','additionalinfo','source','previousapplicants','createdon')

    def create(self, request):
        admin_or_401(request)

        serializer = api.AwardSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()

        return Response(serializer.data)

    def update(self, request, pk=None):
        admin_or_401(request)

        serializer = api.AwardSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()

        return Response(serializer.data)

class UserViewSet(viewsets.ModelViewSet):
	"""
	Endpoint that allows user data to be viewed.
	"""
	resource_name = 'users'
	serializer_class = api.UserSerializer
	queryset = User.objects.all()
	permission_classes = (IsAuthenticated,)

	def get_queryset(self):
		user = self.request.user
		if user.is_superuser:
			return User.objects.all()
		return User.objects.filter(username=user.username)

class ProfileViewSet(viewsets.ModelViewSet):
	"""
	Endpoint that allows user data to be viewed.
	"""
	resource_name = 'profiles'
	serializer_class = api.ProfileSerializer
	queryset = api.Profile.objects.all()
	permission_classes = (IsAuthenticated,)

	def get_queryset(self):
		user = self.request.user
		if user.is_superuser:
			return api.Profile.objects.all()
		return get_object_or_404(api.Profile, user__username=user.username)

class StemfieldViewSet(viewsets.ModelViewSet):
    """
    Stemfield endpoint
    """
    resource_name = 'stemfields'
    queryset = api.Stemfield.objects.all()
    serializer_class = api.StemfieldSerializer
    permission_classes = (AllowAny,)
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('name',)

    def create(self, request):
        admin_or_401(request)

        serializer = api.StemfieldSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()

        return Response(serializer.data)

    def update(self, request, pk=None):
        admin_or_401(request)

        serializer = api.StemfieldSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()

        return Response(serializer.data)


class AwardpurposeViewSet(viewsets.ModelViewSet):
    """
    Awardpurpose endpoint
    """
    resource_name = 'awardpurposes'
    queryset = api.Awardpurpose.objects.all()
    serializer_class = api.AwardpurposeSerializer
    permission_classes = (AllowAny,)
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('name',)

    def create(self, request):
        admin_or_401(request)

        serializer = api.AwardpurposeSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()

        return Response(serializer.data)

    def update(self, request, pk=None):
        admin_or_401(request)

        serializer = api.AwardpurposeSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()

        return Response(serializer.data)

class AreaofinterestViewSet(viewsets.ModelViewSet):
    """
    Area of interest endpoint
    """
    resource_name = 'areaofinterests'
    queryset = api.Areaofinterest.objects.all()
    serializer_class = api.AreaofinterestSerializer
    permission_classes = (AllowAny,)
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('name',)

    def create(self, request):
        admin_or_401(request)

        serializer = api.AreaofinterestSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()

        return Response(serializer.data)

    def update(self, request, pk=None):
        admin_or_401(request)

        serializer = api.AreaofinterestSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()

        return Response(serializer.data)


class ApplicanttypeViewSet(viewsets.ModelViewSet):
    """
    ApplicantType endpoint
    """
    resource_name = 'applicanttypes'
    queryset = api.Applicanttype.objects.all()
    serializer_class = api.ApplicanttypeSerializer
    permission_classes = (AllowAny,)
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('name',)

    def create(self, request):
        admin_or_401(request)

        serializer = api.ApplicanttypeSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()

        return Response(serializer.data)

    def update(self, request, pk=None):
        admin_or_401(request)

        serializer = api.ApplicanttypeSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()

        return Response(serializer.data)




class Register(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        # Login
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        lastname = request.POST.get('lastname')
        firstname = request.POST.get('firstname')
        org = request.POST.get('org')
        college = request.POST.get('college')
        dept = request.POST.get('dept')
        other_details = request.POST.get('otherdetails')
        areas_of_interest = request.POST.get('areasofinterest')
        areas_of_interest = api.Areaofinterest.objects.get_or_create(name=areas_of_interest)

        print request.POST.get('username')
        if User.objects.filter(username=username).exists():
            return Response({'username': 'Username is taken.', 'status': 'error'})
        elif User.objects.filter(email=email).exists():
            return Response({'email': 'Email is taken.', 'status': 'error'})
        # especially before you pass them in here
        newuser = User.objects.create_user(email=email, last_name=lastname, first_name=firstname, username=username, password=password)

        newprofile = api.Profile(user=newuser, org=org, college=college, dept=dept, otherdetails=other_details)
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
