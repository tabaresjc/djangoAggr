# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse


class SitesView(View):

    def get(self, request):
        return HttpResponse('Hello!')
