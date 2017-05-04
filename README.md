# DHT11 Python library for Pycom

This simple class can be used for reading temperature and humidity values from DHT11 sensor on Pycom Board. Thanks to szazo for the original source code.

# Usage

1. Instantiate the `DHT11` class with the pin number as constructor parameter.
2. Call `read()` method, which will return `DHT11Result` object with actual values and error code. 

For example:

```python
import pycom
import time
from machine import Pin
from dth import DTH11

pycom.heartbeat(False)
pycom.rgbled(0x000008) # blue
th = DTH11(Pin('P3', mode=Pin.OPEN_DRAIN))
time.sleep(2)
result = th.read()
if result.is_valid():
    pycom.rgbled(0x001000) # green
    print("Temperature: %d C" % result.temperature)
    print("Humidity: %d %%" % result.humidity)

For working example, see `dht11_example.py` (you probably need to adjust pin for your configuration)


# License

This project is licensed under the terms of the MIT license.
