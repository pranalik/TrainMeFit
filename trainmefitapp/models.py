from django.db import models
from django.contrib.auth.models import User
import datetime
from django.core.exceptions import ValidationError
# from django.forms.fields import email_re

# Create your models here.

EXC_VIDEO_PATH='exercise_video/'
CAM_IMAGES_PATH ='customer_images/'
EXCERCISE_IMAGE_PATH='exercise_images'
SERVER_MEDIA_URL = 'http://192.168.0.121:8000'



GYM_ACCESS = (
    ('Yes','Yes'),
    ('No','No')
)

INTENSITY = (
    ('Easy','Easy'),
    ('Medium','Medium'),
    ('Hard','Hard')
)

GENDER = (
    ('Male','Male'),
    ('Female','Female')
)



ROW_STATUS = (
    ('Active','Active'),
    ('Inactive','Inactive')
)

EXERCISE_STATUS = (
    ('ACTIVE','ACTIVE'),
    ('INACTIVE','INACTIVE')
)

PAYMENT_STATUS = (
    ('ACTIVE','ACTIVE'),
    ('INACTIVE','INACTIVE')
)

WORKOUT_DIFFICULTY =(
    (0,'HIGH'),
    (1,'MEDIUM'),
    (2,'LOW')
)

PAYMENT_MODE =(
    ('CASH','CASH'),
    ('NETBANKING','NETBANKING'),
    ('DEBIT CARD','DEBIT CARD'),
    ('CREDIT CARD','CREDIT CARD'),
    ('CHEQUE','CHEQUE')   
)

PAYMENT_MONTH = (
    (0,'JANUARY'),
    (1,'FEBRUARY'),
    (2,'MARCH'),
    (3,'APRIL'),
    (4,'MAY'),
    (5,'JUNE'),
    (6,'JULY'),
    (7,'AUGUST'),
    (8,'SEPTEMBER'),
    (9,'OCTOBER'),
    (10,'NOVEMBER'),
    (11,'DECEMBER')
)




# The Mebership Details tables, Which will contain different type of membership
class MembershipMaster(models.Model):
    membership_id                = models.AutoField(primary_key=True )
    membership_type              = models.CharField(max_length=70)
    membership_duration          = models.CharField(max_length=50)
    membership_description       = models.CharField(max_length=70)
    membership_created_by        = models.CharField(max_length=50,null=True)
    membership_updated_by        = models.CharField(max_length=50,null=True)
    membership_created_date      = models.DateTimeField(null=True)
    membership_updated_date      = models.DateTimeField(default=datetime.datetime.now())
    membership_status            = models.CharField(max_length=50,default='Active', choices= ROW_STATUS,blank=True)


    def __unicode__(self):
        return unicode(self.membership_type)

      
class ObjectiveMaster(models.Model):

    objective_id                         = models.AutoField(primary_key=True) 
    objective_name                       = models.CharField(max_length=50,null=True)
    objective_created_by                 = models.CharField(max_length=50,null=True)
    objective_updated_by                 = models.CharField(max_length=50,null=True)
    objective_created_date               = models.DateTimeField(null=True)
    objective_updated_date               = models.DateTimeField(default=datetime.datetime.now())
    objective_status                     = models.CharField(max_length=50,default='Active', choices= ROW_STATUS,blank=True)

    def __unicode__(self):
        return unicode(self.objective_name)  



