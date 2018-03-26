# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views import View
from django.shortcuts import render, get_object_or_404
from sites.models import Site


class DetailView(View):

    def get(self, request, site_id):
        site = get_object_or_404(Site, pk=site_id)

        return render(request, 'sites/detail.html', {
            'title': 'Detail Site - %s' % (site.name),
            'site': site
        })
