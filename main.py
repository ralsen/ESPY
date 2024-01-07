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
print("1s timer services started!")

def byte2str (value):
    strval = ''
    for byte in value:
        strval += '{:02X}'.format(byte) + ":"
    return strval[:-1]

cf = cfg.cfg()

myTimers = TM.Timers()

def LED_Timer(timer):
    #print(f"task-ID: {blink['id']} - {blink['name']} executed")
    p0.value(not p0.value())

cfgData = cf.loadConfig()
if (not cfgData):
    print("!!! P A N I K !!! could not load configuration")
    panik =  myTimers.append("Panik", 25, LED_Timer)
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

print(f"\r\n---> Hello from device: {cfgData['hostname']} <---" )
print(f"Architecture:      {cfgData['Architecture']}")
print(f"DEV_TYPE:          {cfgData['Hardware']}")
print(f"FNC_TYPE:          {cfgData['Type']} ")
print(f"MAC-Adress:        {cfgData['MAC']}" )
print(f"running with configuration:\r\n{cfgData}")
print("\r\neverything is initialized, let's go ahead now ->\r\n")

print("---> Directory:")
print(os.listdir('/'))

def handle_uptimer(timer):
    cfgData['uptime'] += 1
    
myTimers.append('Uptimer', 1000, handle_uptimer)

# TM.downTimers.downCnter["noch mehr"] = 300

cfgData["WiFi"] = 0

def taskexample(timer):
    print(f"task-ID: {timerexample['id']} - {timerexample['name']} executed")
    cfgData['WiFi'] = 'SSID-Wert'
    try:
        #print(f"sending to http://192.168.2.87:8081:\r\n{cfgData}")
        #response = urequests.post('http://192.168.2.87:8080', json=cfgData)
        #print(response.content)
        cfgData['goodTrans'] += 1
    except:
        cfgData['badTrans'] += 1
        print('habe niemanden erreicht')
    pass

blink = myTimers.append("Blinker", 500, LED_Timer)

timerexample = myTimers.append("Timer_Example", 10000, taskexample)

#response = urequests.post("http://192.168.2.87:8080", json=cfgData)
#print(response.content)

#ws.webserv(cfgData)
#wstimer = TM.freeTimer("WebServer", 100, ws.webserv.do_web)
#print(f"---> wstimer: {wstimer}")
#ws.webserv.do_web()
  
#print(TM.Timers('Timer_1', 500, LED_Timer))  
#TM.Timers('Timer_2', 1500, taskexample)  
#print(TM.Timers.timers)

while True:
    """
    print(f"elapsed time: {(time.ticks_ms() - start) / 1000}")    
    if p1.value():
        print("Button is released.")
    else:
        print("Button is pressed.")
    """
    print("active downConuters:")
    #for t in TM.Timers.timers.items():
    #    print (t)
    print(TM.Timers.timers)
    print("")
    time.sleep(5)