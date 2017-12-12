from django.conf.urls import include, url

#Django Rest Framework
from rest_framework import routers

from api import controllers
from django.views.decorators.csrf import csrf_exempt

#REST API routes
router = routers.DefaultRouter(trailing_slash=False)

urlpatterns = [
    url(r'^session', csrf_exempt(controllers.Session.as_view())),
    url(r'^register', csrf_exempt(controllers.Register.as_view())),
    url(r'^awards/(?P<id>\d+)', csrf_exempt(controllers.AwardDetail.as_view())),
    url(r'^awards', csrf_exempt(controllers.AwardList.as_view())),
    url(r'^stemfields/(?P<id>\d+)', csrf_exempt(controllers.StemFieldDetail.as_view())),
    url(r'^stemfields', csrf_exempt(controllers.StemFieldList.as_view())),
    url(r'^awardpurposes/(?P<id>\d+)', csrf_exempt(controllers.AwardPurposeDetail.as_view())),
    url(r'^awardpurposes', csrf_exempt(controllers.AwardPurposeList.as_view())),
    url(r'^areaofinterests/(?P<id>\d+)', csrf_exempt(controllers.AreaOfInterestDetail.as_view())),
    url(r'^areaofinterests', csrf_exempt(controllers.AreaOfInterestList.as_view())),
    url(r'^applicanttypes/(?P<id>\d+)', csrf_exempt(controllers.ApplicantTypeDetail.as_view())),
    url(r'^applicanttypes', csrf_exempt(controllers.ApplicantTypeList.as_view())),
    url(r'^', include(router.urls)),
]
