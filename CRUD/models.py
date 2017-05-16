# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django import forms



class Crud(models.Model):
    stdno = models.IntegerField()
    fname = models.CharField(max_length = 50)
    lname = models.CharField(max_length = 50)

class Log(models.Model):
    username = models.CharField(max_length = 30)
    password = models.CharField(max_length = 30)