class UserProfile(User):
  
    user_id                       = models.CharField(max_length=100,null=True,unique=True)
    user_first_name               = models.CharField(max_length=50,null=True,blank=True)
    user_last_name                = models.CharField(max_length=40,null=True,blank=True)
    user_phone_number             = models.CharField(max_length=50, null=True,blank=True)
    user_gender                   = models.CharField(max_length=50,default=True, choices= GENDER,blank=True)
    user_dob                      = models.DateField("Date Of Birth",null=True,blank=True )
    user_city                     = models.CharField(max_length=50,null=True,blank=True)
    user_state                    = models.CharField(max_length=50,null=True,blank=True)
    user_country                  = models.CharField(max_length=50,null=True,blank=True)
    user_sign_up_source           = models.CharField(max_length=10,blank=True)
    user_height                   = models.FloatField(null=True,blank=True)
    user_weight                   = models.FloatField(null=True,blank=True)
    user_objective_id             = models.ForeignKey(ObjectiveMaster,related_name='user_objective',null=True)
    user_membership_id            = models.ForeignKey(MembershipMaster,related_name='user_membership',null=True)
    user_gym_access               = models.CharField(max_length=50,default=True, choices= GYM_ACCESS,blank=True)
    user_workouts_per_week        = models.PositiveIntegerField(default=3,blank=True)
    user_leg_press_weight_lift    = models.FloatField(null=True,blank=True)
    user_bench_press_weight_lift  = models.FloatField(null=True,blank=True)
    user_bicep_curls_weight_lift  = models.FloatField(null=True,blank=True)
    user_workout_intensity        = models.CharField(max_length=50,default=False, choices= INTENSITY,blank=True)
    user_membership_status        = models.CharField(max_length=10,null=True,blank=True)
    user_profile_picture          = models.ImageField("Image",upload_to=CAM_IMAGES_PATH,max_length=255, default=None)
    user_created_by               = models.CharField(max_length=50,null=True)
    user_updated_by               = models.CharField(max_length=50,null=True)
    user_created_date             = models.DateTimeField(null=True)
    user_updated_date             = models.DateTimeField(default=datetime.datetime.now())
    user_status                   = models.CharField(max_length=50,default='Active', choices= ROW_STATUS,blank=True)

    def __unicode__(self):
        return unicode(self.username)

    def validate(self,data):
        print "in the validate"
        print data.username

        if not data.user_membership_id:
            raise UserProfile.DoesNotExist("Please Enter Membership Id")

        if not data.username:
            raise UserProfile.DoesNotExist("Please Enter Valid Username")

        if not data.password:
            raise UserProfile.DoesNotExist("Please Enter Password")    

        if not data.user_phone_number:
            raise UserProfile.DoesNotExist("Please Enter Phone Number")
        elif len(data.user_phone_number)!=10:
            raise UserProfile.DoesNotExist("Please Enter 10 digits For Phone Number")
        else:
            pass

        return True


    def validate_profile(self,data):
        print "in the validate_profile"
        print data.user_objective_id

        if not data.user_objective_id:
            raise UserProfile.DoesNotExist("Please Enter Objective")

        if not data.user_gym_access:
            raise UserProfile.DoesNotExist("Please Enter Gym Access")

        if not data.user_gender:
            raise UserProfile.DoesNotExist("Please Enter Gender")    

        return True    
        

class BodyPartMaster(models.Model):
    body_part_id                  = models.AutoField(primary_key=True)
    body_part_name                = models.CharField(max_length=50)
    body_part_created_by          = models.CharField(max_length=50,null=True)
    body_part_updated_by          = models.CharField(max_length=50,null=True)
    body_part_created_date        = models.DateTimeField(null=True)
    body_part_updated_date        = models.DateTimeField(default=datetime.datetime.now())
    body_part_status              = models.CharField(max_length=50,default='Active', choices= ROW_STATUS,blank=True)

    def __unicode__(self):
        return unicode(self.body_part_name)


class ExcerciseVideo(models.Model):
    exercise_video_id                = models.AutoField(primary_key=True)
    exercise_video_name              = models.CharField(max_length=50)
    #exercise_video_url               = models.FileField(max_length=50)
    exercise_video_url               = models.FileField("video",upload_to=EXC_VIDEO_PATH,max_length=255, default=None)
    exercise_video_created_by        = models.CharField(max_length=50,null=True)
    exercise_video_updated_by        = models.CharField(max_length=50,null=True)
    exercise_video_created_date      = models.DateTimeField(null=True)
    exercise_video_updated_date      = models.DateTimeField(default=datetime.datetime.now())
    exercise_video_status            = models.CharField(max_length=50,default='Active', choices= ROW_STATUS,blank=True)

    def __unicode__(self):
        return unicode(self.exercise_video_id)

