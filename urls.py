from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from trainmefit_project import settings

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'trainmefitapp.views.user_apis.home', name='home'),
    url(r'^dashboard/', 'trainmefitapp.views.user_apis.open_dashboard', name='dashboard'),
    # User OR Customer related API's
    url(r'^adlogin/', 'trainmefitapp.views.user_apis.admin_login', name='admin_login'),
    url(r'^user-login/', 'trainmefitapp.views.user_apis.user_login', name='user_login'),
    url(r'^sign-out-admin/', 'trainmefitapp.views.user_apis.signOutAdmin', name='signOutAdmin'),
    url(r'^sign-out-user/', 'trainmefitapp.views.user_apis.signOutUser', name='signOutUser'),
    url(r'^user-section/', 'trainmefitapp.views.user_apis.user_page', name='user_page'),
    url(r'^user-detail-page/', 'trainmefitapp.views.customers.user_details_page', name='user_details_page'),
    url(r'^get-customer-list/','trainmefitapp.views.customers.get_customer_list',name='get_customer_list'),
    url(r'^forgot-password/', 'trainmefitapp.views.user_apis.forgot_password', name='forgot_password'),
    url(r'^add-customer-program/','trainmefitapp.views.customers.customer_program',name='customer_program'),    
    url(r'^customer-edit-program/','trainmefitapp.views.customers.view_edit_customer_program',name='customer_edit_program'), 
    url(r'^get-customer-programs/','trainmefitapp.views.customers.get_customer_programs',name='customer_edit_program'),   
    url(r'^view-customer-program/','trainmefitapp.views.customers.view_customer_program',name='view_customer_program'),   
    url(r'^get-workout-by-intensity-for-customer/','trainmefitapp.views.customers.get_workout_by_intensity_for_customer',name='get_workout_by_intensity_for_customer'),
    url(r'^add-program-workout-for-customer/','trainmefitapp.views.customers.add_program_workout_for_customer',name='add_program_workout_for_customer'),
    url(r'^delete-program-workout-for-customer/','trainmefitapp.views.customers.delete_program_workout_for_customer',name='delete_program_workout_for_customer'),      
    url(r'^update-user-program/','trainmefitapp.views.customers.update_user_program',name='update_user_program'),      
    url(r'^add-customer-programs/', 'trainmefitapp.views.customers.add_customer_programs', name='add-program-workout'),
    url(r'^check-program-duration/', 'trainmefitapp.views.customers.check_program_duration', name='check_program_duration'),
    
    
    
    #Exercise related API's
    url(r'^exercise-list/','trainmefitapp.views.exercises.exercise_list',name='exercise_list'),
    url(r'^view-exercise/','trainmefitapp.views.exercises.view_exercise',name='view_exercise'),
    url(r'^edit-exercise/','trainmefitapp.views.exercises.edit_exercise',name='edit_exercise'),
    url(r'^add-exercise/','trainmefitapp.views.exercises.add_exercise_page',name='add_exercise_page'),
    url(r'^get-exercises-list/','trainmefitapp.views.exercises.get_exercises_list',name='exercises_list'),
    #url(r'^get-bodypart/','trainmefitapp.views.exercises.get_bodypart',name='get_bodypart'),
    url(r'^save-exercise/','trainmefitapp.views.exercises.save_exercise',name='save_exercise'),
    url(r'^update-exercise/','trainmefitapp.views.exercises.update_exercise',name='update_exercise'),
    url(r'^delete-instruction-from-exercise/','trainmefitapp.views.exercises.delete_instruction_in_exercise',name='instruction'), 
    url(r'^add-instruction-in-exercise/','trainmefitapp.views.exercises.add_instruction_in_exercise',name='instruction'),

    
    #Workout Related API's
     url(r'^workout/','trainmefitapp.views.workout.workout',name='workout'), 
     url(r'^add-workout/','trainmefitapp.views.workout.add_workout',name='workout'),
     url(r'^edit-workout/','trainmefitapp.views.workout.edit_workout',name='workout'),
     url(r'^view-workout/','trainmefitapp.views.workout.view_workout',name='workout'),
     url(r'^get-workout-list/','trainmefitapp.views.workout.get_workout_list',name='workout'),
     url(r'^get-exercises-by-bodypart/','trainmefitapp.views.exercises.get_exercise_by_bodypart',name='get_exercise_by_bodypart'),    
     url(r'^save-workout/','trainmefitapp.views.workout.save_workout',name='save_workout'), 
     url(r'^update-workout/','trainmefitapp.views.workout.update_workout',name='update_workout'),
     url(r'^add-exercise-in-workout/','trainmefitapp.views.workout.add_exercise_in_workout',name='workout'),
     url(r'^delete-exercise-from-workout/','trainmefitapp.views.workout.delete_exercise_in_workout',name='workout'),
    


