from django.shortcuts import render
from django.shortcuts import render_to_response

from django.contrib.auth.models import User


from django.http import HttpResponse
from django.http import HttpResponseRedirect

# importing constants
from constants import AppUserConstants, ExceptionLabel
from trainmefitapp.models import *

