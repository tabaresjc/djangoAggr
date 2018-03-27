# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views import View
from django.shortcuts import render
from sites.models import SiteData


class SummaryView(View):

    aggr_functions = {
        'sites:sum': SiteData.get_sum_by_site,
        'sites:sum-sql': SiteData.get_sum_sql_by_site,
        'sites:avg': SiteData.get_avg_by_site,
        'sites:avg-sql': SiteData.get_avg_sql_by_site,
    }

    def get(self, request, page=1, limit=10):
        page = int(page)
        limit = int(limit)

        view_name = request.resolver_match.view_name

        items, total = self._calg_aggregation(view_name, page, limit)

        return render(request, 'sites/summary.html', {
            'title': 'Summary',
            'page': page,
            'limit': limit,
            'total': total,
            'items': items
        })

    def _calg_aggregation(self, view_name, page, limit):
        f = self.aggr_functions[view_name]
        return f(page=page, limit=limit)
