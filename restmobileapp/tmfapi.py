
from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.
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
import MySQLdb, sys
from django.db import transaction
import csv
import json
from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist
from django.utils.datastructures import MultiValueDictKeyError
import datetime
import time
from datetime import date, timedelta
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from trainmefitapp.views.constants import ExceptionMessages, ExceptionLabel
from trainmefitapp.models import * 
from datetime import date
from django.core.files.base import ContentFile
import smtplib
import urllib
import os
from trainmefit_project import settings



server='http://192.168.0.123:8008'

RESET_URL = 'http://192.168.0.123:9800/forget-pwd/?user_id='



@csrf_exempt
def mobile_login(request):
    # pdb.set_trace()
    try:
        if request.method == 'POST':
            json_obj=json.loads(request.body)
            user = authenticate(username=json_obj['username'], password= json_obj['password'])
            if user is not None:
                if user.is_active:
                    data= {'success' : 'true','myprofileinfo' :get_myprofile(json_obj['username']), ExceptionLabel.ERROR_MESSAGE:'Successfully Login' }
                else:
                    data= {'success' : 'false', ExceptionLabel.ERROR_MESSAGE:'User Is Not Active'}
            else:
                data= {'success' : 'false', ExceptionLabel.ERROR_MESSAGE:'Invalid Username or Password'}
        else:
            data= {'success' : 'false', ExceptionLabel.ERROR_MESSAGE:'Invalid Request'}
    except User.DoesNotExist:
        print 'usr'
        data= {'success' : 'false', ExceptionLabel.ERROR_MESSAGE:'User Not Exist'}
    except MySQLdb.OperationalError, e:
        print e
        data= {'success' : 'false', ExceptionLabel.ERROR_MESSAGE:'Internal Server Error '}
    except Exception, e:
        print e
        data= {'success' : 'false', ExceptionLabel.ERROR_MESSAGE:'Internal Server Error '}
    return HttpResponse(json.dumps(data), content_type='application/json')


@csrf_exempt
def sign_up(request):
    print "in the sign_up"
    # pdb.set_trace()
    try:
        json_obj=json.loads(request.body)
        user_obj = UserProfile(
            username                                = json_obj['email_id'],
            user_phone_number                       = json_obj['phoneno'],
            user_membership_id                      = get_membership(json_obj['membership']) ,
            email                                   = json_obj['email_id'],
            user_id                                 = json_obj['email_id'],
            user_first_name                         = json_obj['first_name'],
            user_last_name                          = json_obj['last_name'],
            user_objective_id                       = get_objective(json_obj['objective']),
            user_gym_access                         = json_obj['is_gym_access'],
            user_gender                             = json_obj['gender'],
            user_dob                                = datetime.datetime.strptime(json_obj['dob'],'%d-%m-%Y').date(),
            user_height                             = json_obj['height'],
            user_weight                             = json_obj['weight'],
            user_profile_picture                    = save_image(json_obj['user_profile_image']),
            user_created_date                        = datetime.datetime.now(),
            user_leg_press_weight_lift               = json_obj['leg_press'],
            user_bench_press_weight_lift             = json_obj['bench_press'],
            user_bicep_curls_weight_lift             = json_obj['bicep_curls'],
            user_workouts_per_week                   = json_obj['workouts_per_week'],
            user_workout_intensity                   = json_obj['workout_intensity']
        )    
        user_obj.save()
        user_obj.set_password(json_obj['password'])
        user_obj.save()
        send_admin_notification(user_obj)
        print user_obj
        if user_obj:
            data= {'success' : 'true', ExceptionLabel.ERROR_MESSAGE:'Successfully Sign Up','email_id':user_obj.username }
        else:
            data= {'success' : 'false', ExceptionLabel.ERROR_MESSAGE:'Not Sign Up Successfully'}
    except UserProfile.DoesNotExist,e:
        data= {'success' : 'false', 'message':str(e)}
    except Exception, e:
        print e
        data= {'success' : 'false', ExceptionLabel.ERROR_MESSAGE:'User Already Exist '}
    return HttpResponse(json.dumps(data), content_type='application/json')


def get_membership(membership_type):
    membership_obj=MembershipMaster.objects.get(membership_type=membership_type)
    return membership_obj



def get_objective(objective_name):
    objective_obj=ObjectiveMaster.objects.get(objective_name=objective_name)
    return objective_obj


