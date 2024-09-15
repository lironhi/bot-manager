from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import mysql.connector
import requests
from django.http import JsonResponse
# Models to implement
from .models import BotGroup
from .forms import BotGroupForm

# ~~~     Login functions     ~~~ #
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not username or not password:
            messages.error(request, 'Both username and password are required.')
            return render(request, 'authentication-login.html')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Failed to log in: username or password error.')
            return render(request, 'authentication-login.html')
    
    return render(request, 'authentication-login.html')

# ~~~     Index functions     ~~~ #
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

@login_required
def index_page(request):
    return render(request, 'index.html')
@login_required
def abots_page(request):
    return render(request,'abots.html')
@login_required
def mbots_page(request):
    return render(request,'mbots.html')
@login_required
def cpanel_page(request):
    return render(request,'cpanel.html')
@login_required
def agroups_page(request):
    groups = BotGroup.objects.all()  # GET all
    return render(request, 'agroups.html', {'groups': groups})

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

# Func to create a group
def create_group(request):
    if request.method == 'POST':
        form = BotGroupForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    return JsonResponse({'success': False, 'error': 'Invalid request method'})

# Func to modify a group
def edit_group(request, group_id):
    group = get_object_or_404(BotGroup, id=group_id)
    if request.method == 'POST':
        form = BotGroupForm(request.POST, instance=group)
        if form.is_valid():
            form.save()
            messages.success(request, 'Group updated successfully!')
            return redirect('agroups')
    else:
        form = BotGroupForm(instance=group)
    return render(request, 'edit_group_form.html', {'form': form, 'group': group})

# Func to delete a group
def delete_group(request, group_id):
    group = get_object_or_404(BotGroup, id=group_id)
    group.delete()
    messages.success(request, 'Group deleted successfully!')
    return redirect('agroups')