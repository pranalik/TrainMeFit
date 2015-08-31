
from django.shortcuts import render
from django.shortcuts import render_to_response

from django.contrib.auth.models import User
from time import gmtime, strftime
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.http import HttpResponseRedirect
import pdb
import json
import datetime
import time
# importing constants
from constants import AppUserConstants, ExceptionLabel
from trainmefitapp.models import *



def workout(request):
    return render_to_response('workouts.html')

def get_category_list():
    category_list =[]
    try:
        categories = Category.objects.all()
        for category in categories:
            category_list.append({'category_id':category.exercise_category_id, 'category_name': category.exercise_category_name})
    except Exception, e:
        print 'Exception : ',e
    return category_list

def get_bodypart():
    bodypart_list =[]
    try:
        bodyparts = BodyPart.objects.all()
        for bodypart in bodyparts:
            bodypart_list.append({'bodypart_id':bodypart.body_part_id,'bodypart_name':bodypart.exercise_body_part_name})
    except Exception,e:
        print 'Exception ',e
    return bodypart_list

def get_exercise():
    exercise_list =[]
    try:
        exercises = Exercise.objects.all()
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

def edit_workout(request):
##    pdb.set_trace()
    try:
        workout_obj=Workout.objects.get(workout_id=request.GET.get('workout_id'))
        ex_list = WorkoutExercise.objects.filter(workout_id=workout_obj)
        dt = ''
       
        if workout_obj.date_updated:
            dt = workout_obj.date_updated.strftime('%d-%m-%Y')
        
        exercise_list_to_send = []
        for ex in ex_list:
            temp_dict = { 'ex_name':ex.exercise_id.exercise_name,'ex_category':ex.exercise_id.exercise_category,
                          'ex_gender':ex.exercise_id.exercise_gender,'ex_bodypart':ex.exercise_id.body_part_id.exercise_body_part_name }
            exercise_list_to_send.append(temp_dict)
        
            
        data = {
                
                'success':'true','workout_id': str(workout_obj.workout_id),
                'workout_name':workout_obj.workout_name,
                'number_of_exercises': workout_obj.number_of_exercises,
                'approximate_workout_time':workout_obj.approximate_workout_time.strftime('%H:%M:%S'),
                'date_updated':dt,
                'status':workout_obj.user_row_status,
                'ex_list':exercise_list_to_send
               }
        print ex_list 
        
        data1 = { 'success':'true', 'category_list':get_category_list(), 'bodypart_list' : get_bodypart(), 'exercise_list' : get_exercise()}
        data.update(data1)
    except Exception,e:
        print 'Exception ',e
        data =  {'success':'false'}
    return render(request,'edit-workout.html',data) 

##def delete_workout_exercise(request):
##    
##    workout_obj=Workout.objects.get(workout_id=request.GET.get('workout_id'))
##    work_exe_obj=WorkoutExercise.objects.get(workoutexercise_id=request.GET.get('workout_id'))
    

    
    
@csrf_exempt
def get_workout_list(request):
##    pdb.set_trace()
    try:
        print 'Workout List'  
        workout_list = Workout.objects.all()
        workouts_list = []    
        for workout in workout_list:
            if workout.user_row_status == 1 :
                status = '<span class="label label-success">Active</span>'
            else:
                status = '<span class="label label-warning">Inactive</span>'  
                                          
            edit   = '<a href="/edit-workout/?workout_id=' +str(workout.workout_id)+'"  class="table-link"> '+ '<span class="fa-stack">' + '<i class="fa fa-square fa-stack-2x"></i> <i class="fa fa-pencil fa-stack-1x fa-inverse"></i> </span> </a>'    
            dt = ''
            if workout.date_updated:
                dt = workout.date_updated.strftime('%d-%m-%Y')
            temp_obj={
                'workout_name':workout.workout_name ,
                'number_of_exercises':workout.number_of_exercises,
                'time':workout.approximate_workout_time.strftime('%H:%M:%S'),
                'status':status,
                'date_updated':dt,
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
                approximate_workout_time = request.POST.get('workout_time'),
                user_row_status          = True,
                date_updated             = request.POST.get('date_updated'),
                number_of_exercises      = request.POST.get('number_of_exercises')  
            )   # Creation of workout object
            workout_obj.save()  # save workout object
            
            # Mapping between workout and exercises
            exercise_list = request.POST.get('workout_exercise_list')
            print exercise_list
            exercise_list = exercise_list.split(',')
            
            for ex_id in exercise_list :
                workout_exercise_obj = WorkoutExercise(
                        workout_id   = workout_obj,
                        exercise_id  = Exercise.objects.get(exercise_id=ex_id ) 
                    )
                workout_exercise_obj.save()
            
            data = { 'success':'true',} 
        else:
            data = {'success': 'false'}
    except Exception, e:
            print 'Exception :' ,e    
            data = {'data':'none'}
    return render(request,'workouts.html',data) 
   
def update_workout(request):
##    pdb.set_trace()
    try:
        print 'Update Workout'
        workout_obj = Workout.objects.get(workout_id=request.POST.get('workout_id'))
        workout_obj.workout_name=request.POST.get('workout_name')
        workout_obj.number_of_exercises=request.POST.get('number_of_exercises')
        workout_obj.approximate_workout_time=request.POST.get('approximate_workout_time')
        workout_obj.user_row_status=request.POST.get('user_row_status')
  
        workout_obj.save()
     
    except Exception,e:
        print 'Exception ',e
        data = {'data':'none'}
    return render(request,'workouts.html')    

def add_exercise_in_workout(request):
##    pdb.set_trace()    
    try:
##        exercise_id=request.GET.get('exercise_id')
##        workout_id=request.GET.get('workout_id')
##        
      
        exercise_obj    = Exercise.objects.get(exercise_id=request.GET.get('exercise_id'))
        workout_obj     = Workout.objects.get(workout_id=request.GET.get('workout_id')) 
        workout_exercise= WorkoutExercise(workout_id=workout_obj,exercise_id=exercise_obj)
        
        workout_exercise.save() 
           
        data = { 'success':'true', 'exercise': exercise_obj}
    except Exception,e:
        print 'Exception',e
        data = {'data':'none'}   
        
def delete_exercise_in_workout(request):
    exercise_obj =  Exercise.objects.get(exercise_id=request.GET.get('exercise_id'))   
    workout_obj     = Workout.objects.get(workout_id=request.GET.get('workout_id')) 
    workout_exercise= WorkoutExercise(workout_id=workout_obj,exercise_id=exercise_obj)  
    
    workout_exercise.delete()
    return HttpResponse('deleted')  