from django.http import HttpResponseRedirect , HttpResponse
from django.shortcuts import render , redirect
from django.views.decorators.csrf import csrf_exempt
import json
from .forms import PhotoForm
import sys
from darkflow.cli import cliHandler


@csrf_exempt
def index(request):
    return render(request,'polls/index.html')


@csrf_exempt
def upload_file(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    else:
        form =PhotoForm()
    image_name = request.FILES['photo']
    return HttpResponse(cliHandler(image_name))




