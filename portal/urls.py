# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='homepage'),
    url(r'^submit/$', views.submit, name='homepage'),
    url(r'^vault/(?P<type>[a-zA-Z0-9]+)$', views.vault, name='homepage'),
    url(r'^detail/(?P<type>[a-zA-Z0-9]+)/(?P<vault_type>[a-zA-Z0-9]+)$', views.detail, name='homepage'),
    url(r'^terminal/(?P<type>[a-zA-Z0-9]+)/(?P<vault_type>[a-zA-Z0-9]+)$', views.terminal, name='homepage'),
    url(r'^auth/(?P<type>[a-zA-Z0-9]+)$', views.auth, name='homepage'),
    url(r'^search/$', views.search, name='homepage')
    # url(r'^notFound',)
]
