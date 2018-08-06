from django.http import HttpResponse
from django.shortcuts import render, reverse, redirect, get_object_or_404, get_list_or_404
from django.views.decorators.http import require_http_methods
from django.core.files.storage import FileSystemStorage
from .models import User, Subject, Chapter, File, Topic
from . import forms


# Create your views here.

subjects = get_list_or_404(Subject)


@require_http_methods(['GET', 'POST'])
def homeHandler(request):
    """Home page handler"""
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
    """upload page request method"""
    chapters = Chapter.objects.filter(
        subject_name__name__iexact=subject
    ).all()
    if request.method == 'POST' and request.FILES['file']:
        form = forms.UploadForm(request.POST, request.FILES, query=chapters)
        if form.is_valid():
            f = form.cleaned_data
            sub = get_object_or_404(Subject.objects.filter(
                name__iexact=subject,
            ))
            chp = get_object_or_404(Chapter.objects.filter(
                title__exact=f['chapter'],
                subject_name__name__iexact=subject,
            ))
            use = get_object_or_404(User.objects.filter(pk=1))
            keywords = f['topics']
            key_arr = keywords.split(',')
            instance = File(
                name=f['filename'],
                file_name=request.FILES['file'],
                upload=f['file'],
                chapter_id=chp,
                subject_id=sub,
                user_id=use,
            )
            instance.save()
            instance.refresh_from_db()
            for i in key_arr:
                key = Topic(
                    title=i,
                    file_id=instance,
                )
                key.save()
        return redirect(reverse('notes:homeHandler'))
    elif request.method == 'GET':
        form = forms.UploadForm(query=chapters)
        return render(request, 'notes/upload.html', {
            'subjects': subjects,
            'form': form,
            'subject': subject
        })


def files(request, subject, chapter):
    sub = get_object_or_404(Subject.objects.filter(
        name__iexact=subject
    ))
    chp = get_object_or_404(Chapter.objects.filter(
        title__iexact=chapter,
        subject_name__name__iexact=subject,
    ))
    docfiles = get_list_or_404(File.objects.filter(
        subject_id=sub.id,
        chapter_id=chp.id,
    ))

    return render(request, 'notes/doclist.html', {
        'docfiles': docfiles,
        'subject': subject,
        'chapter': chapter,
        'subjects': subjects,

    })


def uploaded_file(request, filename):
    f = get_object_or_404(File.objects.filter(
        file_name__exact=filename
    ))
    response = HttpResponse(f.upload)
    return response


def access_file(request, filename):
    return 'hello'


def search(request):
    return 'hello'
