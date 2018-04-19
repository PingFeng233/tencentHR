from .models import Candidaters, Recruiter
from django import forms
from resume.models import Resume


class CanRegisterForm(forms.ModelForm):
    class Meta:
        model = Candidaters
        fields = '__all__'

        css = {'class': "longinput3 changeCheck", 'size': "35", 'maxlength': "60"}
        widgets = {
            'username': forms.TextInput(attrs=css),
            'password1': forms.PasswordInput(attrs=css),
            'password2': forms.PasswordInput(attrs=css),
            'headshot': forms.FileInput(attrs=css),
            'email': forms.EmailInput(attrs=css),
            'tel': forms.TextInput(attrs=css),
        }


class RecRegisterForm(forms.ModelForm):
    class Meta:
        model = Recruiter
        fields = '__all__'

        css = {'class': "longinput3 changeCheck", 'size': "35", 'maxlength': "60"}
        widgets = {
            'username': forms.TextInput(attrs=css),
            'password1': forms.PasswordInput(attrs=css),
            'password2': forms.PasswordInput(attrs=css),
            'department': forms.TextInput(attrs=css),
            'email': forms.EmailInput(attrs=css),
            'tel': forms.TextInput(attrs=css),
        }


class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ['name', 'age', 'sex', 'address', 'school', 'experience', 'evaluation']
