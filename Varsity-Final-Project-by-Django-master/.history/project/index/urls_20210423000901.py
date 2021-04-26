
from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('notice/', views.notice,name='home'),
    path('books/', views.books),
    path('classes/', views.classes),
]