def save_image(imgdata):
    import os
    print "save_image"
    # pdb.set_trace()
    try:
        filename = "uploaded_image%s.png" % str(datetime.datetime.now()).replace('.','_')
        decoded_image = imgdata.decode('base64')
        return ContentFile(decoded_image, filename)

    except Exception, e:
        print e
        data = {'data': None, ExceptionLabel.ERROR_MESSAGE:'Server Error - Please Try Again'}
        return False         
    
def send_admin_notification(user_obj):
    # print "in the send_password_reset_mail"
    #pdb.set_trace()
    gmail_user = "mohit.trainmefit@gmail.com"
    gmail_pwd = "tmf@123!"
    FROM = 'TrainMeFitApp'
    TO = ['mohit.trainmefit@gmail.com']


    try:
        TO.append(user_obj.username)
        TEXT="""User Name: %s \nPhone No: %s\nMembership: %s\nObjective:%s \nGender :%s\nDate Of Birth :%s\nHeight :%s\nWeight :%s\nGym Access :%s\n
           """%(str(user_obj.username),str(user_obj.user_phone_number),str(user_obj.user_membership_id.membership_type), str(user_obj.user_objective_id.objective_name),str(user_obj.user_gender),str(user_obj.user_dob.strftime('%d-%m-%Y')),str(user_obj.user_height),str(user_obj.user_weight),str(user_obj.user_gym_access))
        SUBJECT = "Notification For Customer Registration"
        server = smtplib.SMTP("smtp.gmail.com", 587) #or port 465 doesn't seem to work!
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_pwd)
        message = """From: %s\nTo: %s\nSubject: %s\n\n%s """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
        server.sendmail(FROM, TO, message)
        server.close()          
        data = {'success': 'true', 'message' : "Forgot Password Send Successfully" }

    except UserProfile.DoesNotExist, e:
        data = {'success': 'false', 'message':"Forgot Password Failed"}
        print "failed to send mail", e
    except Exception, e:
        print e
        data = {'success': 'false', 'message':"Server Error, Please try again!"}
    return HttpResponse(json.dumps(data), content_type='application/json')

@csrf_exempt
# @transaction.atomic
def google_sign_up(request):
    print 'Request Body : ',request.body
    # sid = transaction.savepoint()
    try:
        json_obj=json.loads(request.body)
        user_obj = UserProfile.objects.get(username=json_obj['email_id'])
        if user_obj:
            data = {'success': 'true', 'error_message':'User Already Sign Up with this Username' }
    except Exception,e:
        print e
        data = {'success': 'false', 'error_message':'Failed to save user details'}
    return HttpResponse(json.dumps(data), content_type='application/json')

@csrf_exempt
def edit_profile(request):
    try:
        if request.method == 'POST':
            json_obj=json.loads(request.body)
            user_id = json_obj['email_id']
            user_obj                            = UserProfile.objects.get(username=user_id)
            user_obj.user_first_name            = json_obj['first_name']
            user_obj.user_last_name             = json_obj['last_name']
            user_obj.user_objective_id          = get_objective(json_obj['objective'])
            user_obj.user_gym_access            = json_obj['is_gym_access']
            user_obj.user_gender                = json_obj['gender']
            user_obj.user_dob                   = datetime.datetime.strptime(json_obj['dob'],'%d-%m-%Y').date()
            user_obj.user_height                = json_obj['height']
            user_obj.user_weight                = json_obj['weight']
            user_obj.user_profile_picture       = save_image(json_obj['user_profile_image'])
            user_obj.user_phone_number          = json_obj['phoneno']
            # user_obj.validate_profile(user_obj)
            user_obj.save()
            print "done"
        if user_obj:
            data= {'success' : 'true', ExceptionLabel.ERROR_MESSAGE:'Profile Updated Successfully','user_profile_image':server+user_obj.user_profile_picture.url }
        else:
            data= {'success' : 'false', ExceptionLabel.ERROR_MESSAGE:'Profile Not Updated Successfully'}

    except UserProfile.DoesNotExist,e:
        data= {'success' : 'false', 'message':str(e)}
    except Exception, e:
        print e
        data= {'success' : 'false', ExceptionLabel.ERROR_MESSAGE:'Internal Server Error '}
    return HttpResponse(json.dumps(data), content_type='application/json')

