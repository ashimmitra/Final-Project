
from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('notice/', views.notice, name='notice'),
    path('books/', views.books, name='books'),
    path('classes/', views.classes, name='classes'),
    path(r'^view-pdf/$', views.pdf_view, name='pdf_view'),
]
