# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-20 15:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20170320_1545'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='iamge',
            new_name='image',
        ),
    ]