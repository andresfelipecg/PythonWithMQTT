#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 11:46:46 2023

@author: carlosmolina
"""


import paho.mqtt.client as mqtt
import json
#this function is called when the subscriber receives a message

def on_message(client, userdata, message):
    data1 = message.payload.decode('utf-8')
    obj = json.loads(data1)
    print(f'Day: {obj["Day"]}')
    print(f'Time: {obj["Time"]}')
    print(f'{obj["Temperature"]}',"C" , end=' ')
    print(f'{obj["City"]}', end=' ')
    #print(f'{obj["BloodPressure"]["Diastolic"]}(dia)', end=' ')
    #print(f'{obj["BloodPressure"]["Systolic"]}(sys) ')
client = mqtt.Client()
client.on_message = on_message
client.connect('localhost', 1883)
client.subscribe('Group4')
while True:
    client.loop_forever()