from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import User, Subject, Comment, Chapter, File, Topic
from django.views.decorators.http import require_http_methods
from . import forms
# Create your views here.

subjects = get_list_or_404(Subject)


@require_http_methods(['GET', 'POST'])
def homeHandler(request):
    users = get_list_or_404(User.objects.order_by('-rating'))[:3]
    return render(request, 'notes/home.html', {
        'subjects': subjects,
        'users': users,
    })



@require_http_methods(['GET', 'POST'])
def login(request):
    return 'hello'


@require_http_methods(['GET'])
def map(request):
    return render(request, 'notes/map.html', {
        'subjects': subjects,
    })


@require_http_methods(['GET', 'POST'])
def topics(request, subject):
    tpc = get_list_or_404(Chapter.objects.filter(
        subject_name__name__iexact=subject
    ))
    return render(request, 'notes/topics.html', {
        'subject': subject,
        'tpc': tpc,
        'subjects': subjects,
    })


@require_http_methods(['GET', 'POST'])
def upload(request, subject):
    chapters = Chapter.objects.filter(
        subject_name__name__iexact=subject
    ).all()
    form = forms.UploadForm()
    form.getQuery(chapters)
    return render(request, 'notes/upload.html', {
        'subjects': subjects,
        'form': form,
        'subject': subject
    })


def files(request, subject, chapter):
    return 'hello'


def search(request):
    return 'hello'
