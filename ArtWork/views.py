from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
# from .form import *
from .models import *
from django.http import HttpResponse
from django.contrib import messages
from django.http import HttpResponse


# def index(request):
#     return HttpResponse("You're at the Artwork home page.")

# Home page 

def home(request):

    context = {}
    return render(request, 'index.html', context)