def check_program_status(email_id):
    print "here------------------------"
    status =''
    try:
        user_program_obj = UserProgramMap.objects.filter(user_id=UserProfile.objects.get(username=email_id),user_program_program_status='Active')
        if user_program_obj:
            print user_program_obj
            status='yes'
    except Exception, e:
        status='no'
        print e
        data = {'data': None, ExceptionLabel.ERROR_MESSAGE:'Server Error - Please Try Again'}
    print status
    return status




# @csrf_exempt
def get_myprofile(email_id):
    print "in the request.POST.get('username')"
    # pdb.set_trace()
    try:
        user_obj = UserProfile.objects.get(username=email_id)
        temp = {
            'first_name':user_obj.user_first_name,       
            'last_name':user_obj.user_last_name,        
            'user_objective':user_obj.user_objective_id.objective_name,
            'gym_access':user_obj.user_gym_access,
            'user_gender':user_obj.user_gender,
            'user_dob':user_obj.user_dob.strftime('%d-%m-%Y'),
            'user_height':user_obj.user_height,
            'user_weight':user_obj.user_weight,
            'user_email':user_obj.email,
            'user_phoneNo':user_obj.user_phone_number,
            'user_profile_image':server+user_obj.user_profile_picture.url,
            'program_status':check_program_status(email_id)  
        }
        data = { 'data': temp }
        
    except Exception, e:
        print e
        data = {'data': None, ExceptionLabel.ERROR_MESSAGE:'Server Error - Please Try Again'}
    return data 


@csrf_exempt
def save_user_workout_info(request):

    json_obj=json.loads(request.body)
    user_id = json_obj['email_id']
    try:
        if request.method == 'POST':
            user_obj                                          = UserProfile.objects.get(username=user_id)
            user_obj.user_leg_press_weight_lift               = json_obj['leg_press']
            user_obj.user_bench_press_weight_lift             = json_obj['bench_press']
            user_obj.user_bicep_curls_weight_lift             = json_obj['bicep_curls']
            user_obj.user_workouts_per_week                   = json_obj['workouts_per_week']
            user_obj.user_workout_intensity                   = json_obj['workout_intensity']
            
            user_obj.save()

            print "done"
        if user_obj:
            data= {'success' : 'true', ExceptionLabel.ERROR_MESSAGE:'Workout Information Saved Successfully' }
        else:
            data= {'success' : 'false', ExceptionLabel.ERROR_MESSAGE:'Workout Information Not Saved Successfully'}
    except Exception, e:
        print e
        data= {'success' : 'false', ExceptionLabel.ERROR_MESSAGE:'Internal Server Error '}
    return HttpResponse(json.dumps(data), content_type='application/json')

def get_user_workout_info(request):
    # pdb.set_trace()
    try:
        user_id = request.GET.get('email_id')
        user_obj = UserProfile.objects.get(username=user_id)
        res_list=[]
        temp = {
            'leg_press_weight_lift':user_obj.user_leg_press_weight_lift,
            'bench_press_weight_lift':user_obj.user_bench_press_weight_lift,
            'bicep_curls_weight_lift':user_obj.user_bicep_curls_weight_lift,
            'workouts_per_week':user_obj.user_workouts_per_week,
            'workout_intensity':user_obj.user_workout_intensity,
            
        }
        
        res_list.append(temp)
        data = { 'data': temp }
        
    except Exception, e:
        print e
        data = {'data': None, ExceptionLabel.ERROR_MESSAGE:'Server Error - Please Try Again'}
    return HttpResponse(json.dumps(data), content_type='application/json')


def get_sample_workout(request):
    print "in the get_sample_workout"
    # pdb.set_trace()
    try:
        # user_id = request.GET.get('email_id')
        sample_work_obj = Workout.objects.filter(workout_type='Sample',workout_status='Active')
        res_list=[]
        for sample_work in sample_work_obj:
            temp_obj= {

                'workout_name': sample_work.workout_name,
                'workout_id': sample_work.workout_id,
                'workout_type':'Sample'
            }
            res_list.append(temp_obj)
        data = {'data': res_list}

    except Exception, e:
        print e
        data = {'data': None, ExceptionLabel.ERROR_MESSAGE:'Server Error - Please Try Again'}
    return HttpResponse(json.dumps(data), content_type='application/json')  




