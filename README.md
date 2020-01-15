LEDserver
=========

A simple RESTful HTTP API to control WS2801 LED stripes. Additional "effects" can be added by placing in "effect_<name>.py" file in the same folder (see effect_snake.py for an example)

Install
-------

* sudo raspi-config -> Interface options -> SPI -> Enable
* sudo apt-get install python-pip -y
* sudo pip install adafruit-ws2801
* sudo pip install flask

Usage
-----

* GET on http://<ip>:5000/leds shows the state (e.g. color) of all LEDs
* GET on http://<ip>:5000/leds/<id> shows the state (e.g. color) of a specific LED
* POST on .../leds lets you change the color of all LEDs:
  * MimeType: application/json
  * Example body (sets LED#1 to red, LED#2 to green):
     ```javascript
     [
        [ 255, 0, 0 ],
        [ 0, 255, 0 ]
     ]
     ```
* POST on .../leds/<id> lets you change the color of a specific LED:
  * MimeType: application/json
  * Example body (sets the LED to blue):
     ```javascript
     [ 0, 0, 255 ]
     ```
* POST on .../effec/<name> triggers the effect effect_<name>.py:
  * MimeType: application/json
  * body depends on the effect, example for the snake effect (POST on .../effect/snake):
     ```javascript
     {
	      "color": [255, 0, 0],
	      "delay": 0.1,
	      "length": 5
     }
     ```
