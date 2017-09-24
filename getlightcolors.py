#!/usr/bin/env python
from phue import Bridge

print("Printing a list of all lights and their current color")
bridge_ip = "192.168.1.213"

b = Bridge(bridge_ip)
b.connect()
all_lights = b.get_light_objects('name')

for name, light in all_lights.items():
    print("Lamp light {0}: {1}".format(light.name, light.xy))
    if not light.reachable:
        print("Lamp light currently not reachable!\n")