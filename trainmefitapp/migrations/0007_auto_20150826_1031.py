# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('trainmefitapp', '0006_auto_20150825_1253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bodypartmaster',
            name='body_part_updated_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 26, 10, 31, 21, 381582)),
        ),
        migrations.AlterField(
            model_name='excercisevideo',
            name='exercise_video_updated_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 26, 10, 31, 21, 382390)),
        ),
        migrations.AlterField(
            model_name='excercisevideo',
            name='exercise_video_url',
            field=models.FileField(default=None, upload_to=b'exercise_video/', max_length=255, verbose_name=b'video'),
        ),
        migrations.AlterField(
            model_name='exercise',
            name='exercise_gender',
            field=models.CharField(max_length=50, choices=[(b'Male', b'Male'), (b'Female', b'Female')]),
        ),
        migrations.AlterField(
            model_name='exercise',
            name='exercise_gym_access',
            field=models.CharField(default=True, max_length=50, null=True, choices=[(b'Yes', b'Yes'), (b'No', b'No')]),
        ),
        migrations.AlterField(
            model_name='exercise',
            name='exercise_updated_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 26, 10, 31, 21, 383535)),
        ),
        migrations.AlterField(
            model_name='instructionmaster',
            name='instruction_updated_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 26, 10, 31, 21, 384577)),
        ),
        migrations.AlterField(
            model_name='membershipmaster',
            name='membership_updated_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 26, 10, 31, 21, 378300)),
        ),
        migrations.AlterField(
            model_name='objectivemaster',
            name='objective_updated_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 26, 10, 31, 21, 379055)),
        ),
        migrations.AlterField(
            model_name='programmaster',
            name='program_gym_access',
            field=models.CharField(default=True, max_length=50, blank=True, choices=[(b'Yes', b'Yes'), (b'No', b'No')]),
        ),
        migrations.AlterField(
            model_name='programmaster',
            name='program_updated_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 26, 10, 31, 21, 386693)),
        ),
        migrations.AlterField(
            model_name='programmaster',
            name='program_user_gender',
            field=models.CharField(default=True, max_length=50, choices=[(b'Male', b'Male'), (b'Female', b'Female')]),
        ),
        migrations.AlterField(
            model_name='programworkoutmap',
            name='workout_program_updated_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 26, 10, 31, 21, 388892)),
        ),
        migrations.AlterField(
            model_name='sampleworkout',
            name='sample_workout_updated_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 26, 10, 31, 21, 393670)),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user_gender',
            field=models.CharField(default=True, max_length=50, blank=True, choices=[(b'Male', b'Male'), (b'Female', b'Female')]),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user_gym_access',
            field=models.CharField(default=True, max_length=50, blank=True, choices=[(b'Yes', b'Yes'), (b'No', b'No')]),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user_updated_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 26, 10, 31, 21, 380110)),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user_workout_intensity',
            field=models.CharField(default=False, max_length=50, blank=True, choices=[(b'Easy', b'Easy'), (b'Medium', b'Medium'), (b'Hard', b'Hard')]),
        ),
        migrations.AlterField(
            model_name='userprogramexercisemap',
            name='user_program_exercise_updated_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 26, 10, 31, 21, 392183)),
        ),
        migrations.AlterField(
            model_name='userprogrammap',
            name='user_program_updated_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 26, 10, 31, 21, 389831)),
        ),
        migrations.AlterField(
            model_name='userprogramworkoutmaster',
            name='user_program_workout_updated_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 26, 10, 31, 21, 391017)),
        ),
        migrations.AlterField(
            model_name='workout',
            name='workout_updated_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 26, 10, 31, 21, 385480)),
        ),
    ]
