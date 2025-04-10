# Generated by Django 5.0.7 on 2024-09-24 12:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentmgt', '0004_student_batch'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='batch',
        ),
        migrations.AddField(
            model_name='student',
            name='batch_mon',
            field=models.CharField(default=datetime.datetime(2024, 9, 24, 12, 58, 29, 779746, tzinfo=datetime.timezone.utc), max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='batch_year',
            field=models.CharField(default=datetime.datetime(2024, 9, 24, 12, 58, 52, 60721, tzinfo=datetime.timezone.utc), max_length=255),
            preserve_default=False,
        ),
    ]