##    url(r'^workout/','trainmefitapp.views.workout.workout',name='workout'), 
##    url(r'^add-workout/','trainmefitapp.views.workout.add_workout',name='workout'),
##    url(r'^edit-workout/','trainmefitapp.views.workout.edit_workout',name='workout'),
##    url(r'^view-workout/','trainmefitapp.views.workout.view_workout',name='workout'),
##    url(r'^get-workout-list/','trainmefitapp.views.workout.get_workout_list',name='workout'),
##    url(r'^get-exercises-by-bodypart/','trainmefitapp.views.exercises.get_exercise_by_bodypart',name='get_exercise_by_bodypart'),    
##    url(r'^save-workout/','trainmefitapp.views.workout.save_workout',name='save_workout'), 
##    url(r'^update-workout/','trainmefitapp.views.workout.update_workout',name='update_workout'),
##    url(r'^add-exercise-in-workout/','trainmefitapp.views.workout.add_exercise_in_workout',name='workout'),
##    url(r'^delete-exercise-from-workout/','trainmefitapp.views.workout.delete_exercise_in_workout',name='workout'),
    url(r'^check-exist-exercise/','trainmefitapp.views.workout.check_exist_exercise_form',name='workout'),
    url(r'^edit-workout-exercise/','trainmefitapp.views.workout.edit_workout_exercise',name='workout'),

    #Payment Related API's
    url(r'^payments/','trainmefitapp.views.payments.payment',name='payments'),
    
    #Master Related API's
    url(r'^master/','trainmefitapp.views.master.master',name='master'),
   
    #Service Related API's
    url(r'^services/','trainmefitapp.views.services.service',name='services'),
    
    # Program Related APis'
    url(r'^program-list/', 'trainmefitapp.views.program_apis.program_list', name='program_list'),
    url(r'^add-program/', 'trainmefitapp.views.program_apis.add_program', name='add-program'),
    url(r'^view-program/', 'trainmefitapp.views.program_apis.view_program', name='view-program'),
    url(r'^edit-program/', 'trainmefitapp.views.program_apis.edit_program', name='edit-program'),
    url(r'^get-program-list/', 'trainmefitapp.views.program_apis.get_program_list', name='program-list'),
    url(r'^add-new-program/', 'trainmefitapp.views.program_apis.save_program', name='add-a-program'),
    url(r'^delete-program-workout/', 'trainmefitapp.views.program_apis.delete_program_workout', name='delete-program-workout'),
    url(r'^add-program-workout/', 'trainmefitapp.views.program_apis.add_program_workout', name='add-program-workout'),
    url(r'^update-program/', 'trainmefitapp.views.program_apis.update_program', name='update-program'),
    url(r'^get-workout-by-intensity/', 'trainmefitapp.views.program_apis.get_workout_by_intensity', name='update-program'),
    
    
    url(r'^admin/', include(admin.site.urls)),
    
    # These are mobile related  URL and APIs
    url(r'^user-sign-up/','trainmefitapp.views.user_apis.sign_up_end_user',name='sign_up_end_user'),
    
    url(r'^test/','trainmefitapp.views.master.mttest',name='test'), 
    
    # Edit-Mode API's
    url(r'^edit-mode/','trainmefitapp.views.edit-mode.edit_data',name='edit_data'),


# alll apis for ios app    

   
    url(r'^login/', 'restmobileapp.tmfapi.mobile_login',name='login'),
    url(r'^signup/','restmobileapp.tmfapi.sign_up',name='sign_up'),
    url(r'^editprofile/','restmobileapp.tmfapi.edit_profile',name='edit_profile'),
    url(r'^workoutinfo/','restmobileapp.tmfapi.save_user_workout_info',name='save_workout'),
    url(r'^getworkoutinfo/','restmobileapp.tmfapi.get_user_workout_info',name='workout_info'),
    url(r'^sampleworkout/','restmobileapp.tmfapi.get_sample_workout',name='sample_workout'),
    url(r'^myexercise/','restmobileapp.tmfapi.get_exercise_details',name='exercise_details'),
    url(r'^googlesignup/','restmobileapp.tmfapi.google_sign_up',name='sign_up'),
    url(r'^todayworkout/','restmobileapp.tmfapi.get_workout_of_day',name='todayworkout'),
    url(r'^getmyexercise/','restmobileapp.tmfapi.get_exercise_details',name='getmyexercise'),
    url(r'^restdaychallenges/','restmobileapp.tmfapi.get_restday_challenges',name='getmyexercise'),
    url(r'^getschedule/','restmobileapp.tmfapi.get_workout_schedule',name='getschedule'),
    url(r'^contactus/','restmobileapp.tmfapi.send_contact_mail',name='contactus'),
    url(r'^forget-pwd/','restmobileapp.tmfapi.redirect_to_reset_password_page',name='forget-pwd'),
    url(r'^update-password/','restmobileapp.tmfapi.update_new_password', name='update_password'),
    url(r'^forgetpassword/','restmobileapp.tmfapi.send_password_reset_mail', name='reset_password'),
    url(r'^restexercise/','restmobileapp.tmfapi.get_rest_exercise_details', name='reset_password'),

 

)+ static( settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
