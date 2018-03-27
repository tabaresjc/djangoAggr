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
    def get_summary_by_site(cls, page=1, limit=10):
        q = cls.objects.values('site_id') \
                    .annotate(dataA=Sum('dataA'), dataB=Sum('dataB')) \
                    .order_by('-site_id')
        total = len(q)
        q = q[(page - 1) * limit:limit]

        items = []

        for d in q:
            items.append(cls(**d))

        return items, total

    @classmethod
    def get_summary_average_by_site(cls, page=1, limit=10):
        q = cls.objects.values('site_id') \
                    .annotate(dataA=Avg('dataA'), dataB=Avg('dataB')) \
                    .order_by('-site_id')

        total = len(q)
        q = q[(page - 1) * limit:limit]

        items = []

        for d in q:
            items.append(cls(**d))

        return items, total
