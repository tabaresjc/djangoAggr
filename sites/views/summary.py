# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views import View
from django.shortcuts import render
from sites.models import SiteData


class SummaryView(View):

    def get(self, request, page=1, limit=10):
        page = int(page)
        limit = int(limit)

        items, total = SiteData.get_summary_by_site(page=page, limit=limit)

        return render(request, 'sites/summary.html', {
            'title': 'Summary',
            'page': page,
            'limit': limit,
            'total': total,
            'items': items
        })
