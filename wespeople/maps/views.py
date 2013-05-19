# Create your views here.
from django.shortcuts import render_to_response, redirect, render
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.db import models
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

from maps.models import Person

def index(request):
    """
    Display the main index map page
    """

    template_values = {'test': 'hello'}

    return render_to_response('maps/index.html', template_values)

def search(request):
    """
    search stuff perhaps?
    """

    if 'general' in request.GET:
        message = 'You\'re looking for '+ request.GET['general'] + '.'
    else:
        message = "You failed"

    template_values = {'test': 'hello',
                        'message' : message}

    return render_to_response('map.html', template_values)

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/")
    else:
        form = UserCreationForm()
    return render(request, "registration/register.html", {
        'form': form,
    })