def get_workout_schedule(request):
    print "get sample myworkout"
    # pdb.set_trace()
    try:
        day_dict={'monday':'',
                 'tuesday':'',
                 'wednesday':'',
                 'thursday':'',
                 'friday':'',
                 'saturday':'',
                 'sunday':''
            }
        res_list=[]
        user_id = request.GET.get('email_id')
        print user_id
        user_program_obj = UserProgramMap.objects.get(user_id=UserProfile.objects.get(username=user_id),user_program_program_status='Active')
        if user_program_obj:
            for day in day_dict:
                day_details=check_workout_for_day(user_program_obj,day)
                print "day_details"
                print day_details
                if day_details:
                    temp_obj= {
                    'workout_day':day , 
                    'workout_name':day_details['name'],
                    'workout_id':day_details['id'],
                    'workout_type':'Normal',
                    }
                else:
                    temp_obj= {
                    'workout_day': day,
                    'workout_name':'RestDay',
                    'workout_type':'RestDay',
                    'workout_id':str(get_challenges_workout())
                    }
                res_list.append(temp_obj)
        data = {'data': res_list*4,'start_date':str(user_program_obj.user_program_start_date.strftime('%d/%m/%Y'))}
    except Exception, e:
        print e
        data = {'data': None, ExceptionLabel.ERROR_MESSAGE:'Server Error - Please Try Again'}
    return HttpResponse(json.dumps(data), content_type='application/json')          

def check_workout_for_day(user_program_obj,day):
    try:
        program_work_obj = UserProgramWorkoutMaster.objects.get(user_program_id=user_program_obj,user_program_workout_day=day)
        if program_work_obj:
            result={
            'name':program_work_obj.user_program_workout_name,
            'id':program_work_obj.workout_id.workout_id
            }
            return result
    except Exception, e:
        print e
        return False


def get_exercise_details(request):
    print "get_exercise_details"
    # pdb.set_trace()
    try:
        res_list=[]
        video_url=''
        user_program_obj = UserProgramMap.objects.get(user_id=UserProfile.objects.get(username=request.GET.get('email_id')),user_program_program_status='Active')
        if user_program_obj:
            program_work_obj = UserProgramWorkoutMaster.objects.filter(user_program_id=user_program_obj,workout_id=Workout.objects.get(workout_id=request.GET.get('workout_id')))
            if program_work_obj:
                for program_work in program_work_obj:
                    print program_work
                    program_exe_obj=UserProgramExerciseMap.objects.filter(user_program_workout_id=program_work.user_program_workout_id)
                    print "program_exe_obj=================="
                    print program_exe_obj
                    if program_exe_obj:
                        for program_exe in program_exe_obj:
                            instructions=[]
                            images=[]
                            print program_exe.user_program_exercise_name
                            image_obj=ExcerciseImage.objects.filter(exercise_id=program_exe.exercise_id)
                            if image_obj:
                                for img in image_obj:
                                    images.append(server+img.exercise_image.url)
                            instructions_obj=InstructionMaster.objects.filter(instruction_exercise_id=program_exe.exercise_id)
                            if instructions_obj:
                                for inst in instructions_obj:
                                    instructions.append(inst.instruction_name)
                            print 'program_exe.user_program_exercise_video_id'
                            print program_exe.user_program_exercise_video_id
                            # video=ExcerciseVideo.objects.get(exercise_video_id=program_exe.user_program_exercise_video_id)
                            # print "video"
                            # if video:
                            #     print video.exercise_video_url.url
                            #     video_url=video.exercise_video_url.url

                            temp ={
                                # 'workout_name' : program_work.user_program_workout_name,
                                'exercise_name':program_exe.user_program_exercise_name,
                                'exercise_id':program_exe.exercise_id,
                                'exercise_time':program_exe.user_program_exercise_time,
                                'exercise_instructions':instructions,
                                'exercise_images':images,
                                'exercise_video':server+video_url
                                }
                            instructions=[]
                       
                                # print instructions
                            
                            res_list.append(temp)
        data = {'data': res_list}

    except Exception, e:
        print e
        data = {'data': None, ExceptionLabel.ERROR_MESSAGE:'Server Error - Please Try Again'}
    return HttpResponse(json.dumps(data), content_type='application/json')


