from cProfile import label
from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class transcriptForm(forms.ModelForm):
    class Meta:
        model = Mark
        # fields = ['student','subject','semester_mark']
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['semester_mark'].widget.attrs.update(
            {'class': 'form-select'}
        )

class subjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = '__all__'


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class CreateClassForm(forms.ModelForm):
    class_choices = set([(c.classId, c.classId) for c in ClassOfSchool.objects.all()])
    classOfSchool = forms.CharField(label="",widget=forms.Select(
        choices=class_choices, 
        attrs={'class': 'form-select'
    }))
    class Meta:
        model = ClassOfSchool
        fields = []

