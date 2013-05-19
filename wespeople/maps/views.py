# Create your views here.
from django.shortcuts import render_to_response, redirect, render
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.db import models
from django.contrib.auth.decorators import login_required
from django import forms
from django.contrib.auth.forms import UserCreationForm

from maps.models import *


@login_required
def map_test(request):
    """
    display something
    """


    template_values = {'test': 'test',}

    return render_to_response('map.html', template_values)

def register(request):
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      new_user = form.save()
      return HttpResponseRedirect("/books/")
  else:
    form = UserCreationForm()
  return render(request, "/accounts/login.html", {'form': form,})
