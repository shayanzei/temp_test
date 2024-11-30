from django import forms
from .models import Task, Project

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'state', 'description', 'start_date', 'due_date']
        widgets = {
                'start_date': forms.DateInput(attrs={'type': 'date'}),  
                'due_date': forms.DateInput(attrs={'type': 'date'}),
                'description': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
            }
    
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'project', 'assigned_to', 'due_date',
                'status', 'priority']
        widgets = {
                'start_date': forms.DateInput(attrs={'type': 'date'}),  
                'due_date': forms.DateInput(attrs={'type': 'date'}),
                'description': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
            }