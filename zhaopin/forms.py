from django.forms import ModelForm
from .models import Zhaopin


class add_zhaopinForm(ModelForm):
    class Meta:
        model = Zhaopin
        fields = ['title', 'workLocation', 'peopleNumber', 'category', 'content']
