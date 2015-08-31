
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets



# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = patterns(
	url(r'^myprofile/', 'restmobileapp.tmfapi.get_myprofile',name='myprofile'),
)

