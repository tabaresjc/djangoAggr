# -*- coding: utf-8 -*-
from django.conf.urls import url
from .views import SitesView

# Generate pages following
# https://docs.djangoproject.com/en/1.11/topics/http/urls/#including-other-urlconfs
urlpatterns = [
    url(r'^$', SitesView.as_view()),
]
