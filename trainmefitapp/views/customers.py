from django.shortcuts import render
from django.shortcuts import render_to_response
from datetime import datetime
from datetime import date
from django.contrib.auth.models import User
from time import gmtime, strftime
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.db.models import Sum
from django.shortcuts import redirect
import pdb
import json

##import datetime
import time
from django.db import IntegrityError

from constants import AppUserConstants, ExceptionLabel
from trainmefitapp.models import *


USER_PROFILE_PIC='http://192.168.0.123:8008'
#USER_PROFILE_PIC='http://ec2-54-186-1-226.us-west-2.compute.amazonaws.com'

# TO GET THE CUSTOMER LIST  
def get_customer_list(request):
    try:        
        print 'Customer List '
        customer_list = UserProfile.objects.all()
        user_list = []
        for customer in customer_list:
               
            view =   '<a href="/user-detail-page/?user_id='+ str(customer.id)  +'" class="table-link"> '+ '<span class="fa-stack">' + '<i class="fa fa-square fa-stack-2x"></i> <i class="fa fa-search-plus fa-stack-1x fa-inverse"></i> </span> </a>'
            edit = '<a href="/user-detail-page/?user_id='+  str(customer.id)  +'" class="table-link"> '+ '<span class="fa-stack">' + '<i class="fa fa-square fa-stack-2x"></i> <i class="fa fa-search-plus fa-stack-1x fa-inverse"></i> </span> </a>'
            
            temp_obj= {
                'user_first_name': customer.user_first_name or ' ',               
                'email': check_value(customer.username) or ' ',
                'objective': check_value(customer.user_objective_id.objective_name),
                'created_date': check_date_value(customer.user_created_date),
                'status':customer.user_status or ' ',                 
                'view' : edit
            }
            user_list.append(temp_obj)
        data = {'data': user_list}
        
    except Exception, e:
        print 'Exception : ', e
        data = {'data':'none'}        
    return HttpResponse(json.dumps(data), content_type='application/json') 
    
    
# TO GET THE CUSTOMER DETAILS     
def user_details_page(request): 
    print request.GET.get('user_id')
    #pdb.set_trace()
    try:
        custom_obj = UserProfile.objects.get(id=request.GET.get('user_id'))
        print custom_obj
        customer_programs=UserProgramMap.objects.filter(user_id=custom_obj)
        customer_program_details=[] 
        
        for customer_program in customer_programs: 
            total_workout=UserProgramWorkoutMaster.objects.filter(user_program_id=customer_program).count()            
            total_exercises=UserProgramWorkoutMaster.objects.filter(user_program_id=customer_program).aggregate(Sum('user_program_workout_total_execise'))
                  
            customer_program_details.append({'user_program_id':customer_program.user_program_id,          
                                            'user_id':customer_program.user_id,
                                            'program_id':customer_program.program_id,
                                            'program_name':customer_program.user_program_name, 
                                            'total_workout':total_workout,
                                            'start_date':check_date_value(customer_program.user_program_start_date),
                                            'end_date':check_date_value(customer_program.user_program_end_date),
                                           # 'total_exercises': int(total_exercises['user_program_workout_total_execise__sum']),
                                            'status':customer_program.user_program_program_status,
                                            'updated_date':check_date_value(customer_program.user_program_updated_date),
                                            'days':'28',
                                         
            })
       
        memeber_since=check_value(custom_obj.user_created_date).strftime('%b,%Y')
        profile_pic=USER_PROFILE_PIC+custom_obj.user_profile_picture.url
        print '----------------------------------------'
        print profile_pic
        data={
                'success':'true',
                'first_name': check_value(custom_obj.user_first_name),
                'cust_image':custom_obj.user_profile_picture,
                'last_name': check_value(custom_obj.user_last_name),
                'email':check_value(custom_obj.user_id),
                'phone_number':check_value(custom_obj.user_phone_number),
                'dob':check_date_value(custom_obj.user_dob),
                'gender':check_value(custom_obj.user_gender),
                'bench_press':check_value(custom_obj.user_bench_press_weight_lift),
                'bicep_curl':check_value(custom_obj.user_bicep_curls_weight_lift),
                'legt_press':check_value(custom_obj.user_leg_press_weight_lift),
                'wt_in_kg':check_value(custom_obj.user_weight),
                'gym_access':check_value(custom_obj.user_gym_access),
                'objective':check_value(custom_obj.user_objective_id),
                'wrkt_per_week':check_value(custom_obj.user_workouts_per_week),
                'intensity':check_value(custom_obj.user_workout_intensity),
                'height':check_value(custom_obj.user_height), 
                'membership':check_value(custom_obj.user_membership_id), 
                'memeber_since':memeber_since,
                'profile_pic':profile_pic,
                'cutomer_program_list':customer_program_details                          
            }        
        # TO GET THE MASTER PROGRAM LIST     
        data1 = { 'success':'true', 'program_list':get_customer_programs()} 
        data.update(data1)   
          
    except Exception,e:
        print 'Exception ',e
        data = {'success':'false'}
    return render(request,'customer-profile.html',data)

