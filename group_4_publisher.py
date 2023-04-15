#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 11:44:07 2023

@author: carlosmolina
"""
import data_generator as gen1
import random

import time
import paho.mqtt.client as mqtt
import json

print(gen1.Sample_set().base_temperature, "C")

print(gen1.Sample_set().dict[random.randint(1, 3)][0])

my_data1 = {
    'Day': 0,
    'Time': time.asctime(),
    'City': gen1.Sample_set().dict[random.randint(1, 3)][0],
    'Temperature': gen1.Sample_set().base_temperature
    }


client = mqtt.Client()
client.connect('localhost', 1883)
client.loop_start()
time.sleep(1)
for x in range(10):
    my_data1['Day'] = x
    my_data1['Time'] = time.asctime()
    my_data1['City'] = gen1.Sample_set().dict[random.randint(1, 3)][0]
    my_data1['Temperature'] = gen1.Sample_set().base_temperature
    client.publish('Group4', json.dumps(my_data1))
    print('Message sent')
    time.sleep(7)
client.loop_stop()

