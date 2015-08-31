from django.db import models
from django.contrib.auth.models import User
import datetime
from datetime import datetime
# Create your models here.


GYM_ACCESS = (
    ('YES','YES'),
    ('NO','NO')
)

GENDER = (
    ('Male','Male'),
    ('Female','Female')
)

##GENERAL_FITNESS = (
##    (1,'YES'),
##    (0,'NO')
##)
##
##MUSCLE_GAIN = (
##    (1,'YES'),
##    (0,'NO')
##)
##
##WEIGHT_LOSS = (
##    (1,'YES'),
##    (0,'NO')
##)
##
##IMPROVE_STAMINA = (
##    (1,'YES'),
##    (0,'NO')
##)

FITNESS = (
    ('GENERAL_FITNESS','GENERAL_FITNESS'),
    ('MUSCLE_GAIN','MUSCLE_GAIN'),
    ('WEIGHT_LOSS','WEIGHT_LOSS'),
    ('IMPROVE_STAMINA','IMPROVE_STAMINA')
)

ROW_STATUS = (
    (1,'ACTIVE'),
    (0,'INACTIVE')
)

EXERCISE_STATUS = (
    ('ACTIVE','ACTIVE'),
    ('INACTIVE','INACTIVE')
)

WORKOUT_STATUS = (
    ('ACTIVE','ACTIVE'),
    ('INACTIVE','INACTIVE')
)

