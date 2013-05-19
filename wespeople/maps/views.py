# Create your views here.
from django.shortcuts import render_to_response, redirect
from django.http import HttpResponse, HttpRequest
from django.db import models
from django.contrib.auth.decorators import login_required

from maps.models import *


#@login_required
def map_test(request):
    """
    display something
    """


    template_values = {'test': 'test',}

    return render_to_response('map.html', template_values)