def check_value(value_str): 
    if value_str:
        return value_str    
    else:
        return '-------'
        
def check_date_value(value_str): 
    if value_str:
        return value_str.strftime('%m/%d/%y')    
    else:
        return '-------'

# TO VIEW THE CUSTOMER PROGRAM
def view_customer_program(request):
    try:   
        #pdb.set_trace()
        user_program_obj = UserProgramMap.objects.get(user_program_id = request.GET.get('user_program_id'))
        
        print user_program_obj.user_id
        custom_obj = UserProfile.objects.get(user_id=user_program_obj.user_id) 
        
        memeber_since=check_value(custom_obj.user_created_date).strftime('%b,%Y')
        profile_pic=USER_PROFILE_PIC+custom_obj.user_profile_picture.url
        
        user_info = { 
                'id':custom_obj.id,
                'user_id':custom_obj.user_id,
                'first_name': custom_obj.user_first_name,
                'last_name': custom_obj.user_last_name,
                'email':custom_obj.user_id,
                'phone_number':custom_obj.user_phone_number,
                'dob':check_date_value(custom_obj.user_dob),
                'gender':custom_obj.user_gender,
                'membership':check_value(custom_obj.user_membership_id),
                'memeber_since':memeber_since,
                'profile_pic':profile_pic,
                'wt_in_kg':check_value(custom_obj.user_weight),
                }
                
 #       program_master = ProgramMaster.objects.get(program_id=user_program_obj.program_id)
        start = user_program_obj.user_program_start_date
        end = user_program_obj.user_program_end_date
        total_day = end - start        
        
        User_Program_Workout_Master_obj = UserProgramWorkoutMaster.objects.filter(user_program_id=user_program_obj) 
        user_program_workout_list=[]
        for user_program_workout in User_Program_Workout_Master_obj:         		
            user_program_workout_list.append({
                     	'program_workout_id':user_program_workout.user_program_workout_id,
                        'workout_name':user_program_workout.user_program_workout_name,
                        'execises':user_program_workout.user_program_workout_total_execise,                        
                        'time':user_program_workout.user_program_workout_total_time,
                        'days':user_program_workout.user_program_workout_day,
                        'intensity':user_program_workout.user_program_workout_intensity
                        })        
                         
        data={
         'success':'true','user_program_id':user_program_obj.user_program_id,
         'user_program':user_program_obj,
         'user_objective':user_program_obj.program_id.program_user_objective_id,              
         'user_program_start_date':check_date_value(user_program_obj.user_program_start_date),
         'user_program_end_date':check_date_value(user_program_obj.user_program_end_date),
         'days':total_day.days+1,
         'created_by':user_program_obj.user_program_created_by,
         'updated_by':user_program_obj.user_program_updated_by,    
         'created_date':check_date_value(user_program_obj.user_program_created_date),
         'updated_date':check_date_value(user_program_obj.user_program_updated_date),
         'status':user_program_obj.user_program_program_status,
         'program_workout_list':user_program_workout_list,
         
        }
        
        data.update(user_info)
    except Exception,e:
        print 'Exception ',e	
        data = {'success':'false'}
    return render(request,'customer-program.html',data)

