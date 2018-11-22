#!/usr/bin/env python
from phue import Bridge
import sys


def runit(bridge_ip, lightname):
    try:
        b = Bridge(bridge_ip)
        b.connect()
        all_lights = b.get_light_objects('name')
    except Exception as e:
        print("Could not connect to light: {}".format(e.message))
        sys.exit()

    print("Printing all lights and their colors:")
    for name, light in all_lights.items():
        print("Lamp light {0} color tuple: {1}".format(light.name, light.xy))
        if not light.reachable:
            print("Lamp light currently not reachable!")
        
        print("")

if __name__ == "__main__":
    bridge_ip = sys.argv[1] #"192.168.1.211"
    lightname = sys.argv[2] #"dialys1"
    
    runit(bridge_ip, lightname)
