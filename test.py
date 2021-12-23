from bulbeewipy import BeewiSmartLigh
from time import sleep

b = BeewiSmartLigh("D0:39:72:CC:AA:48")
b.turnOn()
sleep(8)
b.turnOff()