# TO VIEW-EDIT THE CUSTOMER PROGRAM
def view_edit_customer_program(request):
    try:   
        #pdb.set_trace()
        user_program_obj = UserProgramMap.objects.get(user_program_id = request.GET.get('user_program_id')) 
        data= view_customer_program_full_details(user_program_obj)
    except Exception,e:
        print 'Exception ',e	
        data = {'success':'false'}
    return render(request,'customer-edit-program.html',data)

#--------------------------------------------------------------------user define function------------
def view_customer_program_full_details(user_program_obj):
    try:        
        custom_obj = UserProfile.objects.get(user_id=user_program_obj.user_id) 
        memeber_since=check_value(custom_obj.user_created_date).strftime('%b,%Y')
        profile_pic=USER_PROFILE_PIC+custom_obj.user_profile_picture.url
        
        user_info = {  
                'id': custom_obj.id,   
                'user_id':custom_obj.user_id,
                'first_name': custom_obj.user_first_name,
                'last_name': custom_obj.user_last_name,
                'email':custom_obj.user_id,
                'phone_number':custom_obj.user_phone_number,
                'dob':check_date_value(custom_obj.user_dob),
                'gender':custom_obj.user_gender,
                'membership':check_value(custom_obj.user_membership_id),
                'memeber_since':memeber_since,
                'profile_pic':profile_pic,
                'wt_in_kg':check_value(custom_obj.user_weight)
                }
        
        start = user_program_obj.user_program_start_date
        end = user_program_obj.user_program_end_date
        total_day = end - start        
        
        #----------------Getting all workout ----------------------------------  
        workout_all_objs=Workout.objects.all() 
        all_workout_list=[]       
        for workot in workout_all_objs: 
        		all_workout_list.append({'workout_id':workot.workout_id,'workout_name':workot.workout_name,
        		'workout_time':workot.workout_total_time,'workout_execises':workot.workout_total_no_execise})                         
        
        User_Program_Workout_Master_obj = UserProgramWorkoutMaster.objects.filter(user_program_id=user_program_obj) 
        user_program_workout_list=[]
        for user_program_workout in User_Program_Workout_Master_obj:         		
            user_program_workout_list.append({
                     	'program_workout_id':user_program_workout.user_program_workout_id,
                        'workout_name':user_program_workout.user_program_workout_name,
                        'execises':user_program_workout.user_program_workout_total_execise,                        
                        'time':user_program_workout.user_program_workout_total_time,
                        'days':user_program_workout.user_program_workout_day,
                        'intensity':user_program_workout.user_program_workout_intensity
                        })        
                         
        data={
         'success':'true','user_program_id':user_program_obj.user_program_id,
         'user_program':user_program_obj,
         'user_objective':user_program_obj.program_id.program_user_objective_id.objective_name,              
         'user_program_start_date':str(user_program_obj.user_program_start_date.strftime('%m/%d/%Y')),
         'user_program_end_date':str(user_program_obj.user_program_end_date.strftime('%m/%d/%Y')),
         'days':total_day.days,
         'created_by':user_program_obj.user_program_created_by,
         'updated_by':user_program_obj.user_program_updated_by,    
         'created_date':check_date_value(user_program_obj.user_program_created_date),
         'updated_date':check_date_value(user_program_obj.user_program_updated_date),
         'status':user_program_obj.user_program_program_status,
         'program_workout_list':user_program_workout_list,
         'workout_list':all_workout_list      
        }        
        data.update(user_info)
    except Exception,e:
        print 'Exception ',e	
        data = {'success':'false'}
    return data






def get_workout_by_intensity_for_customer(request):
##    pdb.set_trace()
    workout_list =[]
    try:
        workout_obj=Workout.objects.filter(workout_intensity=request.GET.get('workout_intensity'))
        for workout in workout_obj:
            workout_list.append({'workout_id':workout.workout_id,'workout_name':workout.workout_name})
        data = {'workout_list': workout_list}
        print json.dumps(data)
    except Exception,e: 
        print 'Exception',e
        data = {'workout_list': workout_list}
    return HttpResponse(json.dumps(data), content_type='application/json')
    