PROGRAM_STATUS = (
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
class Membership(models.Model):
    membership_id           = models.AutoField(primary_key=True )
    membership_type         = models.CharField(max_length=20)
    membership_description  = models.CharField(max_length=50)
    
    def __unicode__(self):
        return unicode(self.membership_type)

# This is for Program Detail, 
class Program(models.Model):
    program_id              = models.AutoField(primary_key=True)
    program_name            = models.CharField(max_length=40)
    program_details         = models.CharField(max_length=70)
    program_creation_date   = models.DateTimeField()
    
    def __unicode__(self):
        return unicode(self.program_name)


# This model for create user profile, this exteds the User model of Django
class UserProfile(User):
    """
    This is UserProfile Class which is for storing the details of Users.
    This class extends the Django User model.
    """
##    user_profile_id         = models.CharField(max_length=20,null=True,unique=True)
    user_profile_image      = models.ImageField(max_length=250,null=True)
    user_nick_name          = models.CharField(max_length=20,null=True)
    user_full_name          = models.CharField(max_length=40,null=True)
    sign_up_via             = models.CharField(max_length=10)
    user_secondary_email    = models.CharField(max_length=30,null=True)
    user_primary_contact    = models.CharField(max_length=20,null=True)
    user_secondary_contact  = models.CharField(max_length=20,null=True)
    user_city               = models.CharField(max_length=20,null=True)
    user_state              = models.CharField(max_length=20,null=True)
    user_country            = models.CharField(max_length=20,null=True)
    user_gender             = models.CharField(max_length=20,default=True, choices= GENDER)
    user_age                = models.PositiveIntegerField(null=True)
    user_height             = models.FloatField(null=True)
    user_weight             = models.FloatField(null=True)
    user_objective          = models.CharField(max_length=30,default=False, choices= FITNESS)
##    is_general_fitness      = models.BooleanField(default=False, choices= GENERAL_FITNESS)
##    is_muscle_gain          = models.BooleanField(default=False, choices= MUSCLE_GAIN)
##    is_weight_loss          = models.BooleanField(default=False, choices= WEIGHT_LOSS)
##    is_improved_stamina     = models.BooleanField(default=False, choices= IMPROVE_STAMINA)
    is_gym_access           = models.BooleanField(default=False, choices= GYM_ACCESS)
    how_many_times_per_week = models.PositiveIntegerField(default=3)
    user_membership_type    = models.ForeignKey(Membership,related_name = 'membership', null=True)
    leg_press_weight_lift   = models.FloatField(null=True)
    bench_press_weight_lift = models.FloatField(null=True)
    bicep_curls_weight_lift = models.FloatField(null=True)
    user_program_id         = models.ForeignKey(Program,related_name = 'program', null=True)
    sign_up_source          = models.CharField(max_length=10,null=True)
    creation_date           = models.DateTimeField(auto_now_add=True, blank=True)
    updated_time            = models.DateTimeField(auto_now_add=True, blank=True)
    updated_by              = models.CharField(max_length=20,null=True)
    user_row_status         = models.BooleanField(default=True,choices= ROW_STATUS)
    
    
    def __unicode__(self):
        return unicode(self.first_name+' '+self.last_name)


class Workout(models.Model):
    workout_id                          = models.AutoField(primary_key=True)
    workout_name                        = models.CharField(max_length=30,null=True)
    number_of_exercise_in_chest         = models.IntegerField(null=True)
    number_of_exercise_in_shoulders     = models.IntegerField(null=True)
    number_of_exercise_in_bicep         = models.IntegerField(null=True)
    number_of_exercise_in_tricep        = models.IntegerField(null=True)
    number_of_exercise_in_legs          = models.IntegerField(null=True)
    number_of_exercise_in_abs           = models.IntegerField(null=True)
    number_of_exercise_in_back          = models.IntegerField(null=True)
    number_of_exercise_in_circuit_hard  = models.IntegerField(null=True)
    number_of_exercise_in_circuit_easy  = models.IntegerField(null=True)
    workout_day                         = models.IntegerField(null=True)
    approximate_workout_time            = models.TimeField(null=True)
    date_updated                        = models.DateTimeField(auto_now_add=True, blank=True)
    user_row_status                     = models.CharField(max_length=20,default=True,choices= WORKOUT_STATUS)
    number_of_exercises                 = models.IntegerField(null=True)    
    
    def __unicode__(self):
        return unicode(self.workout_name)


class ExcerciseVideo(models.Model):
    
    exercise_video_id      = models.AutoField(primary_key=True)
    exercise_video_name    = models.CharField(max_length=30)
    exercise_video_url     = models.FileField(max_length=30)
    
    def __unicode__(self):
        return unicode(self.exercise_video_name)


class BodyPart(models.Model):
    body_part_id            = models.AutoField(primary_key=True)
    exercise_body_part_name =  models.CharField(max_length=30)
    
    def __unicode__(self):
        return unicode(self. exercise_body_part_name)


class Category(models.Model):
      exercise_category_id            = models.AutoField(primary_key=True)
      exercise_category_name          = models.CharField(max_length=30)
    
      def __unicode__(self):
        return unicode(self.exercise_category_name)

class Exercise(models.Model):
    
    exercise_id            = models.AutoField(primary_key=True)
    body_part_id           = models.ForeignKey(BodyPart,related_name ='exercise_body',null=True)
    exercise_video_id      = models.ForeignKey(ExcerciseVideo,related_name = 'exercisevideo', null=True)
    exercise_name          = models.CharField(max_length=30)
    exercise_status        = models.CharField(max_length=20,null=True,choices= EXERCISE_STATUS)
    exercise_instruction   = models.TextField(max_length=150)
    exercise_gender        = models.CharField(max_length=20,choices= GENDER)
    is_gym_exercise        = models.CharField(max_length=20,default=True,choices= GYM_ACCESS)
    exercise_category      = models.ForeignKey(Category,related_name = 'exercisecategory', null=True)
    exercise_time          = models.TimeField(null=True)
        
    
    def __unicode__(self):
        return unicode(self.exercise_id)


    
class WorkoutDifficultyLevel(models.Model):
    workout_difficulty_level_id =models.AutoField(primary_key=True)
    workout_id                  =models.ForeignKey(Workout,related_name='workoutdiff')
    workout_difficulty_level    =models.CharField(max_length=20,default=False,choices= WORKOUT_DIFFICULTY)
    description                 =models.TextField(max_length=230)    
    exercise_sets               =models.IntegerField()
   
    def __unicode__(self):
        return unicode(self.workout_difficulty_level_id)
    
    
class Warmup(models.Model):
    warmup_id    = models.AutoField(primary_key=True)
    warmup_name  = models.CharField(max_length=50)
    warmup_time  = models.TimeField(null=True)

    def __unicode__(self):
        return unicode(self.warmup_name)

class Payment(models.Model):
    payment_id              = models.AutoField(primary_key=True)
    user_id                 = models.ForeignKey(User,related_name='pay',null=True)
    payment_mode            = models.CharField(max_length=20,default=False,choices=PAYMENT_MODE)
    payment_amount          = models.CharField(max_length=20)
    payment_made_amount     = models.CharField(max_length=20)   
    payment_due_amount      = models.CharField(max_length=20)
 #   payment_membership      = models.ForeignKey(Membership,related_name ='membership',null=True)
    payment_status          = models.CharField(max_length=20,default=False,choices=PAYMENT_STATUS)
    payment_month           = models.CharField(max_length=20,default=False,choices=PAYMENT_MONTH )
    transaction_number      = models.CharField(max_length=30)
    payment_against_month   = models.CharField(max_length=20,default=False,choices=PAYMENT_MONTH )
    payment_datetime        = models.DateTimeField(auto_now_add=True, blank=True)
    
    def __unicode__(self):
        return unicode(self.payment_id)
   
class UserWorkout(models.Model):
    
    userworkout_id          = models.AutoField(primary_key=True)
    user_id                 = models.ForeignKey(User,related_name='user_workout',null=True)
    program_id              = models.ForeignKey(Program,related_name='userworkout_program',null=True)             
    workout_number          = models.IntegerField(null=True)
    no_in_chest             = models.IntegerField(null=True) 
    no_in_shoulders         = models.IntegerField(null=True)
    no_in_bicep             = models.IntegerField(null=True)
    no_in_tricep            = models.IntegerField(null=True)
    no_in_legs              = models.IntegerField(null=True)
    no_in_abs               = models.IntegerField(null=True)
    no_in_back              = models.IntegerField(null=True)
    no_in_circuit_hard      = models.IntegerField(null=True)
    no_in_circuit_easy     = models.IntegerField(null=True)

    def __unicode__(self):
        return unicode(self.userworkout_id)
    
class UserExerciseStatus(models.Model):
    
    generated_id       = models.AutoField(primary_key=True)
    user_id            = models.ForeignKey(User,related_name='userexer',null=True)
    program_id         = models.ForeignKey(Program,related_name='userexercise_program',null=True)   
    workout_id         = models.ForeignKey(Workout,related_name='userexercise_workout',null=True)
    exercise_id        = models.ForeignKey(Exercise,related_name='userexercise_exer')
    estimated_time     = models.IntegerField(null=True)
    date               = models.DateField(max_length=15)

    def __unicode__(self):
        return unicode(self.generated_id)
    
class UserWorkoutExercise(models.Model):
    
    userworkoutexercise_id = models.AutoField(primary_key=True)
    userworkout_id         = models.ForeignKey(UserWorkout,related_name='user_workout_exercise',null=True)
    exercise_id            = models.ForeignKey(Exercise,related_name='user_workoutexercise')

    def __unicode__(self):
        return unicode(self.userworkoutexercise_id)
    
class UserExerciseInputs(models.Model):
      user_id                   = models.CharField(max_length=20,null=True)
      user_workout_exercise_id  = models.CharField(max_length=20,null=True)
    
      def __unicode__(self):
        return unicode(self.user_id)
 
class UserProgram(models.Model):
    user_program_id        = models.AutoField(primary_key=True) 
    user_id                = models.ForeignKey(User,related_name='userprogram',null=True)
    program_id             = models.ForeignKey(Program,related_name='user_program',null=True)
    day                    = models.CharField(max_length=10,null=True)
    program_status         = models.CharField(max_length=20,null=True,choices= PROGRAM_STATUS) 
    date_updated           = models.DateField(default=datetime.now,null=True,blank=True) 
    
 

    def __unicode__(self):
        return unicode(self.user_id)
    
class ProgramWorkout(models.Model):
    programworkout_id     = models.AutoField(primary_key=True)
    program_id            = models.ForeignKey(Program,related_name='program_workout',null=True)  
    workout_id            = models.ForeignKey(Workout,related_name='programworkout',null=True)
    
    def __unicode__(self):
        return unicode(self.programworkout_id)

class WorkoutExercise(models.Model):
    workoutexercise_id    = models.AutoField(primary_key=True)
    workout_id            = models.ForeignKey(Workout,related_name='workoutexer')
    exercise_id           = models.ForeignKey(Exercise,related_name='workout_exercise')
    
    class Meta:
        unique_together = ('workout_id','exercise_id') 

    def __unicode__(self):
        return unicode(self.workoutexercise_id)

class UserExercise(models.Model):
    
    userexercise_id           = models.AutoField(primary_key=True) 
    program_id                = models.ForeignKey(Program,related_name='user_exercise_program',null=True)
    user_id                   = models.ForeignKey(User,related_name='user_exercise',null=True)
    workout_id                = models.ForeignKey(Workout,related_name='user_exercise_workout')
    exercise_id               = models.ForeignKey(Exercise,related_name='user_exercis')
    
    def __unicode__(self):
        return unicode(self.userexercise_id)


    
    
   
    
