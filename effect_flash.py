import time

defaults = { "color": [255, 0, 0], "delay": 0.1, "flashes": 5 }

def execute(leds, properties):
    p = dict(defaults.items() + properties.items())
    flashes = p["flashes"]
    max_leds = p["num_leds"]
    start = p["start_offset"]
    color = p["color"]
    delay = p["delay"]
    leds.clear()
    leds.show()
    for i in range(flashes):
        for led in range(start, max_leds):
            leds.set_pixel_rgb(led, *color)
        leds.show()
        time.sleep(delay)
        leds.clear()
        leds.show()
        time.sleep(delay)
    leds.clear()
    leds.show()
