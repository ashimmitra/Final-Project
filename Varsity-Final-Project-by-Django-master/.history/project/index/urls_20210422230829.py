
from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('notice/', views.home),
    path('books/', views.home),
    path('classes/', views.home),
]
