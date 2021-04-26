
from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('notice/', views.notice, name='notice'),
    path('books/', views.books, name='notbooksice'),
    path('classes/', views.classes, name='classes'),
]
