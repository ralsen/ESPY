from machine import Pin
import time

import time
import os
import json
import config

import wifi as wf
import webserver as ws
import settings as set
import timers as TM
import config as cfg
import webserver


p0 = Pin(2, Pin.OUT) 
p1 = Pin(0, Pin.IN)

start = time.ticks_ms()

print(set.MyName)
print(set.Version)

print("Key service started!")            
print("10ms Timer service started!")
TM.downTimers()

print("Hash FAILED !!!")
print("Hello from device: " )
print("DEV_TYPE")
print("Function:          ")
print("MAC-Adress:        " )
print("1s timer services started!")
print("\r\neverything is initialized, let's go ahead now ->\r\n")

print("---> Directory:")
print(os.listdir('/'))


def LED_Timer(timer):
    #print(f"task-ID: {blink.timer_id} - {blink.name} executed")
    p0.value(not p0.value())

if (not cfg.loadConfig()):
    print("!!! P A N I K !!! could not load configuration")
    panik =  TM.freeTimer("Panik", 25, LED_Timer)
    panik.start()
    while True:
        pass

wifi = wf.do_connect(cfg.confData["SSID"], cfg.confData["password"])
if (wifi == None):
    print("OJE!!!")
else:
    print(f"\r\n{wifi}")

TM.downTimers.downCnters["noch mehr"] = 300

def taskexample(timer):
    #print(f"task-ID: {timerexample.timer_id} - {timerexample.name} executed")
    pass

blink = TM.freeTimer("Blinker", 250, LED_Timer)
blink.start()

timerexample = TM.freeTimer("Timer_Example", 5000, taskexample)
timerexample.start()

ws.webserv()
    
while True:
    """
    print(f"elapsed time: {(time.ticks_ms() - start) / 1000}")    
    if p1.value():
        print("Button is released.")
    else:
        print("Button is pressed.")
    """
    try:
        if TM.downTimers.downCnters["noch mehr"] == 0:
            TM.downTimers.downCnters.pop("noch mehr", "")
    except:
        pass
    print("active downConuters:")
    for key, value in TM.downTimers.downCnters.items():
        print(f"{key} = {value}")
    print("")
    time.sleep(0.25)
