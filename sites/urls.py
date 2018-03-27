# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

# Generate pages following
# https://docs.djangoproject.com/en/1.11/topics/http/urls/#including-other-urlconfs
app_name = 'sites'

urlpatterns = [
    # Top page & pagination
    url(r'^$',
        views.IndexView.as_view(),
        name='index'),
    url(r'^page/(?P<page>\d+)$',
        views.IndexView.as_view(),
        name='index_paginated'),

    # Detail page & pagination
    url(r'^sites/(?P<site_id>\d+)$',
        views.DetailView.as_view(),
        name='detail'),
    url(r'^sites/(?P<site_id>\d+)/page/(?P<page>\d+)$',
        views.DetailView.as_view(),
        name='detail_paginated'),

    # Summary pages
    url(r'^summary$',
        views.SummaryView.as_view(),
        name='summary'),
    url(r'^summary-average$',
        views.SummaryAvgView.as_view(),
        name='summary-average'),
]
