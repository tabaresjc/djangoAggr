# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models as md


class Site(md.Model):
    name = md.CharField(max_length=200)
    created_at = md.DateTimeField(auto_now_add=True)
    updated_at = md.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        indexes = [
            md.Index(fields=['name'])
        ]

    @classmethod
    def get_sites(cls, page=1, limit=10):
        q = cls.objects.order_by('-created_at')
        total = q.count()
        return q[(page - 1) * limit:limit], total
