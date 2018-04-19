from django.contrib import admin

# Register your models here.
from .models import Candidaters,Recruiter

admin.site.register(Candidaters)
admin.site.register(Recruiter)