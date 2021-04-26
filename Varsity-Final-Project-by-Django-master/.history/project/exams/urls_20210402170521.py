
from django.urls import path
from .import views

urlpatterns = [
    path('', views.quiz),
    path('bangla/', views.quiz, name=''),
]
