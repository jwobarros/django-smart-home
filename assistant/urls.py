from django.urls import path
from assistant.views import OnOffView, TemperatureHumidityView, AudioView

urlpatterns = [
    path('on-off', OnOffView, name='on_off'),
    path('temperature-humidity', TemperatureHumidityView, name='temperature_humidity'),
    path('audio', AudioView, name='audio')
]
