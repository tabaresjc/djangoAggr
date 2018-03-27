# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models as md
from App3MW.helpers.paginator import PaginationHelper


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
    def get_pagination(cls, page=1, limit=10):
        # in case the following are string
        if isinstance(page, basestring):
            page = int(page)

        if isinstance(limit, basestring):
            limit = int(limit)

        q = cls.objects.order_by('-created_at')

        return PaginationHelper.get_paginator_items(q, page=page, limit=limit)

    @classmethod
    def get_ids(cls, page=1, limit=10):
        q = cls.objects.values_list('id', flat=True).order_by('-created_at')

        offset = (page - 1) * limit

        return list(q[offset:offset+limit])

    @classmethod
    def get_count(cls):
        return cls.objects.count()
