from django.shortcuts import render
from .models import AboutSite
from .models import Slider
from .models import Contact

def home(request):
    aboutdata = AboutSite.objects.all()[0]
    sliderdata = Slider.objects.all()
    context = {
        'AboutSite': aboutdata,
        'Slider': sliderdata
    }
    if request.METHOD=POST:
        name=request.POST.get('name')
        email=request.POST.get('email')
        name=request.POST.get('name')
        name=request.POST.get('name')
    return render(request,"index.html",context)

def blog(request):
    return render(request,"blog.html") 