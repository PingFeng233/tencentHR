from django import forms
from .models import Resume


class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ['name', 'age', 'sex', 'address', 'school', 'experience', 'evaluation']
