# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models as md
from .site import Site


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
