from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from django.template import loader

from .models import Question

def home(request):
    #url = request.build_absolute_uri()

    template = loader.get_template("mysite/home.html")
    return HttpResponse(template.render())

def questions(request):
    resp = loader.get_template("mysite/questions.html").render({"qs" : Question.objects.all()})

    return HttpResponse(resp)
def vote(request, question_id):
    return HttpResponse(f"You are voting on question {question_id}")
def results(request, question_id):
    return HttpResponse(f"You're looking at the results of question {question_id}")
def details(request, question_id):
    return HttpResponse(f"You are looking at question {question_id}")

