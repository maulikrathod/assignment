# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-10 12:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitterApp', '0002_auto_20171210_1157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datewisetweets',
            name='tweets',
            field=models.TextField(blank=True, null=True),
        ),
    ]