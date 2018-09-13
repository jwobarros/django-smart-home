# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse, Http404
from os import system

from assistant.models import RadioFrequencyRelay

#Temperature and Humidity Sensor Library
import Adafruit_DHT



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



@csrf_exempt
def TemperatureHumidityView(request):

    if request.is_ajax():

        sensor = Adafruit_DHT.AM2302
        pin = 23

        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

        if humidity is not None and temperature is not None:

            data = {"humidity": round(humidity, 2), "temperature": round(temperature, 2) }

            return JsonResponse(data, safe=False)


@csrf_exempt
def AudioView(request):

    if request.is_ajax() and request.method == "POST":
        audio = request.FILES
        print(audio)
        return JsonResponse('Foi porra', safe=False)
    raise Http404



