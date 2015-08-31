# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('trainmefitapp', '0008_auto_20150826_1231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bodypartmaster',
            name='body_part_updated_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 27, 5, 57, 28, 365858)),
        ),
        migrations.AlterField(
            model_name='excerciseimage',
            name='exercise_image_updated_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 27, 5, 57, 28, 368454)),
        ),
        migrations.AlterField(
            model_name='excercisevideo',
            name='exercise_video_updated_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 27, 5, 57, 28, 366573)),
        ),
        migrations.AlterField(
            model_name='exercise',
            name='exercise_updated_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 27, 5, 57, 28, 367335)),
        ),
        migrations.AlterField(
            model_name='instructionmaster',
            name='instruction_updated_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 27, 5, 57, 28, 369185)),
        ),
        migrations.AlterField(
            model_name='membershipmaster',
            name='membership_updated_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 27, 5, 57, 28, 362891)),
        ),
        migrations.AlterField(
            model_name='objectivemaster',
            name='objective_updated_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 27, 5, 57, 28, 363617)),
        ),
        migrations.AlterField(
            model_name='programmaster',
            name='program_updated_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 27, 5, 57, 28, 370717)),
        ),
        migrations.AlterField(
            model_name='programworkoutmap',
            name='workout_program_updated_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 27, 5, 57, 28, 372356)),
        ),
        migrations.AlterField(
            model_name='restchallenges',
            name='rest_challenge_updated_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 27, 5, 57, 28, 377133)),
        ),
        migrations.AlterField(
            model_name='sampleworkout',
            name='sample_workout_updated_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 27, 5, 57, 28, 376507)),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user_updated_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 27, 5, 57, 28, 364540)),
        ),
        migrations.AlterField(
            model_name='userprogramexercisemap',
            name='exercise_id',
            field=models.ForeignKey(related_name='user_program_exercise', to='trainmefitapp.UserProgramWorkoutMaster', null=True),
        ),
        migrations.AlterField(
            model_name='userprogramexercisemap',
            name='user_program_exercise_updated_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 27, 5, 57, 28, 375089)),
        ),
        migrations.AlterField(
            model_name='userprogrammap',
            name='user_program_updated_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 27, 5, 57, 28, 373251)),
        ),
        migrations.AlterField(
            model_name='userprogramworkoutmaster',
            name='user_program_workout_updated_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 27, 5, 57, 28, 374110)),
        ),
        migrations.AlterField(
            model_name='workout',
            name='workout_updated_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 27, 5, 57, 28, 370003)),
        ),
    ]
