# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views import View
from django.shortcuts import render
from sites.models import Site


class IndexView(View):

    def get(self, request, page=1, limit=10):
        page = int(page)

        sites, total = Site.get_sites(page=page, limit=limit)

        return render(request, 'sites/index.html', {
            'title': 'Sites',
            'total': total,
            'sites': sites
        })
