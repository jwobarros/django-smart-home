# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from assistant.models import Room, RadioFrequencyRelay

# Register your models here.

admin.site.register(Room)
admin.site.register(RadioFrequencyRelay)
