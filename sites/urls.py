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
        name='index-paginated'),

    # Detail page & pagination
    url(r'^sites/(?P<site_id>\d+)$',
        views.DetailView.as_view(),
        name='detail'),
    url(r'^sites/(?P<site_id>\d+)/page/(?P<page>\d+)$',
        views.DetailView.as_view(),
        name='detail-paginated'),

    # Summary pages
    url(r'^summary$',
        views.SummaryView.as_view(),
        name='sum'),
    url(r'^summary-sum-sql$',
        views.SummaryView.as_view(),
        name='sum-sql'),

    url(r'^summary/page/(?P<page>\d+)$',
        views.SummaryView.as_view(),
        name='sum-paginated'),
    url(r'^summary-sum-sql/page/(?P<page>\d+)$',
        views.SummaryView.as_view(),
        name='sum-sql-paginated'),

    url(r'^summary-average$',
        views.SummaryView.as_view(),
        name='avg'),
    url(r'^summary-average-sql$',
        views.SummaryView.as_view(),
        name='avg-sql'),

    url(r'^summary-average/page/(?P<page>\d+)$',
        views.SummaryView.as_view(),
        name='avg-paginated'),
    url(r'^summary-average-sql/page/(?P<page>\d+)$',
        views.SummaryView.as_view(),
        name='avg-sql-paginated'),
]