class Exercise(models.Model):    
    exercise_id                     = models.AutoField(primary_key=True)
    exercise_body_part_id           = models.ForeignKey(BodyPartMaster,related_name ='exercise_body_part',null=True)
    exercise_video_id               = models.ForeignKey(ExcerciseVideo,related_name = 'exercise_video', null=True)
    exercise_name                   = models.CharField(max_length=50)
    exercise_gender                 = models.CharField(max_length=50,choices= GENDER)
    exercise_gym_access             = models.CharField(max_length=50,default=True,null=True, choices= GYM_ACCESS)
    exercise_objective_id           = models.ForeignKey(ObjectiveMaster,related_name='exercise_objective',null=True)
    exercise_time                   = models.CharField(max_length=50,null=True)
    exercise_intensity             = models.CharField(max_length=50,null=True)
    exercise_created_by            = models.CharField(max_length=50,null=True)
    exercise_updated_by            = models.CharField(max_length=50,null=True)
    exercise_created_date          = models.DateTimeField(null=True)
    exercise_updated_date          = models.DateTimeField(default=datetime.datetime.now())
    exercise_status                = models.CharField(max_length=50,default='Active', choices= ROW_STATUS,blank=True)

        
    
    def __unicode__(self):
        return unicode(self.exercise_id)    


class ExcerciseImage(models.Model):
    exercise_image_id                = models.AutoField(primary_key=True)
    exercise_id                      = models.ForeignKey(Exercise,related_name ='exercise_image',null=True)
    exercise_image_name              = models.CharField(max_length=30)
    exercise_image                   = models.ImageField("Exercise Image",upload_to=EXCERCISE_IMAGE_PATH,max_length=255, default=None, null=True)
    # exercise_image_url               = models.FileField(max_length=30)
    exercise_image_created_by        = models.CharField(max_length=20,null=True)
    exercise_image_updated_by        = models.CharField(max_length=20,null=True)
    exercise_image_created_date      = models.DateTimeField(null=True)
    exercise_image_updated_date      = models.DateTimeField(default=datetime.datetime.now())
    exercise_image_status            = models.CharField(max_length=20,default='Active', choices= ROW_STATUS,blank=True)


    def __unicode__(self):
        return unicode(self.exercise_image_id)


class InstructionMaster(models.Model):
    instruction_id                = models.AutoField(primary_key=True)
    instruction_exercise_id       = models.ForeignKey(Exercise,related_name = 'exercise_instruction', null=True)
    instruction_name              = models.CharField(max_length=50)
    instruction_created_by        = models.CharField(max_length=50,null=True)
    instruction_updated_by        = models.CharField(max_length=50,null=True)
    instruction_created_date      = models.DateTimeField(null=True)
    instruction_updated_date      = models.DateTimeField(default=datetime.datetime.now())
    instruction_status            = models.CharField(max_length=50,default='Active', choices= ROW_STATUS,blank=True)

    def __unicode__(self):
        return unicode(self.instruction_name)

class Workout(models.Model):
    workout_id                          = models.AutoField(primary_key=True)
    workout_name                        = models.CharField(max_length=50,null=True)
    workout_total_no_execise            = models.IntegerField(null=True)
    workout_total_time                  = models.CharField(max_length=50,null=True) 
    workout_intensity                   = models.CharField(max_length=50,null=True)
    workout_type                        = models.CharField(max_length=50,null=True)
    workout_created_by                  = models.CharField(max_length=50,null=True)
    workout_updated_by                  = models.CharField(max_length=50,null=True)
    workout_created_date                = models.DateTimeField(null=True)
    workout_updated_date                = models.DateTimeField(default=datetime.datetime.now())
    workout_status                      = models.CharField(max_length=50,default='Active', choices= ROW_STATUS,blank=True)
    
    
    def __unicode__(self):
        return unicode(self.workout_name)

class ProgramMaster(models.Model):
    program_id                          = models.AutoField(primary_key=True)
    program_name                        = models.CharField(max_length=50,null=True)
    program_user_objective_id           = models.ForeignKey(ObjectiveMaster,related_name='user_program_objective',null=True)
    program_user_gender                 = models.CharField(max_length=50,default=True, choices= GENDER)
    program_gym_access                  = models.CharField(max_length=50,default=True, choices= GYM_ACCESS,blank=True)
    program_total_days                  = models.IntegerField(null=True)
    program_created_by                  = models.CharField(max_length=50,null=True)
    program_updated_by                  = models.CharField(max_length=50,null=True)
    program_created_date                = models.DateTimeField(null=True)
    program_updated_date                = models.DateTimeField(default=datetime.datetime.now())
    program_status                      = models.CharField(max_length=50,default='Active', choices= ROW_STATUS,blank=True)
        
    
    def __unicode__(self):
        return unicode(self.program_name)


