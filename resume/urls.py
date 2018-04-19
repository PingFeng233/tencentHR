from django.conf.urls import url
from .views import send_resume, resume_detail

urlpatterns = [
    url(r'^send_resume/(?P<id>\d+)/$', send_resume, name='send_resume'),
    url(r'^resume_detail/(?P<id>\d+)/$', resume_detail, name='resume_detail')
]
