from django import forms
from .models import Project

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('project_Name','uploaded_By','date')
        widgets ={
            'project_Name':forms.TextInput(attrs={'class':'form-control'}),
            'uploaded_By':forms.TextInput(attrs={'class':'form-control'}),
            'date':forms.TextInput(attrs={'class':'form-control'})
        }