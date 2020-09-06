from django.contrib import admin
from poll_app.models import Instructors,Questions,Answers,userProfileInfo

# Register your models here.
admin.site.register(userProfileInfo)
admin.site.register(Instructors)
admin.site.register(Questions)
admin.site.register(Answers)
