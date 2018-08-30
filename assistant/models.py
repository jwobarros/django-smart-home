# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Room(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class RadioFrequencyRelay(models.Model):
    name = models.CharField(max_length=30)
    room = models.ForeignKey(Room, on_delete = models.CASCADE)
    code_on = models.IntegerField()
    code_off = models.IntegerField()
    protocol = models.IntegerField()
    pulse = models.IntegerField()
    
    def __str__(self):
        return self.name + '-' + self.room.name

    def on(self):
        
        command = "/home/pi/assistant/SmartHome/assistant/433Utils/RPi_utils/codesend %i %i %i " % (self.code_on,  self.protocol, self.pulse) 
        
        return command

    def off(self):
        
        command = "/home/pi/assistant/SmartHome/assistant/433Utils/RPi_utils/codesend %i %i %i " % (self.code_off,  self.protocol, self.pulse)
        
        return command
