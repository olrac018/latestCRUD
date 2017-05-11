# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.


class RegistrationForm(models.Model):
	username = models.CharField(max_length=20)
	password = models.CharField(max_length=20)
	password2 = models.CharField(max_length=20)