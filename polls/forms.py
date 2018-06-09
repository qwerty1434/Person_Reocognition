#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 11:48:58 2018

@author: qwerty1434
"""

from django.forms import ModelForm
from django import forms
from .models import Photo
 
class PhotoForm(ModelForm):
    title = forms.CharField(max_length = 255)
    photo = forms.FileField()
    class Meta:
        model = Photo
        fields = ['title', 'photo',]

        
