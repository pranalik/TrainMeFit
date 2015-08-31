
from django.shortcuts import render
from django.shortcuts import render_to_response
from datetime import datetime
from django.contrib.auth.models import User
from time import gmtime, strftime
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.http import HttpResponseRedirect
import pdb
import json
##import datetime
import time
from django.db import IntegrityError
from django.shortcuts import redirect
# importing constants
from constants import AppUserConstants, ExceptionLabel
from trainmefitapp.models import *



def workout(request):
    return render(request,'workouts.html')

def get_category_list():
    category_list =[]
    try:
        categories = ObjectiveMaster.objects.filter(objective_status="Active")
        for category in categories:
            category_list.append({'category_id':category.objective_id , 'category_name': category.objective_name})
    except Exception, e:
        print 'Exception : ',e
    return category_list

def get_bodypart():
    bodypart_list =[]
    try:
        bodyparts = BodyPartMaster.objects.filter(body_part_status="Active")
        for bodypart in bodyparts:
            bodypart_list.append({'bodypart_id':bodypart.body_part_id,'bodypart_name':bodypart.body_part_name})
    except Exception,e:
        print 'Exception ',e
    return bodypart_list

def get_exercise():
    exercise_list =[]
    try:
        exercises = Exercise.objects.filter(exercise_status="Active")
        for exercise in exercises:
            exercise_list.append({'exercise_id':exercise.exercise_id,'exercise_name':exercise.exercise_name})
    except Exception,e:
        print 'Exception',e
    return exercise_list            

def add_workout(request):
    try:
        print 'ADD_WORKOUT'
        data = { 'success':'true', 'category_list':get_category_list(), 'bodypart_list' : get_bodypart(), 'exercise_list' : get_exercise()}
    except Exception,e:
        print 'Exception',e
        data = {'success':'false'}    
  
    return render(request,'add-workout.html',data)

def view_workout(request):
##    pdb.set_trace()
    try:
        workout_obj=Workout.objects.get(workout_id=request.GET.get('workout_id'))
        ex_list = WorkoutExerciseMap.objects.filter(workout_id=workout_obj.workout_id)
        print ex_list
##        dt = ''
       
##        if workout_obj.date_updated:
##            dt = workout_obj.date_updated.strftime('%d-%m-%Y')
        
        exercise_list_to_send = []
        for ex in ex_list:
            temp_dict = { 
                          'ex_id':ex.exercise_id,
                          'ex_name':ex.exercise_id.exercise_name,
                          'ex_gender':ex.exercise_id.exercise_gender,'ex_bodypart':ex.exercise_id.exercise_body_part_id.body_part_name ,
                          'ex_tot_rep':ex.workout_exercise_total_reps,'ex_tot_set':ex.workout_exercise_total_sets,
                          'ex_tim_bet_set': ex.workout_exercise_time_between_set,'ex_res_tim':ex.workout_exercise_rest_time,
                          'ex_tot_ex_tim': ex.workout_exercise_total_time,'ex_work_id':ex.workout_exercise_id
                        }
            exercise_list_to_send.append(temp_dict)
        
            
        data = {
                
                'success':'true','workout_id': str(workout_obj.workout_id),
                'workout_name':workout_obj.workout_name,
                'number_of_exercises': workout_obj.workout_total_no_execise,
                'approximate_workout_time':workout_obj.workout_total_time,
                'created_name':workout_obj.workout_created_by,
                'created_date':workout_obj.workout_created_date.strftime('%m/%d/%y'),
                'updated_by':workout_obj.workout_updated_by,
                'updated_date':workout_obj.workout_updated_date.strftime('%m/%d/%y'),
                'status':workout_obj.workout_status,
                'wk_type':workout_obj.workout_type,
                'wk_intensity':workout_obj.workout_intensity,
                'ex_list':exercise_list_to_send
##                'workout_exercise_total_sets':workout_obj.WorkoutExerciseMap.workout_exercise_total_sets,
##                'workout_exercise_total_reps':workout_obj.WorkoutExerciseMap.workout_exercise_total_reps,
##                'workout_exercise_total_time':workout_obj.WorkoutExerciseMap.workout_exercise_total_time,
##                'workout_exercise_rest_time':workout_obj.WorkoutExerciseMap.workout_exercise_rest_time,
##                'workout_exercise_time_between_set':workout_obj.WorkoutExerciseMap.workout_exercise_time_between_set
               }

        
        data1 = { 'success':'true', 'category_list':get_category_list(), 'bodypart_list' : get_bodypart(), 'exercise_list' : get_exercise()}
        data.update(data1)
    except Exception,e:
        print 'Exception ',e
        data =  {'success':'false'}
    return render(request,'view-workout.html',data) 

