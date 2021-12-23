from bulbeewipy import BeewiSmartLightPoller
from time import sleep

b = BeewiSmartLightPoller("D0:39:72:CC:AA:48")
b.turn_on()
sleep(8)
b.turn_off()