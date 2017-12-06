from django.contrib import admin

#if ENVIRONMENT == 'PROD':
#	from api.models import *
#else:
from api.models import *

# Register your models here.
admin.site.register(Award)
admin.site.register(StemField)
admin.site.register(AwardPurpose)
admin.site.register(AreaOfInterest)
admin.site.register(Profile)
admin.site.register(ApplicantType)

