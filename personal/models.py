# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User

from django.db import models

class UserProfile(models.Model):
    name = models.CharField('Имя', max_length=255)
    user = models.ForeignKey(User)
