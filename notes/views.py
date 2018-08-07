from django.http import HttpResponse
from django.shortcuts import render, reverse, redirect, get_object_or_404, get_list_or_404
from django.views.decorators.http import require_http_methods
from .models import User, Subject, Chapter, File, Topic, Comment
from . import forms


# Create your views here.

@require_http_methods(['GET', 'POST'])
def home_handler(request):
    """Home page handler"""
    subjects = get_list_or_404(Subject)
    users = get_list_or_404(User.objects.order_by('-rating'))[:3]
    return render(request, 'notes/home.html', {
        'subjects': subjects,
        'users': users,
    })


@require_http_methods(['GET', 'POST'])
def login(request):
    """Handling login"""
    return 'hello'


@require_http_methods(['GET'])
def maps(request):
    """maps page"""
    subjects = get_list_or_404(Subject)
    return render(request, 'notes/map.html', {
        'subjects': subjects,
    })


@require_http_methods(['GET'])
def topics(request, subject):
    """topics handler"""
    tpc = Chapter.objects.filter(
        subject_name__name__iexact=subject
    )
    subjects = get_list_or_404(Subject)
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
    subjects = get_list_or_404(Subject)
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
        return redirect(reverse('notes:home_handler'))
    elif request.method == 'GET':
        form = forms.UploadForm(query=chapters)
        return render(request, 'notes/upload.html', {
            'subjects': subjects,
            'form': form,
            'subject': subject
        })


@require_http_methods(['GET'])
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
    subjects = get_list_or_404(Subject)
    return render(request, 'notes/doclist.html', {
        'docfiles': docfiles,
        'subject': subject,
        'chapter': chapter,
        'subjects': subjects,
    })


@require_http_methods(['GET', 'POST'])
def edit_file(request, subject, filename):
    """Edit the details of the file"""
    file = get_object_or_404(File.objects.filter(
        file_name__exact=filename
    ))
    subjects = get_list_or_404(Subject)
    chapters = Chapter.objects.filter(
        subject_name__name__iexact=subject
    ).all()
    if request.method == 'POST':
        form = forms.UploadForm()
    elif request.method == 'GET':
        topics_list = Topic.objects.filter(
            file_id__id__exact=file.id
        )
        topics_string = ''
        for i in topics_list:
            topics_string += "%s, " % i.title
        form = forms.UploadForm(query=chapters, initial={'filename':file.name, 'topics': topics_string})
        return render(request, 'notes/upload.html', {
            'subjects': subjects,
            'subject': subject,
            'form': form
        })



@require_http_methods(['GET', 'POST'])
def delete_file(request, filename):
    """delete file handler"""
    file = get_object_or_404(File.objects.filter(
        file_name__exact=filename
    ))    
    if request.method == 'POST':
        file.delete()
        return redirect(reverse('notes:home_handler'))
    elif request.method == 'GET':
        subjects = get_list_or_404(Subject)
        return render(request, 'notes/delete.html', {
            'file': file,
            'subjects': subjects
        })


@require_http_methods(['GET'])
def download_file(request, filename):
    """getting the file from filesystem and pass it as a response to download"""
    f = get_object_or_404(File.objects.filter(
        file_name__exact=filename
    ))
    response = HttpResponse(f.upload.read(), content_type='application/jpeg')
    return response


@require_http_methods(['GET'])
def file_detail(request, filename):
    print(filename)
    fdata = get_object_or_404(File.objects.filter(
        file_name=filename
    ))
    topics_list = Topic.objects.filter(
        file_id__id__exact=fdata.id
    )
    comments = Comment.objects.filter(
        file_id__id__exact=fdata.id
    )
    subjects = get_list_or_404(Subject)
    return render(request, 'notes/file.html', {
        'fdata': fdata,
        'subjects': subjects,
        'topics': topics_list,
        'comments': comments
    })


def search(request):
    return 'hello'