def get_rest_exercise_details(request):
    print "get_rest_exercise_details"
    # pdb.set_trace()
    video_url=''
    try:
        res_list=[]
        workout_exe_obj=WorkoutExerciseMap.objects.filter(workout_id=Workout.objects.get(workout_id=request.GET.get('workout_id')))
        if workout_exe_obj:
            for workout_exe in workout_exe_obj:
                instructions=[]
                images=[]
                image_obj=ExcerciseImage.objects.filter(exercise_id=workout_exe.exercise_id)
                if image_obj:
                    for img in image_obj:
                        images.append(server+img.exercise_image.url)
                instructions_obj=InstructionMaster.objects.filter(instruction_exercise_id=workout_exe.exercise_id)
                if instructions_obj:
                    for inst in instructions_obj:
                        instructions.append(inst.instruction_name)
                temp ={
                    'exercise_name':workout_exe.exercise_id.exercise_name,
                    'exercise_id':workout_exe.exercise_id.exercise_id,
                    'exercise_time':workout_exe.exercise_id.exercise_time,
                    'exercise_instructions':instructions,
                    'exercise_images':images,
                    'exercise_video':server+video_url
                    }
                res_list.append(temp)
                
        data = {'data': res_list}
    except Exception, e:
        print e
        data = {'data': None, ExceptionLabel.ERROR_MESSAGE:'Server Error - Please Try Again'}
    return HttpResponse(json.dumps(data), content_type='application/json')



def get_workout_of_day(request):
    # print "get_workout_of_day"
    # pdb.set_trace()
    try:
        user_id = request.GET.get('email_id')
        print user_id
        res_list=[]
        user_program_obj = UserProgramMap.objects.get(user_id=UserProfile.objects.get(username=user_id),user_program_program_status='Active')
        if user_program_obj:
            program_work_obj = UserProgramWorkoutMaster.objects.filter(user_program_id=user_program_obj,user_program_workout_day=request.GET.get('day'))
            if program_work_obj:
                for obj in program_work_obj:
                    if obj:
                        temp = {
                            'workout_name' :str(obj.user_program_workout_name),
                            'workout_id' : obj.workout_id.workout_id
                        }
                    res_list.append(temp)
            else:
                temp = {
                        'workout_name' :'RestDay',
                        'workout_id' :str(get_challenges_workout())
                    }
                res_list.append(temp)
        data = {'data': res_list}

    except Exception, e:
        print e
        data = {'data': 'RestDay', ExceptionLabel.ERROR_MESSAGE:'Server Error - Please Try Again'}
    return HttpResponse(json.dumps(data), content_type='application/json')        

def get_challenges_workout():
    rest_workouts = Workout.objects.filter(workout_type='Challenge',workout_status='Active')
    if rest_workouts:
        for rest in rest_workouts:
            return rest.workout_id





# forgot password api
@csrf_exempt
def forgot_password(request):
    print "in the forgot_password"
    #pdb.set_trace()
    gmail_user = "mohit.trainmefit@gmail.com"
    gmail_pwd = "tmf@123!"
    FROM = 'TrainMeFit Admin'
    TO = ['mohit.trainmefit@gmail.com']

    try:
        if request.method == 'POST':
            json_obj=json.loads(request.body)
            user_name = json_obj['email_id']
            TO.append(user_name)
            user_obj = UserProfile.objects.get(username = json_obj['email_id'])
            # user_obj.set_password(password)
            # user_obj.save()
            print '---------password -------------',user_obj.password
            TEXT = "Your new password is" + " " + user_obj.password
            SUBJECT = "Change your Password"
            server = smtplib.SMTP("smtp.gmail.com", 587) #or port 465 doesn't seem to work!
            server.ehlo()
            server.starttls()
            server.login(gmail_user, gmail_pwd)
            message = """From: %s\nTo: %s\nSubject: %s\n\n%s """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
            server.sendmail(FROM, TO, message)
            server.close()          
            data = {'success': 'true', 'message' : "Forgot Password Send Successfully" }

    except User.DoesNotExist, e:
        data = {'success': 'false', 'message':"Forgot Password Failed"}
        print "failed to send mail", e
    except Exception, e:
        print e
        data = {'success': 'false', 'message':"Server Error, Please try again!"}
    return HttpResponse(json.dumps(data), content_type='application/json')



def get_restday_challenges(request):
    print "in the get_restday_challenges"
    # pdb.set_trace()
    try:
        user_id = request.GET.get('email_id')
        restday_obj = RestChallenges.objects.all()
        res_list=[]
        for restch in restday_obj:
            temp_obj= {
                'challenge_name': restch.rest_challenge_name,
                'workout_id': restch.workout_id
            }
            res_list.append(temp_obj)
        data = {'data': res_list}

    except Exception, e:
        print e
        data = {'data': None, ExceptionLabel.ERROR_MESSAGE:'Server Error - Please Try Again'}
    return HttpResponse(json.dumps(data), content_type='application/json')  


