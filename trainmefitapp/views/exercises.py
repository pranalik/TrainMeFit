

from django.db import transaction
from django.shortcuts import render
from django.shortcuts import render_to_response

from django.contrib.auth.models import User
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
import pdb
import json
import time
import datetime
from constants import AppUserConstants, ExceptionLabel
from trainmefitapp.models import *
from django.shortcuts import redirect


# TO GET THE EXERCISE LIST PAGE
def exercise_list(request):
    return render(request,'exercises.html')

# CATEGORY LIST
def get_category_list():
    category_list =[]
    try:
        categories = ObjectiveMaster.objects.filter(objective_status="Active")
        for category in categories:
            category_list.append({'category_id':category.objective_id , 'category_name': category.objective_name})
    except Exception, e:
        print 'Exception : ',e
    return category_list

# BODYPART LIST
def get_bodypart():
    bodypart_list =[]
    try:
        bodyparts = BodyPartMaster.objects.filter(body_part_status="Active")
        for bodypart in bodyparts:
            bodypart_list.append({'bodypart_id':bodypart.body_part_id,'bodypart_name':bodypart.body_part_name})
    except Exception,e:
        print 'Exception ',e
    return bodypart_list
    
# TO SEND THE CATEGORY LIST AND BODYPART LIST   
def add_exercise_page(request):
    try:
    
        data = { 'success':'true', 'category_list':get_category_list(), 'bodypart_list' : get_bodypart() }
    except Exception, e:
        print 'Exception ',e
        data = {'success':'false'}
    return render(request,'add-exercise.html',data)

 # TO VIEW THE EXERCISE
def view_exercise(request):
##    pdb.set_trace()
    try:
        exercise_obj = Exercise.objects.get(exercise_id= request.GET.get('exercise_id'))
        data = {
            'success':'true','category_list':get_category_list(),
            'bodypart_list' : get_bodypart(), 'exercise_name' : exercise_obj.exercise_name, 
            'gender': exercise_obj.exercise_gender, 'exercise_id' : str(exercise_obj.exercise_id),
            'exercise_time':exercise_obj.exercise_time,'exercise_instructions':exercise_obj.exercise_instruction.all(),
            'body_part': exercise_obj.exercise_body_part_id,'exercise_cat':exercise_obj.exercise_objective_id,'gym':exercise_obj.exercise_gym_access,
            'status':exercise_obj.exercise_status,'created':exercise_obj.exercise_created_by,'updated':exercise_obj.exercise_updated_by,
            'created_date':exercise_obj.exercise_created_date.strftime('%m/%d/%y'),'updated_date':exercise_obj.exercise_updated_date.strftime('%m/%d/%y'),
            'intensity':exercise_obj.exercise_intensity
            }    
    except Exception,e:
        print 'Exception ',e
        data = {'success':'false'}
    return render(request,'view-exercise.html',data)


def edit_exercise(request):
##    pdb.set_trace()
    try:
        exercise_obj = Exercise.objects.get(exercise_id= request.GET.get('exercise_id'))
        data = {
            'success':'true','category_list': get_category_list(),
            'bodypart_list' : get_bodypart(), 'exercise_name' : exercise_obj.exercise_name, 
            'gender': exercise_obj.exercise_gender, 'exercise_id' : str(exercise_obj.exercise_id),
            'exercise_time':exercise_obj.exercise_time,'exercise_instruction':exercise_obj.exercise_instruction.all(),
            'body_part': exercise_obj.exercise_body_part_id,'exercise_cat':exercise_obj.exercise_objective_id,'gym':exercise_obj.exercise_gym_access,
            'status':exercise_obj.exercise_status,'created':exercise_obj.exercise_created_by,'updated':exercise_obj.exercise_updated_by,
            'created_date':exercise_obj.exercise_created_date.strftime('%m/%d/%y'),'updated_date':exercise_obj.exercise_updated_date.strftime('%m/%d/%y'),
            'intensity':exercise_obj.exercise_intensity
            }    
        print data
    except Exception,e:
        print 'Exception ',e
        data = {'success':'false'}    
    return render(request,'edit-exercise.html',data)

# TO  UPDATE THE EXERCISE
def update_exercise(request):
##    pdb.set_trace()
    try:
        print 'Update Exercise'
        exercise_obj = Exercise.objects.get(exercise_id=request.POST.get('exercise_id'))        
        exercise_obj.exercise_name=request.POST.get('exercise_name')
        exercise_obj.exercise_objective_id = ObjectiveMaster.objects.get(objective_id= request.POST.get('exercise_category'))
        exercise_obj.exercise_gender=request.POST.get('exercise_gender')        
        exercise_obj.exercise_body_part_id = BodyPartMaster.objects.get( body_part_id=request.POST.get('exercise_body_part_name'))      
        exercise_obj.exercise_time=request.POST.get('exercise_time')      
        exercise_obj.exercise_gym_access=request.POST.get('gym_exercise')
        exercise_obj.exercise_created_by=request.POST.get('created')
        exercise_obj.exercise_updated_by=request.POST.get('updated')
        exercise_obj.exercise_status=request.POST.get('status_dropdown')
        exercise_obj.exercise_intensity=request.POST.get('intensity')
        exercise_obj.exercise_updated_date=datetime.datetime.now()
        exercise_obj.save()     
    except Exception,e:
        print 'Exception ',e
        data = {'data':'none'}
    return redirect('/exercise-list/')
    #return render(request,'exercises.html')    

