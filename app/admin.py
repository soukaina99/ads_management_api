from django.contrib import admin

from .models import UserAd,Ad

# Register your models here.

admin.site.register(Ad)
admin.site.register(UserAd)