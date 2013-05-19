# Create your views here.
from django.shortcuts import render_to_response, redirect, render
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.db import models
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django import forms
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

class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

def register(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/")
    else:
        form = UserCreateForm()
    return render(request, "registration/register.html", {
        'form': form,
    })
