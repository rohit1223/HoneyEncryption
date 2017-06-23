# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import CreditCard


class CreditCardAdmin(admin.ModelAdmin):
    class Meta:
        model = CreditCard
    list_display = ['alias', 'name', 'password', 'number', 'expiry_date', 'type', 'vault_type']

admin.site.register(CreditCard, CreditCardAdmin)