from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^info/$', info, name='info'),
    url(r'^branch/$', branch, name='branch'),
    url(r'^business/$', business, name='business'),
    url(r'^culture/$', culture, name='culture'),
]
