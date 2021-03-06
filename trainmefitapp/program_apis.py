from django.shortcuts import render
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.cache import cache_control
from django.contrib import auth
import pdb
import json
from django.http import HttpResponse
from django.http import HttpResponseRedirect
import datetime

# importing constants
from constants import AppUserConstants, ExceptionLabel
from trainmefitapp.models import *


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def program_list(request):
    return render_to_response('programs.html')

#def view_program(request):
#    return render_to_response('view-program.html')

def edit_program(request):
    objective_list=[]   
    try:   
        #pdb.set_trace()        
        program_obj = ProgramMaster.objects.get(program_id= request.GET.get('program_id'))

        #----------------Getting all user abjective ----------------------------------   
        objective_objes=ObjectiveMaster.objects.all()    	 
        for objective in objective_objes:
            objective_list.append({'objective_id':objective.objective_id, 'objective':objective.objective_name}) 
			
		#----------------Getting all workout ----------------------------------  
        workout_all_objs=Workout.objects.all() 
        all_workout_list=[]       
        for workot in workout_all_objs: 
        		all_workout_list.append({'workout_id':workot.workout_id,'workout_name':workot.workout_name,
        		'workout_time':workot.workout_total_time,'workout_execises':workot.workout_total_no_execise})       		
					
		#----------------Getting programs workout for table------------------------------------
        program_workout_obj = ProgramWorkoutMap.objects.filter(program_id=program_obj) 
        program_workout_list=[]
        for program_workout in program_workout_obj:         		
            program_workout_list.append({
                     	'program_workout_id':program_workout.program_workout_id,'time':program_workout.workout_id.workout_total_time,'days':program_workout.program_workout_day,'workout_name':program_workout.workout_id.workout_name,'execises':program_workout.workout_id.workout_total_no_execise,'intensity':program_workout.workout_id.workout_intensity
                        })
             	                
        data = {
            'success':'true','program_id': program_obj.program_id,'program_name': program_obj.program_name,
            'gym_access' : program_obj.program_gym_access, 'gender' : program_obj.program_user_gender,
            'days':program_obj.program_total_days,'objective':program_obj.program_user_objective_id,
            'objective_id':program_obj.program_user_objective_id.objective_id,
            'created_by':program_obj.program_created_by,
            'updated_by':program_obj.program_updated_by,    
            'created_date':program_obj.program_created_date.strftime('%m/%d/%y'),
            'updated_date':program_obj.program_updated_date.strftime('%m/%d/%y'),
            'status':program_obj.program_status,            
            'objective_list':objective_list , 
            'list_workout':program_workout_list,
            'workout_list':all_workout_list         
            }    
    except Exception,e:
        print 'Exception ',e	
	data = {'success':'false'}
    return render(request,'edit-program.html',data)
   



def get_program_list(request):
	#pdb.set_trace()
        Program_list =[]
        try:
            programs = ProgramMaster.objects.all()           
            for program in programs: 
             	 edit =   '<a href="/view-program/?program_id='+ str(program.program_id)  +'" class="table-link"> '+ '<span class="fa-stack">' + '<i class="fa fa-square fa-stack-2x"></i> <i class="fa fa-search-plus fa-stack-1x fa-inverse"></i> </span> </a>'           	
                 Program_list.append({'program_name': program.program_name,'program_status':program.program_status, 'total_workout':get_workout_no(program),'total_exercises':get_execirses_no(program),'program_updated_date':program.program_updated_date.strftime("%d/%m/%Y"),'edit':edit })
                 data = {'data': Program_list}         
        except Exception, e:
            print 'Exception : ',e
            data = {'data': 'none'}   
        return HttpResponse(json.dumps(data), content_type='application/json')
        
        
        
def get_workout_no(program):
        workout_no=0;
        try:
            workout_no = ProgramWorkoutMap.objects.all().filter(program_id=program.program_id).count();   
            print workout_no;              
        except Exception, e:
            print 'Exception : ',e  
        return workout_no;
        
        
        
def get_execirses_no(program):
        execirses_no=0;
        try:
            program_workouts = ProgramWorkoutMap.objects.all().filter(program_id=program.program_id);
            for program_workout in program_workouts:
            	execirses_no=execirses_no+WorkoutExerciseMap.objects.all().filter(workout_id=program_workout.workout_id ).count();              
        except Exception, e:
            print 'Exception : ',e  
        return execirses_no;
       
       
       
        
def add_program(request):
    objective_list=[]
    workout_list=[]
    try:
    	
        objective_objes=ObjectiveMaster.objects.all()
        workout_objs=Workout.objects.all()  
        for workot in workout_objs: 
        		workout_list.append({'workout_id':workot.workout_id,'workout_name':workot.workout_name,
        		'workout_time':workot.workout_total_time,'workout_execises':workot.workout_total_no_execise})
         	 
        for objective in objective_objes:
            objective_list.append({'objective_id':objective.objective_id, 'objective':objective.objective_name})       
    
    except Exception,e:
        print 'Exception ',e
    data={
            'success':'true','objecitve_list': objective_list,'workout_list':workout_list                    
            } 
    return render(request,'add-program.html',data)

