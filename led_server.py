import Adafruit_WS2801
import Adafruit_GPIO.SPI as SPI
import time
import json
from flask import Flask
from flask import request
import threading
import Queue

# required configureation
NUM_LEDS            = 50
EFFECT_START_LED    = 0
SPI_PORT            = 0
SPI_DEVICE          = 0

http_server = Flask(__name__)
leds = Adafruit_WS2801.WS2801Pixels(NUM_LEDS, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))
effect_queue = Queue.Queue(5)

@http_server.route('/leds', methods=['GET'])
def get_leds():
    led_states = []
    for i in range(NUM_LEDS):
        led_states.append(get_led(i))
    return json.dumps(led_states)

@http_server.route('/leds/<int:id>', methods=['GET'])
def get_led(id):
    led = dict()
    led["rgb"] = leds.get_pixel_rgb(id)
    return json.dumps(led)

def get_rgb(data):
    if type(data) is list:
        return data
    elif type(data) is dict and "rgb" in data:
        return data["rgb"]
    else:
        return None   

@http_server.route('/leds/<int:id>', methods=['POST'])
def set_led(id):
    if id > NUM_LEDS:
        return json.dumps({"status": "error", "message": "no LED with given index"}), 404
    data = request.json
    color = get_rgb(data)    
    if color is None:
        return json.dumps({"status": "error", "message": "rgb info missing"}), 400
    leds.set_pixel_rgb(id, *color)
    leds.show()
    return json.dumps({"status": "ok"})

@http_server.route('/leds', methods=['POST'])
def set_leds():
    colors = request.json
    if not type(colors) is list:
        return json.dumps({"status": "error", "message": "json array expected"}), 400
    changed = False
    for id in range(len(colors)):
        color = get_rgb(colors[id])
        if color is not None:
            leds.set_pixel_rgb(id, *color)
            changed = True
    if changed:
        leds.show()
        return json.dumps({"status": "ok"})
    else:
        return json.dumps({"status": "error", "message": "no color information given"}), 400
 
@http_server.route('/effect/<name>', methods=['POST'])
def run_effect(name):
    effect = __import__("effect_" + name)
    properties = request.json
    properties["num_leds"] = NUM_LEDS
    properties["start_offset"] = EFFECT_START_LED
    if not effect_queue.full():
        effect_queue.put((effect, properties))
    #effect.execute(leds, properties)
    return json.dumps({"status": "ok"})

def effects_worker():
    while True:
        effect, properties = effect_queue.get()
        effect.execute(leds, properties)


if __name__ == '__main__':
    worker = threading.Thread(target=effects_worker)
    worker.daemon = True
    worker.start()
    http_server.run(host='0.0.0.0')
    leds.clear()
    leds.show()
