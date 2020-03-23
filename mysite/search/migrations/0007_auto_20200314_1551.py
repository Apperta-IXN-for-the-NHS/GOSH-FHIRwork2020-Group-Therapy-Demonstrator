# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2020-03-14 15:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0006_patients_telephone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patients',
            name='telephone',
        ),
        migrations.AddField(
            model_name='patients',
            name='uuid',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
    ]
