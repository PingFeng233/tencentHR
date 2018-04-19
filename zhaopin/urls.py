from django.conf.urls import url
from .views import (index, detail, social, SearchView, add_zhaopin,)

urlpatterns = [
    url(r'^index/$', index, name='index'),
    url(r'^detail/(?P<pk>\d+)/$', detail, name='detail'),
    url(r'^social/$', social, name='social'),
    url(r'^search/$', SearchView.as_view(), name='search'),
    url(r'^add_zhaopin', add_zhaopin, name='add_zhaopin'),

]
