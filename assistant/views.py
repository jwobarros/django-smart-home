# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from os import system

from assistant.models import RadioFrequencyRelay
# Create your views here.

@csrf_exempt
def OnOffView(request):
    
    if request.method == 'POST' and request.is_ajax():
      command = request.POST.get('command', '') 
      id = request.POST.get('id', '')

      RFR = RadioFrequencyRelay.objects.get(id=id)

      #Power On
      if command == 'on':
           
           system(RFR.on())
           
           return HttpResponse('Ligado')

      #Power Off 
      system(RFR.off())
      return HttpResponse('Desligado')
