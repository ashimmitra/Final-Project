from django.shortcuts import render
from quiz.models import Quiz
from quiz.models import Bangla

def welcome(request):
    return render(request, 'welcome.html')

def quiz(request):
    questions = Quiz.objects.all()
    return render(request, 'quiz.html', { 'questions': questions})

def bangla(request):
    questions = Bangla.objects.all()
    return render(request, 'bangla.html', { 'questions': questions})