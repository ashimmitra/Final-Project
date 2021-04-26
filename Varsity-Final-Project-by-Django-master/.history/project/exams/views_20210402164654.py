from django.shortcuts import render
from exams.models import Exam

def quiz(request):
    exam = Exam.objects.all()
    return render(request,quiz.html",{"exam":exam})


