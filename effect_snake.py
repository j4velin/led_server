# sample effect
# you can add your own effects by creating an effect_<name>.py file
# with an 'execute(leds, properties) function as shown below

import time

# it's a good idea to have some default properties
defaults = { "length": 5, "color": [255, 0, 0], "delay": 0.1 }

# the 'execute' method is executed when a POST request on .../effects/<name> is received
# this method should return when the effect is done, as long a one effect is executed, all
# other received effect requests get queued (until the effect_queue is full)
# properties contains the data from the POST request
def execute(leds, properties):
    # the user might have forgotten a property so merge with the defaults
    p = dict(defaults.items() + properties.items())
    length = p["length"]
    # the special key 'num_leds' is always set and contains the amount of LEDs
    # as configured in the led_server.py
    max_leds = p["num_leds"]
    color = p["color"]
    delay = p["delay"]
    leds.clear()
    leds.show()
    for i in range(max_leds + length):
        if i < max_leds:
            leds.set_pixel_rgb(i, *color)
        if i >= length:
            leds.set_pixel_rgb(i - length, 0, 0, 0)
        leds.show()
        time.sleep(delay)
    # when the effect is done, clear all LEDs
    leds.clear()
    leds.show()
