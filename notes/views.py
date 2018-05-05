from django.shortcuts import render, get_object_or_404
from .models import User, Subject, Comment, Chapter, File, Topic

# Create your views here.

subjects = Subject.objects.all()

def homeHandler(request):
    leaders = User.objects.all()[:3]
    return render(request, 'notes/home.html', {
        'subjects': subjects,
        'leaders': leaders,
    })


def login(request):
    return 'hello'


def map(request):
    return render(request, 'notes/map.html', {
        'subjects': subjects,
    })


def topics(request, subject):
    return 'hello'


def search(request):
    return 'hello'
