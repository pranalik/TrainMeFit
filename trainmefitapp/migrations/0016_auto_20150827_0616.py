# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('trainmefitapp', '0015_auto_20150827_0611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bodypartmaster',
            name='body_part_updated_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 27, 6, 16, 2, 676362)),
        ),
        migrations.AlterField(
            model_name='excerciseimage',
            name='exercise_image_updated_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 27, 6, 16, 2, 678628)),
        ),
        migrations.AlterField(
            model_name='excercisevideo',
            name='exercise_video_updated_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 27, 6, 16, 2, 677065)),
        ),
        migrations.AlterField(
            model_name='exercise',
            name='exercise_updated_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 27, 6, 16, 2, 677795)),
        ),
        migrations.AlterField(
            model_name='instructionmaster',
            name='instruction_updated_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 27, 6, 16, 2, 679347)),
        ),
        migrations.AlterField(
            model_name='membershipmaster',
            name='membership_updated_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 27, 6, 16, 2, 673523)),
        ),
        migrations.AlterField(
            model_name='objectivemaster',
            name='objective_updated_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 27, 6, 16, 2, 674170)),
        ),
        migrations.AlterField(
            model_name='programmaster',
            name='program_updated_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 27, 6, 16, 2, 680884)),
        ),
        migrations.AlterField(
            model_name='programworkoutmap',
            name='workout_program_updated_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 27, 6, 16, 2, 682409)),
        ),
        migrations.AlterField(
            model_name='restchallenges',
            name='rest_challenge_updated_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 27, 6, 16, 2, 687131)),
        ),
        migrations.AlterField(
            model_name='sampleworkout',
            name='sample_workout_updated_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 27, 6, 16, 2, 686508)),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user_updated_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 27, 6, 16, 2, 675072)),
        ),
        migrations.AlterField(
            model_name='userprogramexercisemap',
            name='exercise_id',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='userprogramexercisemap',
            name='user_program_exercise_updated_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 27, 6, 16, 2, 685120)),
        ),
        migrations.AlterField(
            model_name='userprogrammap',
            name='user_program_updated_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 27, 6, 16, 2, 683272)),
        ),
        migrations.AlterField(
            model_name='userprogramworkoutmaster',
            name='user_program_workout_updated_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 27, 6, 16, 2, 684155)),
        ),
        migrations.AlterField(
            model_name='workout',
            name='workout_updated_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 27, 6, 16, 2, 680164)),
        ),
    ]
