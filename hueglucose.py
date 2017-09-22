from phue import Bridge
b = Bridge('192.168.1.213')
b.connect()
all_lights = b.get_light_objects('name')



light = all_lights["Hue color lamp 3"]

green = [0.1724, 0.7468]
red = [0.6787, 0.3010]
blue = [0.1590, 0.1221]
yellow = [0.4234, 0.4846]
purple = [0.2451, 0.0979]

def blink(light):
    light.alert="select"

def set_color(light, color):
    light.on=True
    light.brightness = 127
    light.xy=color
    

set_color(light, green)

    


