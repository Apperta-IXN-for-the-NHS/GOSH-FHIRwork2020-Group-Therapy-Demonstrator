# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2020-03-13 14:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0004_auto_20200313_1223'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patients',
            old_name='first_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='patients',
            name='last_name',
        ),
        migrations.AddField(
            model_name='patients',
            name='age',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