def send_contact_mail(request):
    print "in the forgot_password"
    #pdb.set_trace()
    gmail_user = "mohit.trainmefit@gmail.com"
    gmail_pwd = "tmf@123!"
    FROM = 'TrainMeFit Admin'
    TO = ['mohit.trainmefit@gmail.com']

    try:
        issue = request.GET.get('message')
        print issue

        user_name = request.GET.get('email_id')
        print user_name

        TEXT="""User Name: %s \nQuery: %s\n
                """%(str(user_name),str(issue))           
    
        SUBJECT = "Query"
        server = smtplib.SMTP("smtp.gmail.com", 587) #or port 465 doesn't seem to work!
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_pwd)
        message = """From: %s\nTo: %s\nSubject: %s\n\n%s """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
        server.sendmail(FROM, TO, message)
        server.close()          
        data = {'success': 'true', 'message' : "Query Sent Successfully" }

    except User.DoesNotExist, e:
        data = {'success': 'false', 'message':"Query not Sent Successfully"}
        print "failed to send mail", e
    except Exception, e:
        print e
        data = {'success': 'false', 'message':"Server Error, Please try again!"}
    return HttpResponse(json.dumps(data), content_type='application/json')



@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def redirect_to_reset_password_page(request):
    print "in the redirect_to_reset_password_page"
    try:
        # user_id=UserProfile.objects.get(username=request.GET.get('email_id'))
        print "request"
        print request.GET.get('user_id')

        print 'I am in page'
        data = {'hello':'Hello How are You..!','user_id':request.GET.get('user_id')}
    except MySQLdb.OperationalError, e:
        data = {'success': 'false', 'error_message' : 'Failed To Update the profile pic on server'}
    #return HttpResponse(json.dumps(data), content_type='application/json')
    return render(request,'forgotpassword.html',data) 



# This is for reset the password through link
@csrf_exempt
def update_new_password(request):
    print "in tyhe  update_new_password "
    print request.POST
    try:
        user_id = request.POST.get('user_id')
        print user_id
        user_obj   = UserProfile.objects.get(id=user_id)
        confirm_password    = request.POST.get('confirm_password')
        new_password        = request.POST.get('new_password')
        print user_obj
        if new_password == confirm_password:
            user_obj.set_password(new_password)
            user_obj.save()
            print 'done'
            data = {'success': 'true','error_message': 'Thank you.Your password has been reseted.'}
            return redirect('/')
        else:
            data = {'success': 'false', 'error_message': 'Password Should be same'}
    except UserProfile.DoesNotExist, e:
        print e
        data = {'success': 'false', 'message':"User Not Found, Please try another one or Sign Up!"}
    except MySQLdb.OperationalError, e:
        data = {'success': 'false', 'error_message' : 'Failed To Update the profile pic on server'}
    return HttpResponse(json.dumps(data), content_type='application/json')


# @csrf_exempt    
def send_password_reset_mail(request):
    print "in the send_password_reset_mail"
    #pdb.set_trace()
    gmail_user = "mohit.trainmefit@gmail.com"
    gmail_pwd = "tmf@123!"
    FROM = 'TrainMeFit Admin'
    TO = ['mohit.trainmefit@gmail.com']


    try:
        email = request.GET.get('email_id')
        user_id=UserProfile.objects.get(username=email)
        print user_id.id
        TO.append(email)
        
        TEXT=RESET_URL + str(user_id.id)+ '&test_cam_test=RqhFbyMweTJzpdU8EEq73W'
        SUBJECT = "Reset Password Link"
        server = smtplib.SMTP("smtp.gmail.com", 587) #or port 465 doesn't seem to work!
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_pwd)
        message = """From: %s\nTo: %s\nSubject: %s\n\n%s """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
        server.sendmail(FROM, TO, message)
        server.close()          
        data = {'success': 'true', 'message' : "Reset password Sent Successfully" }

    except UserProfile.DoesNotExist, e:
        data = {'success': 'false', 'message':"Forgot Password Failed"}
        print "failed to send mail", e
    except Exception, e:
        print e
        data = {'success': 'false', 'message':"Server Error, Please try again!"}
    return HttpResponse(json.dumps(data), content_type='application/json')

