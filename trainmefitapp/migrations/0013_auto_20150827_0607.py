# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('trainmefitapp', '0012_auto_20150827_0600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bodypartmaster',
            name='body_part_updated_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 27, 6, 7, 21, 218407)),
        ),
        migrations.AlterField(
            model_name='excerciseimage',
            name='exercise_image_updated_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 27, 6, 7, 21, 220694)),
        ),
        migrations.AlterField(
            model_name='excercisevideo',
            name='exercise_video_updated_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 27, 6, 7, 21, 219103)),
        ),
        migrations.AlterField(
            model_name='exercise',
            name='exercise_updated_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 27, 6, 7, 21, 219845)),
        ),
        migrations.AlterField(
            model_name='instructionmaster',
            name='instruction_updated_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 27, 6, 7, 21, 221394)),
        ),
        migrations.AlterField(
            model_name='membershipmaster',
            name='membership_updated_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 27, 6, 7, 21, 215580)),
        ),
        migrations.AlterField(
            model_name='objectivemaster',
            name='objective_updated_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 27, 6, 7, 21, 216232)),
        ),
        migrations.AlterField(
            model_name='programmaster',
            name='program_updated_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 27, 6, 7, 21, 222895)),
        ),
        migrations.AlterField(
            model_name='programworkoutmap',
            name='workout_program_updated_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 27, 6, 7, 21, 224459)),
        ),
        migrations.AlterField(
            model_name='restchallenges',
            name='rest_challenge_updated_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 27, 6, 7, 21, 229452)),
        ),
        migrations.AlterField(
            model_name='sampleworkout',
            name='sample_workout_updated_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 27, 6, 7, 21, 228827)),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user_updated_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 27, 6, 7, 21, 217133)),
        ),
        migrations.AlterField(
            model_name='userprogramexercisemap',
            name='exercise_id',
            field=models.ForeignKey(related_name='user_program_exercise', to='trainmefitapp.Exercise', null=True),
        ),
        migrations.AlterField(
            model_name='userprogramexercisemap',
            name='user_program_exercise_updated_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 27, 6, 7, 21, 227361)),
        ),
        migrations.AlterField(
            model_name='userprogrammap',
            name='user_program_updated_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 27, 6, 7, 21, 225396)),
        ),
        migrations.AlterField(
            model_name='userprogramworkoutmaster',
            name='user_program_workout_updated_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 27, 6, 7, 21, 226279)),
        ),
        migrations.AlterField(
            model_name='workout',
            name='workout_updated_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 27, 6, 7, 21, 222186)),
        ),
    ]
