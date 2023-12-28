from machine import Pin
import machine
import time

import time
import os
import json
import config
import urequests

import wifi as wf
import webserver as ws
import settings as set
import timers as TM
import config as cfg



p0 = Pin(2, Pin.OUT) 
p1 = Pin(0, Pin.IN)

start = time.ticks_ms()

print(set.MyName)
print(set.Version)

print("Key service started!")            
print("10ms Timer service started!")

def byte2str (value):
    strval = ''
    for byte in value:
        strval += '{:02X}'.format(byte) + ":"
    return strval[:-1]

cf = cfg.cfg()

TM.downTimers()

def LED_Timer(timer):
    #print(f"task-ID: {blink.timer_id} - {blink.name} executed")
    p0.value(not p0.value())

cfgData = cf.loadConfig()
if (not cfgData):
    print("!!! P A N I K !!! could not load configuration")
    panik =  TM.freeTimer("Panik", 25, LED_Timer)
    panik.start()
    while True:
        pass
    
cfgData['uptime'] = 0

wifi = wf.do_connect(cfgData["SSID"], cfgData["password"])
if (wifi == None):
    print("OJE!!!")
else:
    print(f"\r\n{wifi.ifconfig()}")

cfgData["IP"] = wifi.ifconfig()[0]
cfgData["Server"] = wifi.ifconfig()[2]
cfgData["MAC"] = byte2str(wifi.config('mac'))
cfgData['hostname'] = cfgData['name'] + '_' + cfgData['MAC'].replace(':', '_')
cfgData['chipID'] = byte2str(machine.unique_id())
cf.saveConfig(cfgData)

print(f"running with configuration:\r\n{cfgData}")
print(f"Hello from device: {cfgData['hostname']}" )
print("DEV_TYPE: ")
print("FNC_TYPE: ")
print(f"MAC-Adress:        {cfgData['MAC']}" )
print("1s timer services started!")
print("\r\neverything is initialized, let's go ahead now ->\r\n")

print("---> Directory:")
print(os.listdir('/'))

def handle_uptimer(timer):
    cfgData['uptime'] += 1
    
uptimer = TM.freeTimer('Uptimer', 1000, handle_uptimer)
uptimer.start()

TM.downTimers.downCnter["noch mehr"] = 300

cfgData["WiFi"] = 0

def taskexample(timer):
    print(f"task-ID: {timerexample.timer_id} - {timerexample.name} executed")
    cfgData['WiFi'] = 'SSID-Wert'
    try:
        print(f"sending to http://192.168.2.87:8081:\r\n{cfgData}")
        #response = urequests.post('http://192.168.2.87:8080', json=cfgData)
        #print(response.content)
        cfgData['goodTrans'] += 1
    except:
        cfgData['badTrans'] += 1
        print('habe niemanden erreicht')
    pass

blink = TM.freeTimer("Blinker", 500, LED_Timer)
blink.start()

timerexample = TM.freeTimer("Timer_Example", 10000, taskexample)
timerexample.start()

#response = urequests.post("http://192.168.2.87:8080", json=cfgData)
#print(response.content)

ws.webserv(cfgData)
#wstimer = TM.freeTimer("WebServer", 100, ws.webserv.do_web)
#print(f"---> wstimer: {wstimer}")
#ws.webserv.do_web()
    
while True:
    """
    print(f"elapsed time: {(time.ticks_ms() - start) / 1000}")    
    if p1.value():
        print("Button is released.")
    else:
        print("Button is pressed.")
    """
    try:
        if TM.downTimers.downCnter["noch mehr"] == 0:
            TM.downTimers.downCnter.pop("noch mehr", "")
    except:
        pass
    print("active downConuters:")
    for key, value in TM.downTimers.downCnter.items():
        print(f"{key} = {value}")
    print("")
    time.sleep(5)