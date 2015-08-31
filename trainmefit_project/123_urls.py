from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'trainmefitapp.views.user_apis.home', name='home'),
    url(r'^dashboard/', 'trainmefitapp.views.user_apis.open_dashboard', name='dashboard'),
    # User related API's
    url(r'^adlogin/', 'trainmefitapp.views.user_apis.admin_login', name='admin_login'),
    url(r'^user-login/', 'trainmefitapp.views.user_apis.user_login', name='user_login'),
    url(r'^sign-out-admin/', 'trainmefitapp.views.user_apis.signOutAdmin', name='signOutAdmin'),
    url(r'^sign-out-user/', 'trainmefitapp.views.user_apis.signOutUser', name='signOutUser'),
    url(r'^user-section/', 'trainmefitapp.views.user_apis.user_page', name='user_page'),
    url(r'^user-detail-page/', 'trainmefitapp.views.user_apis.user_details_page', name='user_details_page'),
    url(r'^get-customer-list/','trainmefitapp.views.customers.get_customer_list',name='get_customer_list'),
    url(r'^forgot-password/', 'trainmefitapp.views.user_apis.forgot_password', name='forgot_password'),    
    
    #Exercise related API's
    url(r'^exercise-list/','trainmefitapp.views.exercises.exercise_list',name='exercise_list'),
    url(r'^edit-exercise/','trainmefitapp.views.exercises.edit_exercise',name='edit_exercise'),
    url(r'^add-exercise/','trainmefitapp.views.exercises.add_exercise_page',name='add_exercise_page'),
    url(r'^get-exercises-list/','trainmefitapp.views.exercises.get_exercises_list',name='exercises_list'),
    #url(r'^get-bodypart/','trainmefitapp.views.exercises.get_bodypart',name='get_bodypart'),
    url(r'^save-exercise/','trainmefitapp.views.exercises.save_exercise',name='save_exercise'),
    url(r'^update-exercise/','trainmefitapp.views.exercises.update_exercise',name='update_exercise'),
##    url(r'^home/','trainmefitapp.views.exercises.home',name='update_exercise'),

    
    #Workout Related API's
    url(r'^workout/','trainmefitapp.views.workout.workout',name='workout'), 
    url(r'^add-workout/','trainmefitapp.views.workout.add_workout',name='workout'),
    url(r'^edit-workout/','trainmefitapp.views.workout.edit_workout',name='workout'),
    url(r'^get-workout-list/','trainmefitapp.views.workout.get_workout_list',name='workout'),
    url(r'^get-exercises-by-bodypart/','trainmefitapp.views.exercises.get_exercise_by_bodypart',name='get_exercise_by_bodypart'),    
    url(r'^save-workout/','trainmefitapp.views.workout.save_workout',name='save_workout'), 
    url(r'^update-workout/','trainmefitapp.views.workout.update_workout',name='update_workout'),
    url(r'^add-exercise-in-workout/','trainmefitapp.views.workout.add_exercise_in_workout',name='workout'),
    url(r'^delete-exercise-from-workout/','trainmefitapp.views.workout.delete_exercise_in_workout',name='workout'),

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
     
    url(r'^admin/', include(admin.site.urls)),
    
    # These are mobile related  URL and APIs
    url(r'^user-sign-up/','trainmefitapp.views.user_apis.sign_up_end_user',name='sign_up_end_user'),    
    url(r'^test/','trainmefitapp.views.master.mttest',name='test'),     
    # Edit-Mode API's
    url(r'^edit-mode/','trainmefitapp.views.edit-mode.edit_data',name='edit_data'),
    

)
