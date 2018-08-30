from django.urls import path
from assistant.views import OnOffView

urlpatterns = [
    path('on-off', OnOffView, name='on_off'),
]