def add_program_workout_for_customer(request): 
    #pdb.set_trace()  
    try:   
        user_program_map_obj    = UserProgramMap.objects.get(user_program_id=request.GET.get('user_program_id'))
        workout_obj    = Workout.objects.get(workout_id=request.GET.get('workout_id'))
        
        user_program_workout_master= UserProgramWorkoutMaster(user_program_id=user_program_map_obj,workout_id=workout_obj,
                                                user_program_workout_name= workout_obj.workout_name,
                                                user_program_workout_total_execise=workout_obj.workout_total_no_execise,
                                                user_program_workout_total_time=workout_obj.workout_total_time,
                                                user_program_workout_type= workout_obj.workout_type,                                                
                                                user_program_workout_day=request.GET.get('day'),
                                                user_program_workout_intensity=workout_obj.workout_intensity,                                                
                                                user_program_workout_created_date = datetime.datetime.now(),
                                                user_program_workout_updated_date = datetime.datetime.now(),
                                                user_program_workout_updated_by ='Test User',
                                                user_program_workout_created_by ='Test User')  
        user_program_workout_master.save()   
        
        workout_exercise_map_obj_list=WorkoutExerciseMap.objects.filter(workout_id=workout_obj)
        for workout_exercise_map_obj in workout_exercise_map_obj_list:
            user_prgramexercise_map= UserProgramExerciseMap(user_program_workout_id=user_program_workout_master,
                                                exercise_id=workout_exercise_map_obj.exercise_id,
                                                user_program_exercise_body_part_id=workout_exercise_map_obj.exercise_id.exercise_body_part_id,
                                                user_program_exercise_video_id=workout_exercise_map_obj.exercise_id.exercise_video_id,
                                                user_program_exercise_name=workout_exercise_map_obj.exercise_id.exercise_name,
                                                user_program_exercise_time=workout_exercise_map_obj.exercise_id.exercise_time,
                                                user_program_exercise_workout_total_sets=workout_exercise_map_obj.workout_exercise_total_sets,
                                                user_program_exercise_workout_total_reps=workout_exercise_map_obj.workout_exercise_total_reps,           
                                                user_program_exercise_workout_time_between_set=workout_exercise_map_obj.workout_exercise_time_between_set,      
                                                user_program_exercise_workout_total_time=workout_exercise_map_obj.workout_exercise_total_time,             
                                                user_program_exercise_workout_rest_time=workout_exercise_map_obj.workout_exercise_rest_time,             
                                                user_program_exercise_created_by ='Test User',                    
                                                user_program_exercise_updated_by ='Test User',                     
                                                user_program_exercise_created_date= datetime.datetime.now(),                   
                                                user_program_exercise_updated_date= datetime.datetime.now())
            user_prgramexercise_map.save()
                 
        data = { 'success':'true', 'error_message':'Successfully Added '}
    except Exception,e:
        print 'Exception : ' , e
        data = {'success':'false', 'error_message': 'Failed to add instruction in exercise' }
    return HttpResponse(json.dumps(data), content_type='application/json')


def delete_program_workout_for_customer(request):
##    pdb.set_trace()
    try:
        print request.GET.get('user_program_workout_id')
        user_program_workout_master= UserProgramWorkoutMaster.objects.get(user_program_workout_id = request.GET.get('user_program_workout_id'))  
        user_program_workout_master.delete()
        
        data = {'success':'true'}
    except Exception,e:
        print 'Exception ',e    
        data = {'success':'true'}
    return HttpResponse(json.dumps(data), content_type='application/json') 


def customer_program(request):
    return render('customer-program.html')

# TO GET THE CUSTOMER EDIT PROGRAM PAGE
def customer_edit_program(request):
    return render(request,'customer-edit-program.html')

def get_customer_programs():
##   
    try:
        program_list =[]
        programs = ProgramMaster.objects.filter(program_status='Active')           
        for program in programs:
            program_list.append({'program_id':program.program_id,'program_name': program.program_name,'days':program.program_total_days})
    except Exception, e:
        print 'Exception : ',e
    return program_list


##----------------------------------------Program Assign-------------------------------------------------------------------

#================================================code for integration=================================================


