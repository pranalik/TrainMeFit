# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('trainmefitapp', '0014_auto_20150827_0608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bodypartmaster',
            name='body_part_updated_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 27, 6, 11, 1, 244878)),
        ),
        migrations.AlterField(
            model_name='excerciseimage',
            name='exercise_image_updated_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 27, 6, 11, 1, 247223)),
        ),
        migrations.AlterField(
            model_name='excercisevideo',
            name='exercise_video_updated_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 27, 6, 11, 1, 245602)),
        ),
        migrations.AlterField(
            model_name='exercise',
            name='exercise_updated_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 27, 6, 11, 1, 246341)),
        ),
        migrations.AlterField(
            model_name='instructionmaster',
            name='instruction_updated_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 27, 6, 11, 1, 247999)),
        ),
        migrations.AlterField(
            model_name='membershipmaster',
            name='membership_updated_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 27, 6, 11, 1, 241616)),
        ),
        migrations.AlterField(
            model_name='objectivemaster',
            name='objective_updated_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 27, 6, 11, 1, 242262)),
        ),
        migrations.AlterField(
            model_name='programmaster',
            name='program_updated_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 27, 6, 11, 1, 249518)),
        ),
        migrations.AlterField(
            model_name='programworkoutmap',
            name='workout_program_updated_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 27, 6, 11, 1, 251048)),
        ),
        migrations.AlterField(
            model_name='restchallenges',
            name='rest_challenge_updated_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 27, 6, 11, 1, 255829)),
        ),
        migrations.AlterField(
            model_name='sampleworkout',
            name='sample_workout_updated_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 27, 6, 11, 1, 255190)),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user_updated_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 27, 6, 11, 1, 243232)),
        ),
        migrations.AlterField(
            model_name='userprogramexercisemap',
            name='user_program_exercise_updated_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 27, 6, 11, 1, 253772)),
        ),
        migrations.AlterField(
            model_name='userprogrammap',
            name='user_program_updated_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 27, 6, 11, 1, 251943)),
        ),
        migrations.AlterField(
            model_name='userprogramworkoutmaster',
            name='user_program_workout_updated_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 27, 6, 11, 1, 252797)),
        ),
        migrations.AlterField(
            model_name='workout',
            name='workout_updated_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 27, 6, 11, 1, 248803)),
        ),
    ]