def edit_workout(request):
##    pdb.set_trace()
    try:
        workout_obj=Workout.objects.get(workout_id=request.GET.get('workout_id'))
        ex_list = WorkoutExerciseMap.objects.filter(workout_id=workout_obj.workout_id)
        print ex_list
        exercise_list_to_send = []
        for ex in ex_list:
            temp_dict = { 'ex_id':ex.exercise_id,
                          'ex_name':ex.exercise_id.exercise_name,
                          'ex_gender':ex.exercise_id.exercise_gender,'ex_bodypart':ex.exercise_id.exercise_body_part_id.body_part_name ,
                          'ex_tot_rep':ex.workout_exercise_total_reps,'ex_tot_set':ex.workout_exercise_total_sets,
                          'ex_tim_bet_set': ex.workout_exercise_time_between_set,'ex_res_tim':ex.workout_exercise_rest_time,
                          'ex_tot_ex_tim': ex.workout_exercise_total_time,'ex_work_id':ex.workout_exercise_id
                        }
            exercise_list_to_send.append(temp_dict)
        
            
        data = {
                
                'success':'true','workout_id': str(workout_obj.workout_id),
                'workout_name':workout_obj.workout_name,
                'number_of_exercises': workout_obj.workout_total_no_execise,
                'approximate_workout_time':workout_obj.workout_total_time,
                'created_name':workout_obj.workout_created_by,
                'created_date':workout_obj.workout_created_date.strftime('%m/%d/%y'),
                'updated_by':workout_obj.workout_updated_by,
                'updated_date':workout_obj.workout_updated_date.strftime('%m/%d/%y'),
                'status':workout_obj.workout_status,
                'wk_type':workout_obj.workout_type,
                'wk_intensity':workout_obj.workout_intensity,
                'ex_list':exercise_list_to_send
##                'workout_exercise_total_sets':workout_obj.WorkoutExerciseMap.workout_exercise_total_sets,
##                'workout_exercise_total_reps':workout_obj.WorkoutExerciseMap.workout_exercise_total_reps,
##                'workout_exercise_total_time':workout_obj.WorkoutExerciseMap.workout_exercise_total_time,
##                'workout_exercise_rest_time':workout_obj.WorkoutExerciseMap.workout_exercise_rest_time,
##                'workout_exercise_time_between_set':workout_obj.WorkoutExerciseMap.workout_exercise_time_between_set
               }

        
        data1 = { 'success':'true', 'category_list':get_category_list(), 'bodypart_list' : get_bodypart(), 'exercise_list' : get_exercise()}
        data.update(data1)
    except Exception,e:
        print 'Exception ',e
        data =  {'success':'false'}
    return render(request,'edit-workout.html',data)

@csrf_exempt   
def update_workout(request):
    # pdb.set_trace()
    print 'update_workout-----------------------------'
    # print request.POST
    # print request.POST.get('approximate_workout_time')
    # print "------------------------------------"
    try:
        if request.method == 'POST':
            workout_obj  = Workout.objects.get(workout_id = request.POST.get('work_id'))
            workout_obj.workout_name                  = request.POST.get('workout_name')
            workout_obj.workout_total_time            = request.POST.get('approximate_workout_time')
            workout_obj.workout_total_no_execise      = request.POST.get('number_of_exercises') 
            workout_obj.workout_status                = request.POST.get('status_dropdown')
            workout_obj.workout_type                  = request.POST.get('wk_type')
            workout_obj.workout_intensity             = request.POST.get('wk_intensity')  
            workout_obj.workout_updated_date          =datetime.datetime.now()
            workout_obj.save()

            # workout_data = request.POST.get('totalData')
            # workoutinfo = json.loads(workout_data)
            # print 'workoutinfo'
            # print workoutinfo
            # for wk in workoutinfo:
            #     if  check_exist_exercise(workout_obj,wk.get('exercise_id')):
            #         print "exist"
            #     else:
            #         workout_exercise_obj = WorkoutExerciseMap(
            #         workout_id   = workout_obj,
            #         exercise_id  = Exercise.objects.get(exercise_id=wk.get('exercise_id')),
            #         workout_exercise_total_sets=wk.get('Total Sets'),
            #         workout_exercise_total_reps= wk.get('Total Reps'),
            #         workout_exercise_total_time=wk.get('Total Exercise Time'),
            #         workout_exercise_rest_time=wk.get('Rest Time'),
            #         workout_exercise_time_between_set =  wk.get('Time Between Sets')
            #         )
            #         workout_exercise_obj.save()
            data = {'success': 'true'}
        else:
            data = {'success': 'false'}
    except Exception, e:
            print 'Exception :' ,e    
            data = {'data':'none'}
    #return render(request,'workouts.html',data)
    return redirect('/workout/')



