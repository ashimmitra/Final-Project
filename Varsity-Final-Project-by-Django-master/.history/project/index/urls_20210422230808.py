
from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('notic', views.home),
    path('', views.home),
]
