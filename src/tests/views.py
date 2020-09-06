from django.shortcuts import render, get_object_or_404
from .models import *


# Create your views here.
def index(request):
    # this shows a list of tests in the homepage
    template = "index.html"
    latest_tests = Test.objects.order_by('-id')[:3]
    context = {'tests': latest_tests}
    return render(request, template, context)

def t_detail(request, t_id):
    # this opens up the test_id and lists the questions for each test
    template = "t_detail.html"
    questionsbypart = Question.objects.order_by('-id')[:12]
    context = {'questions': questionsbypart}
    return render(request, template, context)

# define another shit for choices for the questions