def check_exist_exercise(workout_obj,exercise_id):
    try:
        WorkoutExerciseMap.objects.get(workout_id = workout_obj,exercise_id  = Exercise.objects.get(exercise_id=exercise_id))
        return True
    except Exception,e:
        print 'Exception',e
        return False   

#-----------Edit Workout---------------------------------
@csrf_exempt   
def edit_workout_exercise(request):
    #pdb.set_trace()
    # print 'edit_workout_exercise-----------------------------'
    try:
        if request.method == 'POST':
            workout_obj  = Workout.objects.get(workout_id = request.POST.get('workout_id'))
            workout_data = request.POST.get('totalData')
            workoutinfo = json.loads(workout_data)
            print 'workoutinfo'
            print workoutinfo
            for wk in workoutinfo:
                if  check_exist_exercise(workout_obj,wk.get('exercise_id')):
                    print "exist"
                else:
                    workout_exercise_obj = WorkoutExerciseMap(workout_id = workout_obj)
                    workout_exercise_obj.exercise_id  = Exercise.objects.get(exercise_id=wk.get('exercise_id'))
                    workout_exercise_obj.workout_exercise_total_sets=wk.get('Total Sets')
                    workout_exercise_obj.workout_exercise_total_reps= wk.get('Total Reps')
                    workout_exercise_obj.workout_exercise_total_time=wk.get('Total Exercise Time')
                    workout_exercise_obj.workout_exercise_rest_time=wk.get('Rest Time')
                    workout_exercise_obj.workout_exercise_time_between_set =  wk.get('Time Between Sets')
                    workout_exercise_obj.save()
            data = {'success': 'true'}
        else:
            data = {'success': 'false'}
    except Exception, e:
            print 'Exception :' ,e    
            data = {'data':'none'}
    return HttpResponse(json.dumps(data), content_type='application/json')

def check_exist_exercise_form(request):
    try:
        workout_exercise_obj=WorkoutExerciseMap.objects.get(workout_id =  Workout.objects.get(workout_id=request.GET.get('workout_id')),exercise_id  = Exercise.objects.get(exercise_id=request.GET.get('exercise_id')))
        if workout_exercise_obj:
            data = {'status': 'success'}
    except Exception,e:
        print 'Exception',e
        data = {'status': 'fail'}
    return HttpResponse(json.dumps(data), content_type='application/json')   



@csrf_exempt
def get_workout_list(request):
##    pdb.set_trace()
    try:
        print 'Workout List'  
        workout_list = Workout.objects.all()
        workouts_list = []    
        for workout in workout_list:
            
            edit   = '<a href="/view-workout/?workout_id=' +str(workout.workout_id)+'"  class="table-link"> '+ '<span class="fa-stack">' + '<i class="fa fa-square fa-stack-2x"></i> <i class="fa fa-search-plus fa-stack-1x fa-inverse"></i> </span> </a>'    
            dt = ''
            if workout.workout_updated_date:
                dt = workout.workout_updated_date.strftime('%d-%m-%Y')
            temp_obj={
                'workout_name':workout.workout_name ,
                'number_of_exercises':workout.workout_total_no_execise,
                'time':workout.workout_total_time,
                'date_updated':dt,
                'status':workout.workout_status,
                'edit':edit
            } 
            workouts_list.append(temp_obj)
        data = {'data': workouts_list}
       
    except Exception, e:
        print 'Exception : ', e
        data = {'data': 'none'}
    return HttpResponse(json.dumps(data), content_type='application/json')

