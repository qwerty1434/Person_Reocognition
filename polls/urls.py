#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 10:23:38 2018

@author: qwerty1434
"""

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('upload_file/',views.upload_file,name='upload_file'),
]