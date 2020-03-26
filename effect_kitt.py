import time

defaults = { "length": 5, "color": [255, 0, 0], "delay": 0.1, "loops": 1 }

def execute(leds, properties):
    p = dict(defaults.items() + properties.items())
    length = p["length"]
    max_leds = p["num_leds"]
    start = p["start_offset"]
    color = p["color"]
    delay = p["delay"]
    loops = p["loops"]
    leds.clear()
    leds.show()
    for l in range(loops):
        for i in range(start, max_leds + length):
            if i < max_leds:
                leds.set_pixel_rgb(i, *color)
            if i >= length:
                leds.set_pixel_rgb(i - length, 0, 0, 0)
            leds.show()
            time.sleep(delay)
        for i in range(max_leds - 1, -length + start, -1):
            if i >= start:
                leds.set_pixel_rgb(i, *color)
            if i + length < max_leds:
                leds.set_pixel_rgb(i + length, 0, 0, 0)
            leds.show()
            time.sleep(delay)
    leds.clear()
    leds.show()
