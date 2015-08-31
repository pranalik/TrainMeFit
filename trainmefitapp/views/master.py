
from django.shortcuts import render
from django.shortcuts import render_to_response

from django.contrib.auth.models import User


from django.http import HttpResponse
from django.http import HttpResponseRedirect

# importing constants
from constants import AppUserConstants, ExceptionLabel
from trainmefitapp.models import *

def master(request):
    return render_to_response('master.html')


def mttest(request):
    return render_to_response('test.html')
