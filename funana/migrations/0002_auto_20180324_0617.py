# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-24 06:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funana', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funana',
            name='cmatch',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='funana',
            name='idea',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='funana',
            name='key_num',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='funana',
            name='pv',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='funana',
            name='result_winfo',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='funana',
            name='scan_winfo',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='funana',
            name='src',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
