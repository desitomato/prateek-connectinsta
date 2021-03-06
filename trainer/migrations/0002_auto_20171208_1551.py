# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-08 10:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainer',
            name='designation',
            field=models.CharField(blank=True, max_length=500, verbose_name='Designation'),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='mobile',
            field=models.IntegerField(blank=True, default=0, verbose_name='Mobile'),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='name',
            field=models.CharField(blank=True, max_length=250, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='organisation',
            field=models.CharField(blank=True, max_length=250, verbose_name='Organisation'),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='picture',
            field=models.FileField(blank=True, upload_to=b'', verbose_name='Upload Image'),
        ),
    ]
