"""
__author__      = 'ManojB'
__version__     = '0.0.1'
__createddate__ = '30-04-2015'
This module is related to user profile and all the operations.
"""

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
#from trainmefitapp.profile_editor import get_user_profile_editor


def home(request):
    if request.user.is_authenticated():
        return redirect('/dashboard/')
    return render_to_response('index.html')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def open_dashboard(request):
    if not request.user.is_authenticated():
        return redirect('/')
    return render(request,'dashboard.html')


# This is login for admin at Admin Panel
@csrf_exempt
def admin_login(request):
    #pdb.set_trace()
    try:
        user = authenticate( username=request.POST.get('username'), password=request.POST.get('password'))
        if user is not None:
            if user.is_active:
                login(request,user)
                request.session['login_user']=user.username
                request.session['login_status']=True
                return redirect('/dashboard/') #render_to_response('dashboard.html')
            else:
                data= {'success' : 'false', ExceptionLabel.ERROR_MESSAGE:'User Is Not Active'}
        else:
            data= {'success' : 'false', ExceptionLabel.ERROR_MESSAGE:'Invalid Username or Password'}
    except User.DoesNotExist:
        data= {'success' : 'false', ExceptionLabel.ERROR_MESSAGE:'User Not Exit'}
    except MySQLdb.OperationalError, e:
        print 'DB :',e
        data= {'success' : 'false', ExceptionLabel.ERROR_MESSAGE:'Internal Server Error '}
    except Exception, e:
        print 'BIG :',e
        data= {'success' : 'false', ExceptionLabel.ERROR_MESSAGE:'Internal Server Error '}
    return render_to_response('index.html', {'errors':data})


# This API to login end user through app or website.
# returns the User Status as success=true, success=false
@csrf_exempt
def user_login(request):
    #pdb.set_trace()
    try:
        if request.method == 'POST':
            json_obj=json.loads(request.body)
            print 'JSON OBJECT : ',json_obj
            user = authenticate(username=json_obj['username'], password= json_obj['password'])
            
            if user is not None:
                if user.is_active:
                    login(request,user)
                    data= {'success' : 'true', ExceptionLabel.ERROR_MESSAGE:'Successfully Login'}# 'user_info':get_user_profile_editor(user_id)}
                    
                else:
                    data= {'success' : 'false', ExceptionLabel.ERROR_MESSAGE:'User Is Not Active'}
            else:
                data= {'success' : 'false', ExceptionLabel.ERROR_MESSAGE:'Invalid Username or Password'}
        else:
            data= {'success' : 'false', ExceptionLabel.ERROR_MESSAGE:'Invalid Request'}
    except User.DoesNotExist:
        data= {'success' : 'false', ExceptionLabel.ERROR_MESSAGE:'User Not Exit'}
    except MySQLdb.OperationalError, e:
        data= {'success' : 'false', ExceptionLabel.ERROR_MESSAGE:'Internal Server Error '}
    except Exception, e:
        data= {'success' : 'false', ExceptionLabel.ERROR_MESSAGE:'Internal Server Error '}
    return HttpResponse(json.dumps(data), content_type='application/json')

# This is Sign Up from mobile and web
@csrf_exempt
def sign_up_end_user(request):
   # pdb.set_trace()
    try:
        print request
        if request.method == 'POST':
            json_obj=json.loads(request.body)
            _user_name  = json_obj[AppUserConstants.USER_NAME]
            password  = json_obj[AppUserConstants.PASS_WORD]
            _sign_up_via= json_obj[AppUserConstants.SIGN_UP_VIA]
            _first_name = json_obj[AppUserConstants.FIRST_NAME]
            _user_nick_name   = json_obj[AppUserConstants.USER_NICK_NAME]
            _email_id   = json_obj[AppUserConstants.USER_NAME]
            _sign_up_source = json_obj[AppUserConstants.SIGN_UP_SOURCE]
            _user_profile_image=json_obj[AppUserConstants.USER_PROFILE_IMAGE]
            _last_name=json_obj[AppUserConstants.LAST_NAME]
            _apns_token=json_obj[AppUserConstants.APNS_TOKEN]
            _user_full_name=json_obj[AppUserConstants.USER_FULL_NAME]

            
            user_obj = UserProfile(
                username   = _user_name,
                sign_up_via = _sign_up_via,
                first_name  = _first_name,
                last_name   = _last_name,
                user_full_name   = _user_full_name,
                email    = _email_id,
                user_nick_name=_user_nick_name,
                sign_up_source = _sign_up_source,
                user_profile_image=_user_profile_image
            )
            user_obj.save()
            user_obj.set_password(password)
            user_obj.save()
            data = { ExceptionLabel.SUCCESS : 'true','user_id':user_obj.id}
        else:
            data = { ExceptionLabel.SUCCESS : 'false', ExceptionLabel.ERROR_MESSAGE : 'Invalid Request' }
            print 'hello'
    except Exception, e:
        print 'exception hello',e
        data = { ExceptionLabel.SUCCESS : 'false', ExceptionLabel.ERROR_MESSAGE : 'Invalid Request' }
    return HttpResponse(json.dumps(data), content_type='application/json')

# log out the user
def signOutAdmin(request):
    logout(request)
    return redirect('home')

def signOutUser(request):
    logout(request)
    data = { ExceptionLabel.SUCCESS : 'true'}
    return HttpResponse(json.dumps(data), content_type='application/json')

def user_page(request):
    return render(request,'customers.html')


def user_details_page(request):
    return render_to_response('customer-profile.html')

