from django.http


def home(request):
    return HttpResponse("this is home page")