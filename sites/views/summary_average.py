# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views import View
from django.shortcuts import render


class SummaryAvgView(View):

    def get(self, request):
        return render(request, 'sites/summary_average.html', {
            'title': 'Summary'
        })
