# Generated by Django 2.2.7 on 2020-08-01 17:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eCapture', '0007_event_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='dob',
            field=models.DateField(default=datetime.datetime(1990, 1, 1, 0, 0)),
            preserve_default=False,
        ),
    ]
