# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-12 22:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CreditCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('number', models.CharField(max_length=200)),
                ('expiry_date', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('type', models.CharField(max_length=200)),
                ('vault_type', models.CharField(max_length=200)),
            ],
        ),
    ]
