from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from .views import AdsManagmentViewApi

router = DefaultRouter()

router.register(r'ads-management', AdsManagmentViewApi, base_name='ads-management')

urlpatterns = [
    url(r'^', include(router.urls)),
]
