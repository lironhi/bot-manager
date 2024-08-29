from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from django.contrib import messages
import mysql.connector
import requests
# from bots.models import Product, Ordershop

# ~~~ Basic functions renders ~~~ #
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
def login_page(request):
    return render(request,'authentication-login.html')

def index_page(request):
    return render(request,'index.html')

def abots_page(request):
    return render(request,'abots.html')

def mbots_page(request):
    return render(request,'mbots.html')

def cpanel_page(request):
    return render(request,'cpanel.html')

def load_create_bot_form(request):
    return render(request, 'create_bot_form.html')

def create_bot(request):
    if request.method == 'POST':
        # Récupérer les données du formulaire et créer un bot
        bot_name = request.POST.get('bot_name')
        bot_platform = request.POST.get('bot_platform')
        bot_groups = request.POST.get('bot_groups')
        # Code pour enregistrer le bot dans la base de données
        # ...
        return redirect('index')  # Rediriger vers la page d'accueil après la création
    return redirect('index')