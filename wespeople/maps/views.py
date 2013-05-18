# Create your views here.
from django.shortcuts import render_to_response, redirect
from django.http import HttpResponse, HttpRequest
from django.db import models

from map.models import *


def map_test(request):
    """
    display something
    """
    
    
    template_values = {'test': 'test',}
    
    return render_to_response('map-test.html', template_values)