def add_user_details(request):
    """
    This function will get called from mobile and web site. 
    This will store all the information of user
    """
    try:
        if request.method == 'POST':
            json_obj=json.loads(request.body)
            
            userprofileimage        = json_obj[AppUserConstants.USER_PROFILE_IMAGE]
            usernickname            = json_obj[AppUserConstants.USER_NICK_NAME]
            userfullname            = json_obj[AppUserConstants.USER_FULL_NAME]
            signupvia               = json_obj[AppUserConstants.SIGN_UP_VIA]
            usersecondaryemail      = json_obj[AppUserConstants.USER_SECONDARY_EMAIL]
            userprimarycontact      = json_obj[AppUserConstants.USER_PRIMARY_CONTACT]
            usersecondarycontact    = json_obj[AppUserConstants.USER_SECONDARY_CONTACT]
            usercity                = json_obj[AppUserConstants.USER_CITY]
            userstate               = json_obj[AppUserConstants.USER_STATE]
            usercountry             = json_obj[AppUserConstants.USER_COUNTRY]
            usergender              = json_obj[AppUserConstants.USER_GENDER]
            userage                 = json_obj[AppUserConstants.USER_AGE]
            userheight              = json_obj[AppUserConstants.USER_HEIGHT]
            userweight              = json_obj[AppUserConstants.USER_WEIGHT]
            isgeneralfitness        = json_obj[AppUserConstants.IS_GENERAL_FITNESS]
            ismusclegain            = json_obj[AppUserConstants.IS_MUSCLE_GAIN]
            isweightloss            = json_obj[AppUserConstants.IS_WEIGHT_LOSS]
            isimprovedstamina       = json_obj[AppUserConstants.IS_IMPROVED_STAMINA]
            isgymaccess             = json_obj[AppUserConstants.IS_GYM_ACCESS]
            howmanytimesperweek     = json_obj[AppUserConstants.HOW_MANY_TIMES_PER_WEEK]
            usermembershiptype      = json_obj[AppUserConstants.USER_MEMBERSHIP_TYPE]
            legpressweightlift      = json_obj[AppUserConstants.LEG_PRESS_WEIGHT_LIFT]
            benchpressweightlift    = json_obj[AppUserConstants.BENCH_PRESS_WEIGHT_LIFT]
            bicepCurlsWeightLift    = json_obj[AppUserConstants.BICEP_CURLS_WEIGHT_LIFT]
            
            # Create User Profile Object
            user_obj = UserProfile(
                user_profile_image =    userprofileimage,
                user_nick_name  =   usernickname,
                user_full_name  =   userfullname,
                sign_up_via     =   signupvia,
                user_secondary_email    =   usersecondaryemail  ,
                user_primary_contact    =   userprimarycontact  ,
                user_secondary_contact  =   usersecondarycontact,
                user_city   =   usercity,
                user_state  =   userstate,
                user_country    =   usercountry,
                user_gender =   usergender,
                user_age    =   userage,
                user_height =   userheight,
                user_weight =   userweight,
                is_general_fitness  =   isgeneralfitness,
                is_muscle_gain  =   ismusclegain,
                is_weight_loss  =   isweightloss,
                is_improved_stamina =   isimprovedstamina,
                is_gym_access   =   isgymaccess ,
                how_many_times_per_week =   howmanytimesperweek ,
                user_membership_type    =   usermembershiptype  ,
                leg_press_weight_lift   =   legpressweightlift  ,
                bench_press_weight_lift =   benchpressweightlift,
                bicep_curls_weight_lift =   bicepCurlsWeightLift
            )
            # save object
            # return profile object
        else:
            print 'hello'
    except Exception, e:
        print 'exception hello'
        

def forgot_password(request):
    return render_to_response('forgotpassword.html')    


##                AppUserConstants.USER_PROFILE_IMAGE =userprofileimage,
##                AppUserConstants.USER_NICK_NAME=usernickname,
##                AppUserConstants.USER_FULL_NAME=userfullname,
##                AppUserConstants.SIGN_UP_VIA=signupvia,
##                AppUserConstants.USER_SECONDARY_EMAIL=usersecondaryemail  ,
##                AppUserConstants.USER_PRIMARY_CONTACT=userprimarycontact  ,
##                AppUserConstants.USER_SECONDARY_CONTACT=usersecondarycontact,
##                AppUserConstants.USER_CITY=usercity,
##                AppUserConstants.USER_STATE=userstate,
##                AppUserConstants.USER_COUNTRY=usercountry,
##                AppUserConstants.USER_GENDER=usergender,
##                AppUserConstants.USER_AGE=userage,
##                AppUserConstants.USER_HEIGHT=userheight,
##                AppUserConstants.USER_WEIGHT=userweight,
##                AppUserConstants.IS_GENERAL_FITNESS=isgeneralfitness,
##                AppUserConstants.IS_MUSCLE_GAIN=ismusclegain,
##                AppUserConstants.IS_WEIGHT_LOSS=isweightloss,
##                AppUserConstants.IS_IMPROVED_STAMINA=isimprovedstamina,
##                AppUserConstants.IS_GYM_ACCESS=isgymaccess ,
##                AppUserConstants.HOW_MANY_TIMES_PER_WEEK=howmanytimesperweek ,
##                AppUserConstants.USER_MEMBERSHIP_TYPE=usermembershiptype  ,
##                AppUserConstants.LEG_PRESS_WEIGHT_LIFT=legpressweightlift  ,
##                AppUserConstants.BENCH_PRESS_WEIGHT_LIFT=benchpressweightlift,
##                AppUserConstants.BICEP_CURLS_WEIGHT_LIFT=bicepCurlsWeightLift
