from django.conf.urls import url
from django.urls import path
from . import views
from django.contrib.auth.views import login , logout
app_name = 'accounts'
urlpatterns = [
    path('' , views.all_accounts , name='all_accounts'),
    path('login/' , login , {'template_name':'login.html'} , name='login'),
    path('logout/' , logout , name='logout'),
    path('signup/' , views.register , name='register'),
    path('profile/<slug:slug>/', views.profile, name='profile'),
    path('profile/<slug:slug>/edit', views.edit_profile, name='edit_profile'),
    path('profile/<slug:slug>/change_password', views.change_password, name='change_password'),

]
