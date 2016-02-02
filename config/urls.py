#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.conf.urls import url, include
from django.contrib import admin

from musicfy.search import urls as search_urls
urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # Your stuff: custom urls includes go here
    url(r'', include(search_urls, namespace='search')),
]
