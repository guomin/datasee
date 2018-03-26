# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Funana(models.Model):
    match_type = models.CharField(max_length=128)
    key_num = models.IntegerField(default=0)
    scan_winfo = models.IntegerField(default=0)
    result_winfo = models.IntegerField(default=0)
    idea = models.IntegerField(default=0)
    pv = models.IntegerField(default=0)
    src = models.PositiveSmallIntegerField(default=0)
    cmatch = models.PositiveSmallIntegerField(default=0)
    stat_time = models.DateTimeField()
    insert_time = models.DateTimeField()

class BsFunnelStats(models.Model):
    """
    """
    match_type = models.CharField(max_length=128)
    key_num = models.IntegerField(default=0)
    scan_winfo = models.IntegerField(default=0)
    result_winfo = models.IntegerField(default=0)
    idea = models.IntegerField(default=0)
    pv = models.IntegerField(default=0)
    src = models.PositiveSmallIntegerField(default=0)
    cmatch = models.PositiveSmallIntegerField(default=0)
    stat_time = models.DateTimeField()
    insert_time = models.DateTimeField()
