from django.shortcuts import render
from .model import AboutSite

def home(request):
    aboutdata=AboutSite.objects.all()
    context()
    return render(request,"index.html")

def blog(request):
    return render(request,"blog.html") 