def view_program(request):
    try:   
        #pdb.set_trace()
        program_obj = ProgramMaster.objects.get(program_id= request.GET.get('program_id'))          
        workout_list = ProgramWorkoutMap.objects.filter(program_id=program_obj) 
        program_workout_list=[]
        for program_workout in workout_list:         		
            temp_workout={
                       'time':program_workout.workout_id.workout_total_time,'days':program_workout.program_workout_day,'workout_name':program_workout.workout_id.workout_name,'execises':program_workout.workout_id.workout_total_no_execise,'intensity':program_workout.workout_id.workout_intensity
                        }
            program_workout_list.append(temp_workout)
                
        data = {
            'success':'true','program_id': program_obj.program_id,'program_name': program_obj.program_name,
            'gym_access' : program_obj.program_gym_access, 'gender' : program_obj.program_user_gender,
            'days':program_obj.program_total_days,'objective':program_obj.program_user_objective_id,
            'created_by':program_obj.program_created_by,
            'updated_by':program_obj.program_updated_by,    
            'created_date':program_obj.program_created_date.strftime('%m/%d/%y'),
            'updated_date':program_obj.program_updated_date.strftime('%m/%d/%y'),
            'status':program_obj.program_status,
            'list_workout':program_workout_list           
            }    
    except Exception,e:
        print 'Exception ',e	
	data = {'success':'false'}
    return render(request,'view-program.html',data)

@csrf_exempt
def save_program(request):
##    pdb.set_trace()
    try:
        print 'NEW_PROGRAM'
        if request.method == 'POST':
            program_obj  = ProgramMaster( 
            program_name = request.POST.get('program_name'),
            program_total_days = request.POST.get('program_total_days'),
            program_gym_access = request.POST.get('program_gym_access'),
            program_user_gender = request.POST.get('program_user_gender'),
            program_user_objective_id = ObjectiveMaster.objects.get(objective_id=request.POST.get('program_user_objective_id')), 
           	program_created_date=datetime.datetime.now(), 
           	program_created_by='vikram singh chandel',
           	program_updated_by='vikram singh chandel'           	           	
            )   
            program_obj.save()  
            
            programwk_list = request.POST.get('program_workout_list')
            programwk_day_list = request.POST.get('program_workout_day_list')
            print programwk_list
            programwk_list = programwk_list.split(',')
            programwk_day_list = programwk_day_list.split(',')
            i=0;
            for pgwk_id in programwk_list:                  
                program_work_obj = ProgramWorkoutMap(
                    program_id   = program_obj,
                    workout_id  = Workout.objects.get(workout_id=pgwk_id), 
                    program_workout_day=programwk_day_list[i],  
                    workout_program_created_date = datetime.datetime.now(),
                    workout_program_created_by ='vikram singh chandel',
                    workout_program_updated_by ='vikram singh chandel'                 
                    )
                i=i+1
                program_work_obj.save()
            data = { 'success':'true'}
            print data
        else:
            data = {'success': 'false'}
    except Exception, e:
            print 'Exception :' ,e    
            data = {'data':'none'}
            
    return render(request,'programs.html',data)	
  
    
def delete_program_workout(request):
    try:
        program_workout= ProgramWorkoutMap(program_workout_id = request.GET.get('program_workout_id'))  
        program_workout.delete()
        data = {'success':'true'}
    except Exception,e:
        print 'Exception ',e    
    return HttpResponse(json.dumps(data), content_type='application/json') 
   
   
def add_program_workout(request):   
    try:
        program_obj    = ProgramMaster.objects.get(program_id=request.GET.get('program_id'))
        workout_obj    = Workout.objects.get(workout_id=request.GET.get('workout_id'))
        program_workout_map= ProgramWorkoutMap(program_id=program_obj,workout_id=workout_obj,
                                                program_workout_day=request.GET.get('day'),
                                                workout_program_created_date = datetime.datetime.now(),
                                                workout_program_created_by ='vikram singh chandel',
                                                workout_program_updated_by ='vikram singh chandel')  
        program_workout_map.save()            
        data = { 'success':'true', 'error_message':'Successfully Added '}
    except Exception,e:
        print 'Exception : ' , e
        data = {'success':'false', 'error_message': 'Failed to add instruction in exercise' }
    return HttpResponse(json.dumps(data), content_type='application/json')
	        
	        
def update_program(request):
    ##pdb.set_trace()
    try:
        print 'Update Program------>'     
        print request.POST
        print '--------------------------------------' 
        program_obj = ProgramMaster.objects.get(program_id=request.POST.get('program_id_test'))
        program_obj.program_name = request.POST.get('program_name')      
        program_obj.program_user_objective_id = ObjectiveMaster.objects.get(objective_id=request.POST.get('program_user_objective_id'))
        program_obj.program_total_days = request.POST.get('program_total_days')       
        program_obj.program_gym_access = request.POST.get('program_gym_access')      
        program_obj.program_user_gender = request.POST.get('program_user_gender')
        program_obj.program_status = request.POST.get('status_combo')
        program_obj.program_updated_date=datetime.datetime.now()
        program_obj.program_updated_by='vikram singh chandel'
        program_obj.save()
    except Exception,e:
        print 'Exception ',e
        data = {'data':'none'}
    return render(request,'programs.html') 
    
    
def get_workout_by_intensity(request):
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
