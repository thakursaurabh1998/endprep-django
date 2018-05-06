from django import forms
from .models import *


class UploadForm(forms.Form):
    def getQuery(self,query):
        self.chapter = forms.ModelChoiceField(widget=forms.Select(
            attrs={'class': 'placeholder'}
        ), label='Chapter', empty_label='Select Chapter', queryset=query)
        print(query.title)
    file = forms.FileField()
    filename = forms.CharField(label='File name', widget=forms.TextInput(
        attrs={'placeholder': 'Enter file name', 'class': 'placeholder'}
    ))
    topics = forms.CharField(label='Topics Covered', widget=forms.TextInput(
        attrs={'placeholder':'Enter topics','class':'placeholder'}
    ))
    # chapter = forms.ModelChoiceField(widget=forms.Select(
    #     attrs={'class':'placeholder'}
    # ),label='Chapter', empty_label='Select Chapter', queryset=Subject.objects.all())
