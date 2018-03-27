# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views import View
from django.shortcuts import render
from sites.models import Site
from django.core.paginator import Paginator, EmptyPage


class IndexView(View):

    def get(self, request, page=1, limit=10):

        items = Site.get_pagination(page=page, limit=limit)

        return render(request, 'sites/index.html', {
            'title': 'Sites',
            'items': items
        })
