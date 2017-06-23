# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class CreditCard(models.Model):
	# alias = models.CharField(max_length=10)
    alias = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    number = models.CharField(max_length=200)
    expiry_date = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    vault_type = models.CharField(max_length=200)