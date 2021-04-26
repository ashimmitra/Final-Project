
from django.urls import path
from .import views

urlpatterns = [
    path('', views.english),
    #path('',views.welcome),
    path('',views.welcome),
    path('english/', views.english, name='profile.english'),
    path('bangla/', views.bangla, name='profile.bangla'),
]