# TO ADD THE CUSTOMER PROGRAM FROM MASTER PROGRAM
def add_customer_programs(request):
    #pdb.set_trace()
    print "in the assign_program----------------------------------"
    print request.GET
    print request.GET.get('startdate')
    print request.GET.get('enddate')
    print request
    status=''
   
    try:
        print "ADD_CUSTOMER_PROGRAM"
        user_obj = UserProfile.objects.get(user_id=request.GET.get('user_id'))
        program_obj = ProgramMaster.objects.get(program_id=request.GET.get('program_id'))
        if program_obj:
            if check_assigned_program_version2(user_obj,program_obj, request.GET.get('startdate'),request.GET.get('enddate')):
                print "exist"
                status='exist'
            elif check_assigned_program_date_version2(user_obj,request.GET.get('startdate'),request.GET.get('enddate')):
                print "DATE"
                status='date'
            else:
                user_program_obj=create_user_program_entry(user_obj,program_obj, request.GET.get('startdate'),request.GET.get('enddate'))
                program_work_obj=ProgramWorkoutMap.objects.filter(program_id = program_obj.program_id)
                if program_work_obj:
                    for program_work in program_work_obj:
                        user_program_workout_obj=create_user_program_workout_entry(user_program_obj,program_work)
                        work_exe_obj=WorkoutExerciseMap.objects.filter(workout_id=program_work.workout_id)
                        # print "^^^^^^^^^^^^^^^^^^^^^^^^^^^here"
                        # print work_exe_obj
                        if work_exe_obj:
                            for work_exe in work_exe_obj:
                                # print "----------------------work_exe--------------------------"
                                print work_exe
                                user_pgm_exer_obj=create_user_program_exercise_entry(user_program_workout_obj,work_exe)
                status='true' 
        data = { 'success':status}
    except Exception,e:
        print 'Exception',e
        data = {'success':'exception'}
    return HttpResponse(json.dumps(data), content_type='application/json')


def check_assigned_program_version2(user_obj,program_obj,startdate,enddate):
    print "in the check as"

    try:
        user_program_obj=UserProgramMap.objects.get(
                user_id                          = user_obj,
                program_id                       = program_obj,
                user_program_program_status='Active'
                )
               
        print "user_program_obj"
        print user_program_obj
        if user_program_obj:
            return True    
        else:
            return False
    except Exception,e:
        print 'Exception',e
        data = {'status':'false'}
        return False


def check_assigned_program_date_version2(user_obj,startdate,enddate):
    try:
        #pdb.set_trace()
        user_program_obj_list=UserProgramMap.objects.filter(user_id = user_obj,user_program_program_status='Active')
        for user_program_obj in user_program_obj_list:
            program_start_date= user_program_obj.user_program_start_date       #user_program_obj.user_program_start_date.strftime('%m/%d/%Y')
            program_end_date=   user_program_obj.user_program_end_date         #user_program_obj.user_program_end_date.strftime('%m/%d/%Y')
            check_start_date=   datetime.datetime.strptime(startdate,'%m/%d/%Y').date()
            check_end_date=     datetime.datetime.strptime(enddate,'%m/%d/%Y').date()
            #if (program_start_date <= check_start_date <= program_end_date) or (program_start_date<= check_end_date <= program_end_date):
            if (program_start_date <= check_start_date <= program_end_date) or (program_start_date<= check_end_date <= program_end_date) or ( check_start_date <= program_start_date <= check_end_date) or ( check_start_date <= program_end_date <= check_end_date):
                return True;   
                     
    except Exception,e:
        print 'Exception',e
        return False;
        data = {'status':'false'}
    return False
    
    
