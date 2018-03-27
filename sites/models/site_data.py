# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models as md
from .site import Site
from django.db.models import Avg, Sum


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
    def get_data_by_site(cls, site_id, page=1, limit=10):
        q = cls.objects.filter(site_id=site_id).order_by('-created_at')
        total = q.count()
        return q[(page - 1) * limit:limit], total

    @classmethod
    def get_sum_by_site(cls, page=1, limit=10):
        q = cls.objects.values('site_id') \
            .annotate(dataA=Sum('dataA'), dataB=Sum('dataB')) \
            .order_by('-site_id')

        q = q[(page - 1) * limit:limit]

        items = [cls(**d) for d in q]

        # total should be the number of sites available
        total = Site.get_total()

        return items, total

    @classmethod
    def get_sum_sql_by_site(cls, page=1, limit=10):
        query = ' SELECT' \
                '   0 AS id,' \
                '   `site_id`,' \
                ' 	SUM(`dataA`) AS dataA,' \
                ' 	SUM(`dataB`) AS dataB' \
                ' FROM' \
                '   `{}`' \
                ' GROUP BY `site_id`' \
                ' ORDER BY `site_id` DESC'

        query = query.format(cls.objects.model._meta.db_table)
        q = cls.objects.raw(query)

        # total should be the number of sites available
        total = Site.get_total()

        return q[(page - 1) * limit:limit], total

    @classmethod
    def get_avg_by_site(cls, page=1, limit=10):
        q = cls.objects.values('site_id') \
            .annotate(dataA=Avg('dataA'), dataB=Avg('dataB')) \
            .order_by('-site_id')

        q = q[(page - 1) * limit:limit]

        items = [cls(**d) for d in q]

        # total should be the number of sites available
        total = Site.get_total()

        return items, total

    @classmethod
    def get_avg_sql_by_site(cls, page=1, limit=10):
        query = ' SELECT' \
                '   0 AS id,' \
                '   `site_id`,' \
                ' 	AVG(`dataA`) AS dataA,' \
                ' 	AVG(`dataB`) AS dataB' \
                ' FROM' \
                '   `{}`' \
                ' GROUP BY `site_id`' \
                ' ORDER BY `site_id` DESC'

        query = query.format(cls.objects.model._meta.db_table)
        q = cls.objects.raw(query)

        # total should be the number of sites available
        total = Site.get_total()

        return q[(page - 1) * limit:limit], total
