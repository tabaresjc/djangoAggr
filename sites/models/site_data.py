# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models as md
from site import Site
from django.db.models import Avg, Sum
from App3MW.helpers.paginator import PaginationHelper
from App3MW.helpers.timer import TimerHelper


class SiteData(md.Model):
    site = md.ForeignKey(Site, on_delete=md.CASCADE)
    date = md.DateField()
    dataA = md.DecimalField(max_digits=19, decimal_places=10)
    dataB = md.DecimalField(max_digits=19, decimal_places=10)
    created_at = md.DateTimeField(auto_now_add=True)
    updated_at = md.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)

    @classmethod
    def get_pagination(cls, site_id, page=1, limit=10):
        # in case the following are string
        if isinstance(page, basestring):
            page = int(page)

        if isinstance(limit, basestring):
            limit = int(limit)

        q = cls.objects.filter(site_id=site_id).order_by('-created_at')

        return PaginationHelper.get_paginator_items(q, page=page, limit=limit)

    @classmethod
    def get_sum_by_site(cls, page=1, limit=10):
        sites = Site.get_pagination(page, limit)
        total = Site.objects.count()

        items = []

        for site in sites:
            q = cls.objects.filter(site_id=site.id).values_list('dataA', 'dataB')

            # the results are a collection of tupples [(d1, d2), (d3, d4) ... (dn, dm)]
            # so  we should be able to use the transpose to get [(d1, d3, ..., dn), (d2, d4, ..., dm)]
            # then sum each group
            dataA, dataB = map(sum, zip(*list(q)))

            items.append(cls(site=site, dataA=dataA, dataB=dataB))

        return items, total

    @classmethod
    def get_sum_sql_by_site(cls, page=1, limit=10):
        table_name = cls.objects.model._meta.db_table
        ids = Site.get_ids(page, limit)
        total = Site.objects.count()

        query = ' SELECT' \
                '   0 AS id,' \
                '   `site_id`,' \
                ' 	SUM(`dataA`) AS dataA,' \
                ' 	SUM(`dataB`) AS dataB' \
                ' FROM' \
                '   `{}`' \
                ' WHERE `site_id` IN({})' \
                ' GROUP BY `site_id`' \
                ' ORDER BY `site_id` DESC'

        query = query.format(table_name,
                             ",".join(map(str, ids)))

        return list(cls.objects.raw(query)), total

    @classmethod
    def get_avg_by_site(cls, page=1, limit=10):
        sites = Site.get_pagination(page, limit)
        total = Site.objects.count()

        items = []

        def mean(l):
            return sum(l) / len(l)

        for site in sites:
            q = cls.objects.filter(site_id=site.id).values_list('dataA', 'dataB')

            # the results are a collection of tupples [(d1, d2), (d3, d4) ... (dn, dm)]
            # so  we should be able to use the transpose to get [(d1, d3, ..., dn), (d2, d4, ..., dm)]
            # then apply the mean to each group
            dataA, dataB = map(mean, zip(*list(q)))

            items.append(cls(site=site, dataA=dataA, dataB=dataB))

        return items, total

    @classmethod
    def get_avg_sql_by_site(cls, page=1, limit=10):
        table_name = cls.objects.model._meta.db_table
        ids = Site.get_ids(page, limit)
        total = Site.objects.count()

        query = ' SELECT' \
                '   0 AS id,' \
                '   `site_id`,' \
                ' 	AVG(`dataA`) AS dataA,' \
                ' 	AVG(`dataB`) AS dataB' \
                ' FROM' \
                '   `{}`' \
                ' WHERE `site_id` IN({})' \
                ' GROUP BY `site_id`' \
                ' ORDER BY `site_id` DESC'

        query = query.format(table_name,
                             ",".join(map(str, ids)))

        return list(cls.objects.raw(query)), total
