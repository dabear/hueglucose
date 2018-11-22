#!/usr/bin/env python
from __future__ import division
from phue import Bridge
import nightscout
import time
import sys
import datetime
from dateutil.tz import tzlocal
import pytz
from socket import gethostname

bridge_ip = "192.168.1.213"
lightname = "dialys1"
nightscout_url = "https://bjorningedia4.herokuapp.com"

#sudo pip install phue
#sudo pip install git+https://github.com/ps2/python-nightscout.git

b = Bridge(bridge_ip)
b.connect()
all_lights = b.get_light_objects('name')
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
        print("Blinking light {0} times".format(times))
        light.alert="select"
        if times > 1:
            time.sleep(sleep)
    

def set_color(light, color):
    
    print("Trying to set color to {0}".format(color))
    color=COLORS.get(color, None)
    
    light.on=True
    light.brightness = 110
    light.xy=color
    print("Color was set to {0}".format(color))

    if not light.reachable:
        print("However, the light was not reachable :(")

def get_nowtime():
    zone = tzlocal()
    return datetime.datetime.now().replace(tzinfo=zone)
def get_entry_date(entry):
    zone = tzlocal()
    return entry.date.replace(tzinfo=zone)

if "bjorningedia4.herokuapp.com" in nightscout_url and not "bjorninge" in gethostname():
    print("Error: You should probably change the nightscout_url!")
    sys.exit(0)
 
#if glucose is really low, blink!
#  blink(light, times=3)

if __name__ == '__main__':
#if True:
    now = get_nowtime()
    print("Datetime is now {0}".format(now))
    try:
        entry = api.get_sgvs({'count':1})[0]
    except IndexError:
        print("Could not get glucose")
        sys.exit(-1)
    except:
        print("Could not connect to nightscout api at: {0}".format(nightscout_url) )
        sys.exit(-2)
    
    try:
        light = all_lights[lightname]
    except KeyError:
        print("Could not find light '{0}', Exiting..".format(lightname))
        sys.exit(-3)
    except:
        print("Could not find hue lights, Exiting...")
        sys.exit(-3)
    mmol = entry.sgv / 18
    should_blink = False
    
    #
    # We consider the system date and the entry glucose date timestamps to be within
    # the same timezone. This may not always be the case, but for our purposes it
    # is a reasonable assumption.
    #
    
    
    minago15 = now - datetime.timedelta(minutes=15)
    minago30 = now - datetime.timedelta(minutes=30)
    minago1 = now - datetime.timedelta(minutes=1)
    entry_date = get_entry_date(entry)
    
    print("Glucose datetime is {0}. Glucose  is {1} mgdl/ {2} mmol".format(entry_date, entry.sgv, mmol))
    
    #first check gluicose timestamp
    #only consider glucose value if the timestamp is not too old
    if entry_date <= minago30:
        print("Glucose entry is older than 30 minutes old")
        color = "red"
    elif entry_date <= minago15:
        print("Glucose entry is older than 15 minutes old")
        color = "purple"
    else:
        #entry date is up to 15 minutes old, we consider that valid
        
        if mmol > 10.5:
            print("Glucose is between 15.3 and 10.5")
            color = "red"
        elif mmol > 5.3:
            print("Glucose is between 5.3 and 10.5")
            color = "lavender"
        elif mmol > 4.5:
            print("Glucose is between 4.5 and 5.3")
            color = "purple"
        else:
            print("Glucose is below 4.5")
            color = "red"
            should_blink=True
        
    set_color(light, color)
    if should_blink:
        blink(light, 3)

    


