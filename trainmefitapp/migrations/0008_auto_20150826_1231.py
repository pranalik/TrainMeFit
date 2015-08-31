# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('trainmefitapp', '0007_auto_20150826_1031'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExcerciseImage',
            fields=[
                ('exercise_image_id', models.AutoField(serialize=False, primary_key=True)),
                ('exercise_image_name', models.CharField(max_length=30)),
                ('exercise_image', models.ImageField(default=None, max_length=255, null=True, verbose_name=b'Exercise Image', upload_to=b'exercise_images')),
                ('exercise_image_created_by', models.CharField(max_length=20, null=True)),
                ('exercise_image_updated_by', models.CharField(max_length=20, null=True)),
                ('exercise_image_created_date', models.DateTimeField(null=True)),
                ('exercise_image_updated_date', models.DateTimeField(default=datetime.datetime(2015, 8, 26, 12, 31, 30, 617113))),
                ('exercise_image_status', models.CharField(default=b'Active', max_length=20, blank=True, choices=[(b'Active', b'Active'), (b'Inactive', b'Inactive')])),
            ],
        ),
        migrations.CreateModel(
            name='RestChallenges',
            fields=[
                ('rest_challenge_id', models.AutoField(serialize=False, primary_key=True)),
                ('rest_challenge_name', models.CharField(max_length=50, null=True)),
                ('rest_challenge_description', models.CharField(max_length=50, null=True)),
                ('rest_challenge_created_by', models.CharField(default=b'admin', max_length=50, null=True)),
                ('rest_challenge_updated_by', models.CharField(default=b'admin', max_length=50, null=True)),
                ('rest_challenge_created_date', models.DateTimeField(null=True)),
                ('rest_challenge_updated_date', models.DateTimeField(default=datetime.datetime(2015, 8, 26, 12, 31, 30, 625869))),
                ('rest_challenge_status', models.CharField(default=b'Active', max_length=50, blank=True, choices=[(b'Active', b'Active'), (b'Inactive', b'Inactive')])),
            ],
        ),
        migrations.AlterField(
            model_name='bodypartmaster',
            name='body_part_updated_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 26, 12, 31, 30, 614750)),
        ),
        migrations.AlterField(
            model_name='excercisevideo',
            name='exercise_video_updated_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 26, 12, 31, 30, 615462)),
        ),
        migrations.AlterField(
            model_name='exercise',
            name='exercise_updated_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 26, 12, 31, 30, 616244)),
        ),
        migrations.AlterField(
            model_name='instructionmaster',
            name='instruction_updated_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 26, 12, 31, 30, 617813)),
        ),
        migrations.AlterField(
            model_name='membershipmaster',
            name='membership_updated_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 26, 12, 31, 30, 611890)),
        ),
        migrations.AlterField(
            model_name='objectivemaster',
            name='objective_updated_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 26, 12, 31, 30, 612542)),
        ),
        migrations.AlterField(
            model_name='programmaster',
            name='program_updated_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 26, 12, 31, 30, 619308)),
        ),
        migrations.AlterField(
            model_name='programworkoutmap',
            name='workout_program_updated_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 26, 12, 31, 30, 620906)),
        ),
        migrations.AlterField(
            model_name='sampleworkout',
            name='sample_workout_updated_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 26, 12, 31, 30, 625241)),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user_updated_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 26, 12, 31, 30, 613456)),
        ),
        migrations.AlterField(
            model_name='userprogramexercisemap',
            name='user_program_exercise_updated_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 26, 12, 31, 30, 623823)),
        ),
        migrations.AlterField(
            model_name='userprogrammap',
            name='user_program_updated_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 26, 12, 31, 30, 621824)),
        ),
        migrations.AlterField(
            model_name='userprogramworkoutmaster',
            name='user_program_workout_updated_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 26, 12, 31, 30, 622746)),
        ),
        migrations.AlterField(
            model_name='workout',
            name='workout_updated_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 26, 12, 31, 30, 618603)),
        ),
        migrations.AddField(
            model_name='restchallenges',
            name='workout_id',
            field=models.ForeignKey(related_name='rest_day_workout_id', to='trainmefitapp.Workout', null=True),
        ),
        migrations.AddField(
            model_name='excerciseimage',
            name='exercise_id',
            field=models.ForeignKey(related_name='exercise_image', to='trainmefitapp.Exercise', null=True),
        ),
    ]
