# Create your views here.
from django.shortcuts import render_to_response, redirect
from django.http import HttpResponse, HttpRequest
from django.db import models
from django.contrib.auth.decorators import login_required

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