# TO GET THE EXERCISE LIST ON EXERCISE PAGE
def get_exercises_list(request):
    try:
        print 'Exercises List'  
        exercises_list = Exercise.objects.all()
        exer_list = []
        for exercise in exercises_list:
            video =  '<a href="//" class="table-link"> '+ '<span class="fa-stack">' + '<i class="fa fa-square fa-stack-2x"></i> <i class="fa fa-play-circle fa-stack-1x fa-inverse"></i> </span> </a>'
            edit =   '<a href="/view-exercise/?exercise_id='+ str(exercise.exercise_id)  +'" class="table-link"> '+ '<span class="fa-stack">' + '<i class="fa fa-square fa-stack-2x"></i> <i class="fa fa-search-plus fa-stack-1x fa-inverse"></i> </span> </a>'

            temp_obj={
                'exercise_name':exercise.exercise_name,
                'category':exercise.exercise_objective_id.objective_name,
                'gender':exercise.exercise_gender ,
                'bodypart':exercise.exercise_body_part_id.body_part_name, 
                'video':video,
                'edit':edit
            } 
            exer_list.append(temp_obj)
        data = {'data': exer_list}
        
    except Exception, e:
        print 'Exception : ', e    
        data = {'data':'none'}
    return HttpResponse(json.dumps(data), content_type='application/json')       
 

# TO SAVE THE EXERCISE 
@csrf_exempt
def save_exercise(request):
##    pdb.set_trace()
    try:
        print 'ADD EXERCISE'
               
        if request.method == "POST":

            exercise_obj           = Exercise(
            exercise_name          = request.POST.get('exercise_name'),
            exercise_body_part_id  = BodyPartMaster.objects.get(body_part_id=request.POST.get('body_part')),
            exercise_gender        = request.POST.get('gender'),
            exercise_objective_id  = ObjectiveMaster.objects.get(objective_id=request.POST.get('exercise_category')),
            exercise_gym_access    = request.POST.get('gym'),
            exercise_time          = request.POST.get('exercise_time'),
            exercise_updated_by    = "Admin",
            exercise_created_by    = "Admin",
            exercise_status        = "Active", 
            exercise_created_date  = datetime.datetime.now(),
            exercise_video_id      = request.POST.get('video_dropzone'),
            exercise_intensity     = request.POST.get('intensity') 
            ) 
            exercise_obj.save()
            
            print 'Request : ', request.POST
            instruction_list = request.POST.get('exercise_instruction_list')
            print instruction_list

            instruction_list = instruction_list.split(',')            

            for instruction in instruction_list :
                try:                  
                    
                    instruct_obj = InstructionMaster(
                            instruction_exercise_id   = exercise_obj,
                            instruction_name = instruction 
                            )
                    instruct_obj.save()
                    
                    data = { 'success':'true',}
                
                except Exception, e:
                        print 'Exception :' ,e    
                        data = {'data':'none'}   
          
        else:
            data = {'success': 'false'}
    except Exception, e:
            print 'Exception :' ,e    
            data = {'data':'none'}   
    return redirect('/exercise-list/')
    #return render(request,'exercises.html',data)    

# TO GET THE EXERCISES IN WORKOUT SECTION 
def get_exercise_by_bodypart(request):
##    pdb.set_trace()
    exrcise_list =[]
    try:
        exercises=Exercise.objects.filter(exercise_body_part_id=request.GET.get('body_part_id'),exercise_objective_id=request.GET.get('exercise_category'),exercise_gender=request.GET.get('exercise_gender'),exercise_intensity=request.GET.get('intensity'),exercise_status="Active")
        for exercise in exercises:
            exrcise_list.append({'exercise_id':exercise.exercise_id,'exercise_name':exercise.exercise_name,'exercise_time':exercise.exercise_time})
        data = {'exercise_list': exrcise_list}
        print json.dumps(data)
    except Exception,e: 
        print 'Exception',e
        data = {'exercise_list': exrcise_list}
    return HttpResponse(json.dumps(data), content_type='application/json')  

# TO DELETE THE INSTRUCTION IN EDIT EXERCISE
def delete_instruction_in_exercise(request):
##    pdb.set_trace()
    try:
        exercise_instruction= InstructionMaster(instruction_id = request.GET.get('deleteInstructionExercise_id'))  
        exercise_instruction.delete()
        data = {'success':'true'}
    except Exception,e:
        print 'Exception ',e    
    return HttpResponse(json.dumps(data), content_type='application/json')

# TO ADD THE INSTRUCTION IN EDIT EXERCISE 
def add_instruction_in_exercise(request):
    #pdb.set_trace()
    try:
        exercise_obj    = Exercise.objects.get(exercise_id=request.GET.get('exercise_id'))
        exercise_instruction= InstructionMaster(instruction_exercise_id=exercise_obj, instruction_name=request.GET.get('instruction_id'))
        
        exercise_instruction.save() 
           
        data = { 'success':'true', 'error_message':'Successfully Added '}
    except Exception,e:
        print 'Exception : ' , e
        data = {'success':'false', 'error_message': 'Failed to add instruction in exercise' }
    return HttpResponse(json.dumps(data), content_type='application/json')
