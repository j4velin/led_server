LEDserver
=========

A simple RESTful HTTP API to control WS2801 LED stripes. Additional "effects" can be added by placing in "effect_<name>.py" file in the same folder (see effect_snake.py for an example)

Install
-------

* sudo raspi-config -> Interface options -> SPI -> Enable
* sudo apt-get install python-pip -y
* sudo pip install adafruit-ws2801
* sudo pip install flask
