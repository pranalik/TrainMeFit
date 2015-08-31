from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from restmobileapp.model import *
from restmobileapp.serializers import UserSerializer




 
