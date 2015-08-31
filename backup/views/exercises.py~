
from django.db import transaction
from django.shortcuts import render
from django.shortcuts import render_to_response

from django.contrib.auth.models import User

##from django import forms
##from trainmefitapp.views.forms import UploadFileForm
##from trainmefitapp.views.models import ModelWithFileField

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
import pdb
import json


# importing constants
from constants import AppUserConstants, ExceptionLabel
from trainmefitapp.models import *



def exercise_list(request):
    return render(request,'exercises.html')

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
    
   

def add_exercise_page(request):
    try:
    
        data = { 'success':'true', 'category_list':get_category_list(), 'bodypart_list' : get_bodypart() }
    except Exception, e:
        print 'Exception ',e
        data = {'success':'false'}
    return render(request,'add-exercise.html',data)

 
    
def edit_exercise(request):
##    pdb.set_trace()
    try:
        exercise_obj = Exercise.objects.get(exercise_id= request.GET.get('exercise_id'))
        data = {
            'success':'true','category_list':get_category_list(),
            'bodypart_list' : get_bodypart(), 'exercise_name' : exercise_obj.exercise_name, 
            'gender': exercise_obj.exercise_gender, 'exercise_id' : str(exercise_obj.exercise_id),
            'time':exercise_obj.exercise_time,'exercise_instruction':exercise_obj.exercise_instruction,
            'body_part': exercise_obj.body_part_id,'exercise_cat':exercise_obj.exercise_category
            }    
    except Exception,e:
        print 'Exception ',e
        data = {'success':'false'}
    return render(request,'edit-exercise.html',data)

def update_exercise(request):
##    pdb.set_trace()
    try:
        print 'Update Exercise'
        exercise_obj = Exercise.objects.get(exercise_id=request.POST.get('exercise_id'))
        
        exercise_obj.exercise_name=request.POST.get('exercise_name')
        exercise_obj.exercise_category = Category.objects.get(exercise_category_id= request.POST.get('exercise_category'))
        exercise_obj.exercise_gender=request.POST.get('exercise_gender')
        exercise_obj.body_part_id = BodyPart.objects.get(body_part_id=request.POST.get('exercise_body_part_name'))
        exercise_obj.exercise_time=request.POST.get('exercise_time')
        exercise_obj.exercise_instruction=request.POST.get('exercise_instructions')
        exercise_obj.is_gym_exercise=request.POST.get('is_gym_exercise')
        exercise_obj.save()
     
    except Exception,e:
        print 'Exception ',e
        data = {'data':'none'}
    return render(request,'exercises.html')    


def get_exercises_list(request):
    try:
        print 'Exercises List'  
        exercises_list = Exercise.objects.all()
        exer_list = []
        for exercise in exercises_list:
            video =  '<a href="//" class="table-link"> '+ '<span class="fa-stack">' + '<i class="fa fa-square fa-stack-2x"></i> <i class="fa fa-play-circle fa-stack-1x fa-inverse"></i> </span> </a>'
            edit =   '<a href="/edit-exercise/?exercise_id='+ str(exercise.exercise_id)  +'" class="table-link"> '+ '<span class="fa-stack">' + '<i class="fa fa-square fa-stack-2x"></i> <i class="fa fa-pencil fa-stack-1x fa-inverse"></i> </span> </a>'

            temp_obj={
                'exercise_name':exercise.exercise_name,
                'category':exercise.exercise_category.exercise_category_name,
                'gender':exercise.exercise_gender ,
                'bodypart':exercise.body_part_id.exercise_body_part_name, 
                'video':video,
                'edit':edit
            } 
            exer_list.append(temp_obj)
        data = {'data': exer_list}
        
    except Exception, e:
        print 'Exception : ', e    
        data = {'data':'none'}
    return HttpResponse(json.dumps(data), content_type='application/json')       
 

 
@csrf_exempt
def save_exercise(request):
##    pdb.set_trace()
    try:
        print 'ADD EXERCISE'
       
        if request.method == "POST":
            exercise_obj           = Exercise(
            exercise_name          = request.POST.get('add_exercise_name'),
            body_part_id           = BodyPart.objects.get(body_part_id=request.POST.get('body_part')),
            exercise_gender        = request.POST.get('gender'),
            exercise_category      = Category.objects.get(exercise_category_id=request.POST.get('exercise_category')),
            is_gym_exercise        = request.POST.get('gym_access'),
            exercise_time          = request.POST.get('exercise_time'),
            exercise_instruction   = request.POST.get('exercise_instructions'),
            exercise_video_id      = request.POST.get('video_dropzone')
            ) 
            exercise_obj.save()
            
            data = { 'success':'true','ADD_EXERCISE':exercise_obj }
        else:
            data = {'success': 'false'}
    except Exception, e:
            print 'Exception :' ,e    
            data = {'data':'none'}
    return render(request,'exercises.html',data)    

 
def get_exercise_by_bodypart(request):
    exrcise_list =[]
    try:
        exercises=Exercise.objects.filter(body_part_id=request.GET.get('body_part_id'))
        for exercise in exercises:
            exrcise_list.append({'exercise_id':exercise.exercise_id,'exercise_name':exercise.exercise_name})
        data = {'exercise_list': exrcise_list}
        print json.dumps(data)
    except Exception,e:
        print 'Exception',e
        data = {'exercise_list': exrcise_list}
    return HttpResponse(json.dumps(data), content_type='application/json')  

 
##def home(request):
##    if request.method == 'POST':
##        form = UploadFileForm(request.POST, request.FILES)
##        if form.is_valid():
##            new_file = UploadFile(file = request.FILES['file'])
##            new_file.save()
## 
##            return HttpResponseRedirect(reverse('main:home'))
##    else:
##        form = UploadFileForm()
## 
##    data = {'form': form}
##    return render_to_response('exercises.html', data, context_instance=RequestContext(request))