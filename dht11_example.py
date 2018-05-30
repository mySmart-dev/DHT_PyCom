import pycom
import time
from machine import Pin
from dht import DHT

pycom.heartbeat(False)
pycom.rgbled(0x000008) # blue
th = DHT(Pin('P3', mode=Pin.OPEN_DRAIN),0)
time.sleep(2)
result = th.read()
if result.is_valid():
    pycom.rgbled(0x001000) # green
    print("Temperature: %d C" % result.temperature)
    print("Humidity: %d %%" % result.humidity)