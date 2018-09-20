# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse, Http404
from os import system

import speech_recognition as sr
import wave, struct, math

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
           
           return JsonResponse('Ligado', safe=False)

      #Power Off 
      system(RFR.off())
      return JsonResponse('Desligado', safe=False)



@csrf_exempt
def TemperatureHumidityView(request):

    if request.is_ajax():

        sensor = Adafruit_DHT.AM2302
        pin = 23

        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

        if humidity is not None and temperature is not None:

            data = {"humidity": round(humidity, 2), "temperature": round(temperature, 2) }

            return JsonResponse(data, safe=False)



def packSoundFrame(nChannels,sampleWidth,values):

    formats = (None,'B','h',None,'l')
    offsets = (None,127, 0, None,0)

    format = '<'+formats[sampleWidth]*nChannels
    offset = offsets[sampleWidth] 
    volume = 2**(8*sampleWidth-1) - 1

    args = [format]
    for value in values:
        args.append(int(offset + volume*value)) 
    return struct.pack( *args )


@csrf_exempt
def AudioView(request):

    lFreq =  880.00      
    rFreq = 1760.00

    if request.is_ajax() and request.method == "POST":
        audio = request.FILES['file'].read()

        r = sr.Recognizer()

        with wave.open("test.wav", "w") as audio_data:
            audio_data.setnchannels(2)
            audio_data.setsampwidth(2)
            audio_data.setframerate(48000.0)
            audio_data.setnframes(audio_data.getnframes())
            nSamples = 5 * 48000
            for i in range(int(nSamples)):
                l = math.cos(lFreq*math.pi*float(i)/float(48000))
                r = math.cos(rFreq*math.pi*float(i)/float(48000))
                data = packSoundFrame(2, 2, [l,r])
                audio_data.writeframesraw( data )
            # audio_data.writeframesraw(audio)
            #audio_data.writeframes(audio)
            print(audio_data.getnframes()) 

        with sr.AudioFile("test.wav") as source:
            audio = r.listen(source)

        data = ""
        try:
            data = r.recognize_google(audio, language="pt-BR")
            print("data")
        except sr.UnknownValueError:
            print("Não entendi.")
        except sr.RequestError as e:
            print("Sem resultados da API do Google")

        return JsonResponse('Teste', safe=False)
    raise Http404



