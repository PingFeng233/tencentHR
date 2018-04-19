from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^work/$', work, name='work'),
    url(r'^live/$', live, name='live'),
    url(r'^training/$', training, name='training'),
    url(r'^welfare/$', welfare, name='welfare'),

]
