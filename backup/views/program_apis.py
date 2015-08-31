from django.shortcuts import render
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.cache import cache_control
from django.contrib import auth


from django.http import HttpResponse
from django.http import HttpResponseRedirect

# importing constants
from constants import AppUserConstants, ExceptionLabel
from trainmefitapp.models import *


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def program_list(request):
    return render_to_response('programs.html')

def view_program(request):
    return render_to_response('view-program.html')

def edit_program(request):
    return render_to_response('edit-program.html')

##def get_program_list(request):
##    
##    try:
##        print 'Program List'  
##        program_list = Program.objects.all()
##        prprogram_listog_list = []
##        for program in program_list:
##            
##            edit =   '<a href="/edit-exercise/?exercise_id='+ str(program.program_id)  +'" class="table-link"> '+ '<span class="fa-stack">' + '<i class="fa fa-square fa-stack-2x"></i> <i class="fa fa-pencil fa-stack-1x fa-inverse"></i> </span> </a>'
##
##            temp_obj={
##                'program_name':program.program_name,
##                'category':exercise.exercise_category.exercise_category_name,
##                'gender':exercise.exercise_gender ,
##                'bodypart':exercise.body_part_id.exercise_body_part_name, 
##                'video':video,
##                'edit':edit
##            } 
##            exer_list.append(temp_obj)
##        data = {'data': exer_list}
##        
##    except Exception, e:
##        print 'Exception : ', e    
##        data = {'data':'none'}
##    return HttpResponse(json.dumps(data), content_type='application/json') 