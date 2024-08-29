from django.urls import path
from . import views
#from django.contrib.files.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # --- [Main] --- #
    path('', views.login_page, name='login'),
    path('Index/', views.index_page, name='index'),
    path('All_Bots/', views.abots_page, name='abots'),
    path('My_Bots/', views.mbots_page, name='mbots'),
    path('Control_Panel/', views.cpanel_page, name='cpanel'),
    path('load_create_bot_form/', views.load_create_bot_form, name='load_create_bot_form'),
    # L'URL pour créer le bot
    path('create_bot/', views.create_bot, name='create_bot'),
]