# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-14 20:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scrumboard', '0005_card_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='members',
        ),
        migrations.RemoveField(
            model_name='card',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='list',
            name='project',
        ),
        migrations.DeleteModel(
            name='Project',
        ),
    ]
