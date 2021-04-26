
from django.urls import path
from .import views

urlpatterns = [
    
    path('bangla/', views.quiz, name='student.profile.bangla'),
]
