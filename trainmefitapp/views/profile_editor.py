
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.cache import cache_control
from django.contrib import auth
from django.core.context_processors import csrf
from django.core import serializers
import pdb
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import logout
from django.contrib.auth import login
from django.shortcuts import redirect
from django.template import RequestContext
from django.db.models import Count, Sum

from django.views.generic import TemplateView

# importing mysqldb and system packages
import MySQLdb, sys
from django.db.models import Q
from django.db.models import F
from django.db import transaction

import csv
import json
#importing exceptions
from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist
from django.utils.datastructures import MultiValueDictKeyError

# imports date times
import datetime
import time
from datetime import date, timedelta

from django.http import HttpResponse
from django.http import HttpResponseRedirect

# importing constants
from constants import AppUserConstants, ExceptionLabel
from trainmefitapp.models import *
from trainmefitapp.profile_editor import get_user_profile_editor

from trainmefitapp.models import *


def get_user_profile_editor(user_id):
    try:
        user_object = UserProfile.objects.get(id=user_id)    
        
        data ={
            "Name":user_object.user_name,
            "NickName":user_object.user_nickname,
            "Age":user_object.user_age,
            "Gender":user_object.user_gender,
            "Height":user_object.user_height,
            "ProfilePic":user_object.user_profilepic,
            "FullName":user_object.user_fullname
        }
    except Exception, e:
        print e
        data = {'success':'false'}
        