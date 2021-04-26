from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseNotFound
from .models import AboutSite
from .models import Slider
from .models import Contact
from .models import Notice
from .models import Books

def home(request):
    aboutdata = AboutSite.objects.all()[0]
    sliderdata = Slider.objects.all()
    context = {
        'AboutSite': aboutdata,
        'Slider': sliderdata
    }
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')

        contactdata = Contact(name=name,email=email,subject=subject,message=message)
        contactdata.save()
    return render(request,"index.html",context)

def notice(request):
    notices = Notice.objects.all()
    return render(request,"notice.html",{'notices':notices})

def classes(request):
    return render(request, 'classes.html')

def books(request):
    book_list = Books.objects.all()
    return render(request, 'books.html',{'book_list':book_list})

def pdf_view(request):
    fs = FileSystemStorage()
    filename = 'mypdf.pdf'
    if fs.exists(filename):
        with fs.open(filename) as pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            #response['Content-Disposition'] = 'attachment; filename="mypdf.pdf"' #user will be prompted with the browser’s open/save file
            response['Content-Disposition'] = 'inline; filename="mypdf.pdf"' #user will be prompted display the PDF in the browser
            return response
    else:
        return HttpResponseNotFound('The requested pdf was not found in our server.')    