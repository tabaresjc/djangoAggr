# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views import View
from django.shortcuts import render


class IndexView(View):

    def get(self, request):
        return render(request, 'sites/index.html', {
            'title': 'Sites'
        })