def check_assigned_program_date_for_update(user_program_obj,user_obj,startdate,enddate):
    try:
        #pdb.set_trace()
        user_program_obj_list=UserProgramMap.objects.filter(user_id = user_obj,user_program_program_status='Active').exclude(user_program_id = user_program_obj.user_program_id)
        for user_program_obj in user_program_obj_list:
            program_start_date= user_program_obj.user_program_start_date       #user_program_obj.user_program_start_date.strftime('%m/%d/%Y')
            program_end_date=   user_program_obj.user_program_end_date         #user_program_obj.user_program_end_date.strftime('%m/%d/%Y')
            check_start_date=   datetime.datetime.strptime(startdate,'%m/%d/%Y').date()
            check_end_date=     datetime.datetime.strptime(enddate,'%m/%d/%Y').date()
            #if (program_start_date <= check_start_date <= program_end_date) or (program_start_date<= check_end_date <= program_end_date):
            if (program_start_date <= check_start_date <= program_end_date) or (program_start_date<= check_end_date <= program_end_date) or ( check_start_date <= program_start_date <= check_end_date) or ( check_start_date <= program_end_date <= check_end_date) :
                return True;   
                     
    except Exception,e:
        print 'Exception',e
        return False;
        data = {'status':'false'}
    return False
    
#---------------------------------By Pranali-----------------------------------------


def check_assigned_program_date(user_obj,startdate,enddate):
    try:
        user_program_obj=UserProgramMap.objects.get(  
                user_id                          = user_obj,              
                user_program_start_date__range   =[datetime.datetime.strptime(startdate,'%m/%d/%Y'),datetime.datetime.strptime(enddate,'%m/%d/%Y')],
                user_program_end_date__range     =[datetime.datetime.strptime(startdate,'%m/%d/%Y'),datetime.datetime.strptime(enddate,'%m/%d/%Y')]
                )
        print "user_program_obj"        

        print "======================user_program_obj============================"
        print user_program_obj
        
        if len(user_program_obj)>=1:
            return False  
        else:
            return True
    except Exception,e:
        print 'Exception',e
        data = {'status':'false'}
        return False


def check_assigned_program(user_obj,program_obj,startdate,enddate):
    print "in the check as"

    try:
        user_program_obj=UserProgramMap.objects.get(
                user_id                          = user_obj,
                program_id                       = program_obj,
                user_program_start_date__range   =[datetime.datetime.strptime(startdate,'%m/%d/%Y'),datetime.datetime.strptime(enddate,'%m/%d/%Y')],
                user_program_end_date__range     =[datetime.datetime.strptime(startdate,'%m/%d/%Y'),datetime.datetime.strptime(enddate,'%m/%d/%Y')]
                )
                

        print user_program_obj
        if user_program_obj:
            return True    
        else:
            return False
    except Exception,e:
        print 'Exception',e
        data = {'status':'false'}
        return False
    
#------------------------------------------------End By PRanali--------------------------------



def create_user_program_entry(user_obj,program_obj,startdate,enddate):
    # pdb.set_trace()
    print "in the create_user_program_entry "
    user_program_obj=UserProgramMap(
            user_id                          = user_obj,
            program_id                       = program_obj,
            user_program_name                = 'PRG'+' '+user_obj.user_first_name+' '+program_obj.program_name,
            user_program_created_by          = 'Admin',
            user_program_updated_by          = 'Admin',
            user_program_start_date          = datetime.datetime.strptime(startdate,'%m/%d/%Y'),
            user_program_end_date            = datetime.datetime.strptime(enddate,'%m/%d/%Y'),
            user_program_created_date        = datetime.datetime.now().date(),
            user_program_updated_date        = datetime.datetime.now().date(),
            user_program_program_status      ='Active' 
            )
    user_program_obj.save()
    print "done with things================================================================="
    return user_program_obj


def create_user_program_workout_entry(user_program_obj,program_work):
    # pdb.set_trace()
    print "in the creatcreate_user_program_workout_entry ========================================"
    user_program_workout_obj=UserProgramWorkoutMaster(
            workout_id                                     = program_work.workout_id,
            user_program_id                                = user_program_obj,
            user_program_workout_name                      = program_work.workout_id.workout_name,
            user_program_workout_total_execise             = program_work.workout_id.workout_total_no_execise,
            user_program_workout_total_time                = program_work.workout_id.workout_total_time,
            user_program_workout_type                      = program_work.workout_id.workout_type,
            user_program_workout_day                       = program_work.program_workout_day,
            user_program_workout_created_by                = 'Admin',
            user_program_workout_updated_by                = 'Admin',
            user_program_workout_created_date              = datetime.datetime.now().date(),
            user_program_workout_updated_date              = datetime.datetime.now().date(),    
            user_program_workout_status                    = 'Active'
            )
    user_program_workout_obj.save()
    print "done with create_user_program_workout_entry================================================================="
    return user_program_workout_obj



