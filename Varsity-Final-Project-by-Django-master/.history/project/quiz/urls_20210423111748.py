
from django.urls import path
from .import views

urlpatterns = [
    path('', views.english),
    #path('',views.welcome),
    path('result/',views.result, name='quiz.result'),
    path('english/', views.english, name='profile.english'),
    path('bangla/', views.bangla, name='profile.bangla'),
    path('science/', views.science, name='profile.science'),
    path('math/', views.math, name='profile.math'),
    path('generalknowledge/', views.generalknowledge, name='profile.generalknowledge'),
]
