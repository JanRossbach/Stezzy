from django import forms
from LernApp.models import Tag, LernKarte, Project


class TagForm(forms.ModelForm):
    model = Tag
    fields = {'name', 'color'}


class LernModelForm(forms.ModelForm):

    class Meta():
        model = LernKarte
        fields = ('name', 'tag', 'text')


class ProjectForm(forms.ModelForm):
    
    class Meta():
        model = Project
        fields = ('name', 'color',)
