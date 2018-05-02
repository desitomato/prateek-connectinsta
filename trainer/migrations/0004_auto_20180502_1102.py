# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-05-02 05:32
from __future__ import unicode_literals

from django.db import migrations, models
import trainer.models


class Migration(migrations.Migration):

    dependencies = [
        ('trainer', '0003_auto_20171227_1335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='epicture',
            field=models.ImageField(blank=True, null=True, upload_to=trainer.models.upload_location, verbose_name='Upload Image'),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to=trainer.models.upload_location, verbose_name='Upload Image'),
        ),
    ]