def create_user_program_exercise_entry(user_program_workout_obj,work_exe):
    # pdb.set_trace()
    print "in the user_pgm_exercise_obj================================= "
    user_pgm_exer_obj=UserProgramExerciseMap(
            user_program_workout_id                             = user_program_workout_obj,
            exercise_id                                         = work_exe.exercise_id,
            user_program_exercise_body_part_id                  = work_exe.exercise_id.exercise_body_part_id,
            user_program_exercise_video_id                      = work_exe.exercise_id.exercise_video_id,
            user_program_exercise_name                          = work_exe.exercise_id.exercise_name,
            user_program_exercise_time                          = work_exe.exercise_id.exercise_time,
            user_program_exercise_workout_total_sets            = work_exe.workout_exercise_total_sets,
            user_program_exercise_workout_total_reps            = work_exe.workout_exercise_total_reps,
            user_program_exercise_workout_time_between_set      = work_exe.workout_exercise_time_between_set,
            user_program_exercise_workout_total_time            = work_exe.workout_exercise_total_time,
            user_program_exercise_workout_rest_time             = work_exe.workout_exercise_rest_time,
            user_program_exercise_created_by                    ='Admin',
            user_program_exercise_updated_by                    ='Admin',
            user_program_exercise_created_date                  = datetime.datetime.now().date(),
            user_program_exercise_updated_date                  = datetime.datetime.now().date(),
            user_program_exercise_workout_status                = 'Active'
            )
    user_pgm_exer_obj.save()
    print "done with the user_pgm_exercise_obj================================================================="
    return user_pgm_exer_obj

@csrf_exempt
def check_program_duration(request):
    print "================================================================="
    #pdb.set_trace()
    try:        
        user_program_obj = UserProgramMap.objects.get(user_program_id = request.POST.get('user_program_id')) 
        custom_obj = UserProfile.objects.get(user_id=user_program_obj.user_id)
        print custom_obj
        
        start_date=request.POST.get('startDate')
        end_date=request.POST.get('endDate')     
        if check_assigned_program_date_for_update(user_program_obj,custom_obj,start_date,end_date):
            data = {'success': 'false'}
        else:
            data = {'success': 'true'}
    except Exception, e:
        print 'Exception :' ,e    
        data = {'success':'Exception'}
    return HttpResponse(json.dumps(data), content_type='application/json')



def update_user_program(request):
    #pdb.set_trace()
    id=''
    try:        
        program_obj = UserProgramMap.objects.get(user_program_id=request.POST.get('user_program_id_test'))
        user_obj=program_obj.user_id 
        start_date=request.POST.get('startDate')
        end_date=request.POST.get('endDate')
        #-------check date range for user program---------            
        if check_assigned_program_date_for_update(program_obj,user_obj,start_date,end_date):
            data= view_customer_program_full_details(program_obj)
            opration_status = {'success':'false','ERROR_MSG':'*Given Duration is Already Assinged to This User For Another Program.'}
            data.update(opration_status)
            print data
            return render(request,'customer-edit-program.html',data)
            #return HttpResponse(json.dumps(data), content_type='application/json')
        #return HttpResponse(json.dumps(data), content_type='application/json')
        
        id=user_obj.id       
        program_obj.user_program_name = request.POST.get('program_name')       
        program_obj.user_program_start_date= datetime.datetime.strptime(request.POST.get('startDate'),'%m/%d/%Y')       
        program_obj.user_program_end_date = datetime.datetime.strptime(request.POST.get('endDate'),'%m/%d/%Y')         
        program_obj.user_program_updated_by = 'Test User'
        program_obj.user_program_updated_date = datetime.datetime.now()
        program_obj.user_program_program_status=request.POST.get('status_combo')        
        program_obj.save()
    except Exception,e:
        print 'Exception ',e
        data = {'data':'none'}
    return redirect('/user-detail-page/?user_id='+str(id))
    #return render(request,'customer-profile.html')
    