# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-10-04 05:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pyas2', '0015_auto_20160615_0409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='message',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='logs', to='pyas2.Message'),
        ),
    ]