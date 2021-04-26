
from django.urls import path
from .import views

urlpatterns = [
    path('', views.english),
    #path('',views.welcome),
    path('result/',views.result, name='result'),
    path('english/', views.english, name='profile.english'),
    path('bangla/', views.bangla, name='profile.bangla'),
    path('ban/', views.ban, name='profile.ban'),
    path('science/', views.science, name='profile.science'),
    path('science/', views.sci, name='profile.sci'),
    path('math/', views.math, name='profile.math'),
    path('math/', views.mat, name='profile.mat'),
    path('ict/', views.ict, name='profile.ict'),
    path('generalknowledge/', views.generalknowledge, name='profile.generalknowledge'),
    path('generalknowledge/', views.gnk, name='profile.gnk'),
]
