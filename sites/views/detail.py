# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views import View
from django.shortcuts import render, get_object_or_404
from sites.models import Site, SiteData


class DetailView(View):

    def get(self, request, site_id, page=1, limit=10):
        site_id = int(site_id)
        page = int(page)

        site = get_object_or_404(Site, pk=site_id)

        items, total = SiteData.get_data_by_site(site_id=site.id, page=page)

        return render(request, 'sites/detail.html', {
            'title': 'Detail Site - %s' % (site.name),
            'site': site,
            'page': page,
            'total': total,
            'items': items
        })
