from django.conf.urls import url
from .views import (register_can, register_rec, login_can, login_rec, logout,
                    edit_info_cand, edit_resume_cand, edit_info_rec, resume_list,
                    send_zhaopin_list, zhaopin_detail)
from .chart import histogram, line

urlpatterns = [
    url(r'^register_can/$', register_can, name='register_can'),
    url(r'^register_rec/$', register_rec, name='register_rec'),
    url(r'^login_can/$', login_can, name='login_can'),
    url(r'^login_rec/$', login_rec, name='login_rec'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^edit_info_cand/(?P<id>\d+)/$', edit_info_cand, name='edit_info_cand'),
    url(r'^edit_resume_cand/(?P<id>\d+)/$', edit_resume_cand, name='edit_resume_cand'),
    url(r'^edit_info_rec/(?P<id>\d+)/$', edit_info_rec, name='edit_info_rec'),
    url(r'^resume_list/$', resume_list, name='resume_list'),
    url(r'^zhaopin_list/$', send_zhaopin_list, name='send_zhaopin_list'),
    url(r'^zhaopin_detail/(?P<id>\d+)/$', zhaopin_detail, name='zhaopin_detail'),

    url(r'^histogram/$', histogram, name='histogram'),
    url(r'^line/$', line, name='line'),
]
