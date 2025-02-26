from django import forms
from .models import Project

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'location', 'start_date', 'end_date', 'status', 'budget', 'manager', 'plan_pdf']