class WorkoutExerciseMap(models.Model):
    workout_exercise_id                          = models.AutoField(primary_key=True)
    workout_id                                   = models.ForeignKey(Workout,related_name='workout_exe_id',null=True)
    exercise_id                                  = models.ForeignKey(Exercise,related_name='exercise_workout_id',null=True)
    workout_exercise_total_sets                  = models.CharField(max_length=50,null=True)
    workout_exercise_total_reps                  = models.CharField(max_length=50,null=True)
    workout_exercise_total_time                  = models.CharField(max_length=50,null=True)
    workout_exercise_rest_time                   = models.CharField(max_length=50,null=True)
    workout_exercise_time_between_set            = models.CharField(max_length=50,null=True)
    workout_exercise_created_by                  = models.CharField(max_length=50,null=True)
    workout_exercise_updated_by                  = models.CharField(max_length=50,null=True)
    workout_exercise_created_date                = models.DateTimeField(null=True)
    workout_exercise_status                      = models.CharField(max_length=50,default='Active', choices= ROW_STATUS,blank=True)
     
    def __unicode__(self):
        return unicode(self.workout_exercise_id)


class ProgramWorkoutMap(models.Model):
    program_workout_id                          = models.AutoField(primary_key=True)
    workout_id                                  = models.ForeignKey(Workout,related_name='program_workout_id',null=True)
    program_id                                  = models.ForeignKey(ProgramMaster,related_name='workout_program_id',null=True)
    program_workout_day                         = models.CharField(max_length=50,null=True)
    workout_program_created_by                  = models.CharField(max_length=50,null=True)
    workout_program_updated_by                  = models.CharField(max_length=50,null=True)
    workout_program_created_date                = models.DateTimeField(null=True)
    workout_program_updated_date                = models.DateTimeField(default=datetime.datetime.now())
    workout_program_status                      = models.CharField(max_length=50,default='Active', choices= ROW_STATUS,blank=True)
       
    
    def __unicode__(self):
        return unicode(self.program_workout_id)



class UserProgramMap(models.Model):
    user_program_id                             = models.AutoField(primary_key=True)
    user_id                                     = models.ForeignKey(UserProfile,related_name='user_program_id',null=True)
    program_id                                  = models.ForeignKey(ProgramMaster,related_name='program_user_id',null=True)
    user_program_name                           = models.CharField(max_length=50,null=True)
    user_program_start_date                     = models.DateField(null=True)
    user_program_end_date                       = models.DateField(null=True)
    user_program_created_by                     = models.CharField(max_length=50,null=True)
    user_program_updated_by                     = models.CharField(max_length=50,null=True)
    user_program_created_date                   = models.DateTimeField(null=True)
    user_program_updated_date                   = models.DateTimeField(default=datetime.datetime.now())
    user_program_program_status                 = models.CharField(max_length=50,default='Active', choices= ROW_STATUS,blank=True)
         
    
    def __unicode__(self):
        return unicode(self.user_program_name)




class UserProgramWorkoutMaster(models.Model):
    user_program_workout_id                             = models.AutoField(primary_key=True)
    workout_id                                          = models.ForeignKey(Workout,related_name='user_programworkout_workout_id',null=True)
    user_program_id                                     = models.ForeignKey(UserProgramMap,related_name='program_user_workout_id',null=True)
    user_program_workout_name                           = models.CharField(max_length=50,null=True)
    user_program_workout_total_execise                  = models.CharField(max_length=50,null=True)          
    user_program_workout_total_time                     = models.CharField(max_length=50,null=True) 
    user_program_workout_type                           = models.CharField(max_length=50,null=True)
    user_program_workout_day                            = models.CharField(max_length=50,null=True)
    user_program_workout_intensity                      = models.CharField(max_length=50,null=True)    
    user_program_workout_created_by                     = models.CharField(max_length=50,null=True)
    user_program_workout_updated_by                     = models.CharField(max_length=50,null=True)
    user_program_workout_created_date                   = models.DateTimeField(null=True)
    user_program_workout_updated_date                   = models.DateTimeField(default=datetime.datetime.now())    
    user_program_workout_status                         = models.CharField(max_length=50,default='Active', choices= ROW_STATUS,blank=True)
  
    
    def __unicode__(self):
        return unicode(self.user_program_workout_id)  


