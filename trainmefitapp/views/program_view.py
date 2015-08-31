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
# importing constants
from constants import AppUserConstants, ExceptionLabel
from trainmefitapp.models import *


    program_id                          = models.AutoField(primary_key=True)
    program_name                        = models.CharField(max_length=30,null=True)
    program_user_objective_id           = models.ForeignKey(ObjectiveMaster,related_name='user_program_objective',null=True)
    program_user_gender                 = models.CharField(max_length=20,default=True, choices= GENDER)
    program_gym_access                  = models.CharField(max_length=20, choices= GYM_ACCESS)
    program_total_days                  =  models.IntegerField(null=True)
    program_created_by                  = models.CharField(max_length=20,null=True)
    program_updated_by                  = models.CharField(max_length=20,null=True)
    program_created_date                = models.DateTimeField(null=True)
    program_updated_date 


def get_prgram_list():
    Program_list =[]
    try:
        programs = ProgramMaster.objects.all()
        for program in programs:
            Program_list.append({'program_id':programs.program_id, 'program_name': programs.program_name })
    except Exception, e:
        print 'Exception : ',e
    return Program_list
    
    

def get_category_list():
    category_list =[]
    try:
        categories = Category.objects.all()
        for category in categories:
            category_list.append({'category_id':category.exercise_category_id, 'category_name': category.exercise_category_name})
    except Exception, e:
        print 'Exception : ',e
    return category_list
    
def get_workout_list(program_id):
    workout_list =[]
    try:
        workouts = program_workout_mapping.objects.all().filter(Program_id=program_id);
        for workout in workouts:
            workout_list.append({'workout_id':program_workout_mapping.workout_id});
    except Exception, e:
        print 'Exception : ',e
    return workout_list;
    
    
def get_exercises_list(workout_id):
    workout_list =[]
    try:
        workouts = program_workout_mapping.objects.all().filter(Program_id=program_id);
        for workout in workouts:
            workout_list.append({'workout_id':program_workout_mapping.workout_id});
    except Exception, e:
        print 'Exception : ',e
    return workout_list;
    
    