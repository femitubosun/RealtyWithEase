from django.contrib import admin
from user_management.models import User, UserProfile, OtpToken

admin.site.register([User, UserProfile, OtpToken])
