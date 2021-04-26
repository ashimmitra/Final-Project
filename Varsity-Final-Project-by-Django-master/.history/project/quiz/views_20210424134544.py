from django.shortcuts import render
from quiz.models import Quiz
from quiz.models import Math
from quiz.models import Science
from quiz.models import GK
from quiz.models import ICT
from quiz.models import Ban

#def welcome(request):
    #return render(request, 'welcome.html')

def english(request):
    questions = Quiz.objects.all()
    return render(request, 'english.html', { 'questions': questions})

def ban(request):
    questions = Ban.objects.all()
    return render(request, 'ban.html', { 'questions': questions})

def math(request):
    questions = Math.objects.all()
    return render(request, 'math.html', { 'questions': questions})

def science(request):
    questions = Science.objects.all()
    return render(request, 'science.html', { 'questions': questions})

def generalknowledge(request):
    questions = GK.objects.all()
    return render(request, 'generalknowledge.html', { 'questions': questions})

def ict(request):
    questions = ICT.objects.all()
    return render(request, 'ict.html', { 'questions': questions})

def mental_ability(request):
    questions = ICT.objects.all()
    return render(request, 'ict.html', { 'questions': questions})    

def result(request):
    results = Math.objects.all()
    return render(request, 'result.html',{'results':result})
