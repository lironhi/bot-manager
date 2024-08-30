from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views
#from django.contrib.files.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # --- [Main] --- #
    path('', views.login_page, name='login'),
    path('index/', views.index_page, name='index'),
    path('All_Bots/', views.abots_page, name='abots'),
    path('My_Bots/', views.mbots_page, name='mbots'),
    path('Control_Panel/', views.cpanel_page, name='cpanel'),
    path('All_Groups/', views.agroups_page, name='agroups'),
    path('load_create_bot_form/', views.load_create_bot_form, name='load_create_bot_form'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    # L'URL pour créer le bot
    path('create_bot/', views.create_bot, name='create_bot'),
    # grp
    path('groups/', views.agroups_page, name='agroups'),
    path('groups/create/', views.create_group, name='create_group'),
    path('groups/edit/<int:group_id>/', views.edit_group, name='edit_group'),
    path('groups/delete/<int:group_id>/', views.delete_group, name='delete_group'),
]