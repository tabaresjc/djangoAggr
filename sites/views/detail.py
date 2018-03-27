# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views import View
from django.shortcuts import render, get_object_or_404
from sites.models import Site, SiteData
from django.core.paginator import Paginator, EmptyPage


class DetailView(View):

    def get(self, request, site_id, page=1, limit=10):
        view_name = request.resolver_match.view_name

        if view_name:
            view_name = view_name.replace('-paginated', '')

        site = get_object_or_404(Site, pk=site_id)

        items = SiteData.get_pagination(site_id=site.id, page=page, limit=limit)

        return render(request, 'sites/detail.html', {
            'title': 'Detail Site - %s' % (site.name),
            'site': site,
            'items': items,
            'params': (site_id,),
        })
