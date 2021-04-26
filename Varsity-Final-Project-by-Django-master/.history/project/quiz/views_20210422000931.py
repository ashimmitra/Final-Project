from django.shortcuts import render
from quiz.models import Quiz
from quiz.models import Bangla
from quiz.models import Math
from quiz.models import Science
from quiz.models import GK

#def welcome(request):
    #return render(request, 'welcome.html')

def english(request):
    questions = Quiz.objects.all()
    return render(request, 'english.html', { 'questions': questions})

def bangla(request):
    questions = Bangla.objects.all()
    return render(request, 'bangla.html', { 'questions': questions})

def math(request):
    questions = Math.objects.all()
    return render(request, 'math.html', { 'questions': questions})

def science(request):
    questions = Science.objects.all()
    return render(request, 'science.html', { 'questions': questions})

def generalknowledge(request):
    questions = Bangla.objects.all()
    return render(request, 'generalknowledge.html', { 'questions': questions})

def result(request):
    return render(request, 'result.html')
