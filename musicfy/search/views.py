#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'search/search.html'
