from django.contrib import admin
from .models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('name','name')

admin.site.register(UserProfile, UserProfileAdmin)
