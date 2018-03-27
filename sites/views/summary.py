# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views import View
from django.http import Http404
from django.shortcuts import render
from sites.models import Site, SiteData
from App3MW.helpers.paginator import PaginationHelper

class SummaryView(View):

    aggr_functions = {
        'sum': 'get_sum_by_site',
        'sum-sql': 'get_sum_sql_by_site',
        'avg': 'get_avg_by_site',
        'avg-sql': 'get_avg_sql_by_site',
    }

    def get(self, request, page=1, limit=10):
        items = self._calg_aggregation(request, page, limit)

        return render(request, 'sites/summary.html', {
            'title': 'Summary',
            'items': items,
        })

    def _calg_aggregation(self, request, page, limit):
        func_name = request.resolver_match \
            .view_name.replace('-paginated', '') \
            .split(':').pop()

        fn = self.aggr_functions.get(func_name)

        if not fn:
            raise Http404()

        if isinstance(page, basestring):
            page = int(page)

        if isinstance(limit, basestring):
            limit = int(limit)

        q, total = getattr(SiteData, fn)(page=page, limit=limit)

        items = PaginationHelper.get_paginator_items(q, page=page, limit=limit, total=total)

        return items
