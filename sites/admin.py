# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from sites.models import Site, SiteData

admin.site.register(Site)
admin.site.register(SiteData)
