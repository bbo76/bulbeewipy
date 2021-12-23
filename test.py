from bulbeewipy import BeewiSmartLight
from time import sleep

b = BeewiSmartLight("D0:39:72:CC:AA:48")
b.turnOn()
sleep(8)
b.turnOff()
