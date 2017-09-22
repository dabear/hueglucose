#!/usr/bin/env python
from __future__ import division
from phue import Bridge
import nightscout
import time
import sys
from datetime import datetime

bridge_ip = "192.168.1.213"
lightname = "dialys1"
nightscout_url = "https://bjorningedia4.herokuapp.com"

#pip install phue
#sudo pip install git+https://github.com/ps2/python-nightscout.git

b = Bridge(bridge_ip)
b.connect()
all_lights = b.get_light_objects('name')
light = all_lights[lightname]

api = nightscout.Api(nightscout_url)

COLORS = {
    "green": [0.1724, 0.7468],
    "red": [0.6787, 0.3010],
    "blue": [0.1590, 0.1221],
    "yellow": [0.4234, 0.4846],
    "purple": [0.2451, 0.0979],
    "lavender": [0.3077, 0.3058],
}

def blink(light, times=1,sleep=3):
    for i in range(0, times):
        print("alerting")
        light.alert="select"
        if times > 1:
            time.sleep(sleep)
    

def set_color(light, color):
    color=COLORS.get(color, None)
    
    light.on=True
    light.brightness = 127
    light.xy=color

  
#if glucose is really low, blink!
#  blink(light, times=3)

if __name__ == '__main__':
#if True:
    try:
        entry = api.get_sgvs({'count':1})[0]
    except IndexError:
        print("could not get glucose")
        sys.exit(-1)
    except:
        print("could not connect to nightscout api at: %s".format(nightscout_url) )
        sys.exit(-2)
        
    mmol = entry.sgv / 18
    should_blink = False
    
    if mmol > 10.5:
        color = "red"
    elif mmol > 5.3:
        color = "green"
    elif mmol > 4.5:
        color = "yellow"
    else:
        color = "red"
        should_blink=True
        
    set_color(light, color)
    if should_blink:
        blink(light, 3)

    