class UserProgramExerciseMap(models.Model):
    user_program_exercise_id                            = models.AutoField(primary_key=True)
    user_program_workout_id                             = models.ForeignKey(UserProgramWorkoutMaster,related_name='user_program',null=True)
    exercise_id                                         = models.CharField(max_length=50,null=True)
    #user_program_exercise_body_part_id                  = models.CharField(max_length=50,null=True)
    user_program_exercise_body_part_id                  = models.ForeignKey(BodyPartMaster,related_name ='user_exercise_body_part',null=True)        
    user_program_exercise_video_id                      = models.ForeignKey(ExcerciseVideo,related_name ='user_exercise_video',null=True)         
    user_program_exercise_name                          = models.CharField(max_length=50,null=True)
    user_program_exercise_time                          = models.CharField(max_length=50,null=True)
    user_program_exercise_workout_total_sets            = models.CharField(max_length=50,null=True)
    user_program_exercise_workout_total_reps            = models.CharField(max_length=50,null=True)
    user_program_exercise_workout_time_between_set      = models.CharField(max_length=50,null=True)
    user_program_exercise_workout_total_time            = models.CharField(max_length=50,null=True)
    user_program_exercise_workout_rest_time             = models.CharField(max_length=50,null=True)
    user_program_exercise_created_by                     = models.CharField(max_length=50,null=True)
    user_program_exercise_updated_by                     = models.CharField(max_length=50,null=True)
    user_program_exercise_created_date                   = models.DateTimeField(null=True)
    user_program_exercise_updated_date                   = models.DateTimeField(default=datetime.datetime.now())    
    user_program_exercise_workout_status                 = models.CharField(max_length=50,default='Active', choices= ROW_STATUS,blank=True)
  
    def __unicode__(self):
        return unicode(self.user_program_exercise_id)  


class CustomerImage(models.Model):
    customer_image        = models.ImageField("Image", max_length=255, default=None)

    def __unicode__(self):
        return  str(self.customer_image)

class SampleWorkout(models.Model):
    sample_workout_id                          = models.AutoField(primary_key=True)
    sample_workout_name                        = models.CharField(max_length=50,null=True)
    sample_workout_description                 = models.CharField(max_length=50,null=True)
    sample_workout_created_by                  = models.CharField(max_length=50,null=True)
    sample_workout_updated_by                  = models.CharField(max_length=50,null=True)
    sample_workout_created_date                = models.DateTimeField(null=True)
    sample_workout_updated_date                = models.DateTimeField(default=datetime.datetime.now())
    sample_workout_status                      = models.CharField(max_length=50,default='Active', choices= ROW_STATUS,blank=True)
    
    
    def __unicode__(self):
        return unicode(self.sample_workout_name)


class RestChallenges(models.Model):
    rest_challenge_id                          = models.AutoField(primary_key=True)
    workout_id                                 = models.ForeignKey(Workout,related_name='rest_day_workout_id',null=True)
    rest_challenge_name                        = models.CharField(max_length=50,null=True)
    rest_challenge_description                 = models.CharField(max_length=50,null=True)
    rest_challenge_created_by                  = models.CharField(max_length=50,default='admin',null=True)
    rest_challenge_updated_by                  = models.CharField(max_length=50,default='admin',null=True)
    rest_challenge_created_date                = models.DateTimeField(null=True)
    rest_challenge_updated_date                = models.DateTimeField(default=datetime.datetime.now())
    rest_challenge_status                      = models.CharField(max_length=50,default='Active', choices= ROW_STATUS,blank=True)
    
    
    def __unicode__(self):
        return unicode(self.rest_challenge_id)




  