@csrf_exempt
def save_workout(request):
##    pdb.set_trace()
    try:
        print 'ADD_WORKOUT'
        if request.method == 'POST':
            workout_obj  = Workout(
                workout_name             = request.POST.get('workout_name'),
                workout_total_time       = request.POST.get('workout_time'),
                workout_intensity        = request.POST.get('wk_intensity'),
                workout_type             = request.POST.get('wk_type'), 
                workout_total_no_execise = request.POST.get('number_of_exercises'),
                workout_created_by       = 'Admin',
                workout_updated_by       = 'Admin',
                workout_created_date     =datetime.datetime.now(),           
                workout_updated_date     =datetime.datetime.now()
            )   
            workout_obj.save()  
            workout_data = request.POST.get('totalData')
            workoutinfo = json.loads(workout_data)
            print workoutinfo
            for wk in workoutinfo:
                try:
                    workout_exercise_obj = WorkoutExerciseMap(
                        workout_id   = workout_obj,
                        exercise_id  = Exercise.objects.get(exercise_id=wk.get('exercise_id')),
                        workout_exercise_total_sets=wk.get('Total Sets'),
                        workout_exercise_total_reps= wk.get('Total Reps'),
                        workout_exercise_total_time=wk.get('Total Exercise Time'),
                        workout_exercise_rest_time=wk.get('Rest Time'),
                        workout_exercise_time_between_set =  wk.get('Time Between Sets')
                       )
                    
                    workout_exercise_obj.save()
                except Exception, e:
                    print 'Workout Exercise Mapping data Saving exception :', e
            data = {'success': 'true'}
        else:
            data = {'success': 'false'}
    except Exception, e:
            print 'Exception :' ,e    
            data = {'data':'none'}            
    return redirect('/workout/')
    #return render(request,'workouts.html',data)


# This is for adding exercise in workout at the time of save workout
def add_exercise_in_workout(request):
    try:
        exercise_obj    = Exercise.objects.get(exercise_id=request.GET.get('exercise_id'))
        workout_obj     = Workout.objects.get(workout_id=request.GET.get('workout_id')) 
        workout_exercise= WorkoutExercise(workout_id=workout_obj,exercise_id=exercise_obj)
        workout_exercise.save() 
        data = { 'success':'true', 'exercise': exercise_obj.exercise_id}
    except Exception,e:
        print 'Exception',e
        data = {'data':'none'}   
    return HttpResponse(json.dumps(data), content_type='application/json')
 
# This is for deleting exercise in workout at the time of edit workout   
def delete_exercise_in_workout(request):
##    pdb.set_trace()
    try:
        print request.GET.get('deleteWorkoutExercise_id')
        workout_exercise= WorkoutExerciseMap(workout_exercise_id = request.GET.get('deleteWorkoutExercise_id')) 
        print workout_exercise
        workout_exercise.delete()
        data = {'success':'true'}
    except Exception,e:
        print 'Exception ',e    
    return HttpResponse(json.dumps(data),content_type='application/json')




#------------------------Edit Workout Excercises-----------Not using now-------------
@csrf_exempt   
def edit_workout_exercise0101(request):
    #pdb.set_trace()
   
    try:
        if request.method == 'POST':
            workout_obj  = Workout.objects.get(workout_id = request.POST.get('workout_id'))
            workout_data = request.POST.get('totalData')
            workoutinfo = json.loads(workout_data)
            print 'workoutinfo'
            print workoutinfo
            for wk in workoutinfo:
                if  check_exist_exercise(workout_obj,wk.get('exercise_id')):
                    print "exist"
                else:
                    workout_exercise_obj = WorkoutExerciseMap(workout_id = workout_obj)
                    workout_exercise_obj.exercise_id  = Exercise.objects.get(exercise_id=wk.get('exercise_id'))
                    workout_exercise_obj.workout_exercise_total_sets=wk.get('Total Sets')
                    workout_exercise_obj.workout_exercise_total_reps= wk.get('Total Reps')
                    workout_exercise_obj.workout_exercise_total_time=wk.get('Total Exercise Time')
                    workout_exercise_obj.workout_exercise_rest_time=wk.get('Rest Time')
                    workout_exercise_obj.workout_exercise_time_between_set =  wk.get('Time Between Sets')
                    workout_exercise_obj.save()            
            #--------------------------------get Excercise------------------------------------
            ex_list = WorkoutExerciseMap.objects.filter(workout_id=workout_obj)
            exercise_list=[]
            for ex in ex_list:
                exercise_list = ({ 
                          'ex_id':ex.exercise_id,
                          'ex_name':ex.exercise_id.exercise_name,
                          'ex_gender':ex.exercise_id.exercise_gender,'ex_bodypart':ex.exercise_id.exercise_body_part_id.body_part_name ,
                          'ex_tot_rep':ex.workout_exercise_total_reps,'ex_tot_set':ex.workout_exercise_total_sets,
                          'ex_tim_bet_set': ex.workout_exercise_time_between_set,'ex_res_tim':ex.workout_exercise_rest_time,
                          'ex_tot_ex_tim': ex.workout_exercise_total_time,'ex_work_id':ex.workout_exercise_id
                        })
            data = {'success': 'true','exercise_list':exercise_list}
            
        else:
            data = {'success': 'false'}
    except Exception, e:
            print 'Exception :' ,e    
            data = {'data':'false'}
    return HttpResponse(json.dumps(data), content_type='application/json')


#-------------------------------------------------------------------------







