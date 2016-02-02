#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from django.utils.encoding import smart_str
from django.views.generic import View

import pafy


class HomeView(View):
    template_name = 'search/search.html'

    def get(self, request):
        return render(request, self.template_name)

    @staticmethod
    def post(request):
        url = request.POST.get('video_url')
        video = pafy.new(url)
        best_audio = video.getbestaudio()
        best_audio.download(
            filepath=str(settings.MEDIA_ROOT + "/songs"),
        )
        song_name = video.title + '.' + best_audio.extension
        response = HttpResponse(content_type='application/force-download')
        response['X-Sendfile'] = smart_str(settings.MEDIA_ROOT + "/songs")
        response['Content-Disposition'] = 'attachment; filename=%s' % \
                                          smart_str(song_name)
        return response
