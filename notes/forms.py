from django import forms
from .models import Chapter


class UploadForm(forms.Form):
    """Upload Form"""

    def __init__(self, *args, **kwargs):
        self.query = (kwargs.pop('query', None))
        super(UploadForm, self).__init__(*args, **kwargs)
        self.fields['chapter'] = forms.ModelChoiceField(widget=forms.Select(
            attrs={'class': 'placeholder'}
        ), label='Chapter', empty_label='Select Chapter', queryset=self.query)

    file = forms.FileField()
    filename = forms.CharField(label='File name', widget=forms.TextInput(
        attrs={'placeholder': 'Enter file name', 'class': 'placeholder'}
    ))
    topics = forms.CharField(label='Topics Covered', widget=forms.TextInput(
        attrs={'placeholder': 'Enter topics', 'class': 'placeholder'}
    ))


class EditFileForm(forms.Form):
    """Form for editing details of the file"""

    def __init__(self, *args, **kwargs):
        self.query = (kwargs.pop('query', None))
        super(EditFileForm, self).__init__(*args, **kwargs)
        self.fields['chapter'] = forms.ModelChoiceField(widget=forms.Select(
            attrs={'class': 'placeholder'}
        ), label='Chapter', empty_label='Select Chapter', queryset=self.query)

    file = forms.FileField(required=False)
    filename = forms.CharField(required=False, label='File name', widget=forms.TextInput(
        attrs={'placeholder': 'Enter file name', 'class': 'placeholder'}
    ))
    topics = forms.CharField(required=False, label='Topics Covered', widget=forms.TextInput(
        attrs={'placeholder': 'Enter topics', 'class': 'placeholder'}
    ))
