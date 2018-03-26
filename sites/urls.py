# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

# Generate pages following
# https://docs.djangoproject.com/en/1.11/topics/http/urls/#including-other-urlconfs
app_name = 'sites'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^sites/(?P<site_id>\d+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^summary$', views.SummaryView.as_view(), name='summary'),
    url(r'^summary-average$', views.SummaryAvgView.as_view(), name='summary-average'),
]
