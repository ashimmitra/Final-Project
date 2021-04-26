
from django.urls import path
from .import views

urlpatterns = [
    path('', views.english),
    #path('',views.welcome),
    path('result/',views.result),
    path('english/', views.english, name='profile.english'),
    path('bangla/', views.bangla, name='profile.bangla'),
    path('science/', views.bangla, name='profile.science'),
    path('math/', views.bangla, name='profile.math'),
    path('generalknowledge/', views.bangla, name='profile.generalknowledge'),
]
