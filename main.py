from machine import Pin
import machine
import time
import time
import os
import urequests
import binascii

import wifi as wf
import webserver as ws
import settings as set
import timers as TM
import config as cfg
import util as ut
import DS1820 as DS

p0 = Pin(2, Pin.OUT) 
p1 = Pin(0, Pin.IN)

start = time.ticks_ms()

print(set.MyName)
print(set.Version)

print("Key service started!")            
print("10ms Timer service started!")
print("1s timer services started!")

sysData = {}

cf = cfg.cfg()

myTimers = TM.Timers()
myDS1820 = DS.DS1820()
print(myDS1820.read())

# ############################# Timer handlers ############################## 
def LED_Timer(timer):
    #print(f"task-ID: {blink['id']} - {blink['name']} executed")
    p0.value(not p0.value())

def handle_taskexample(timer):
    print(f"task-ID: {timerexample['id']} - {timerexample['name']} executed")
    sysData['WiFi'] = "RSSI"
    srvData = ut.ServerInfo(set.ServerContent, cfgData, sysData)
    if srvData == False:
        print("no data available !!!")
        return
    try:
        print(f"sending to http://192.168.2.87:8080:\r\n{srvData}")
        response = urequests.post('http://192.168.2.87:8080', json=srvData)
        print(response.content)
        sysData['goodTrans'] += 1
    except:
        sysData['badTrans'] += 1
        print('habe niemanden erreicht')
    pass

def handle_uptimer(timer):
    sysData['uptime'] += 1

def handle_DS1820(timer):
    print(myDS1820.read())
# ############################## Timer handlers ##############################

loaded_cfgData = cf.loadConfig()
cfgData = loaded_cfgData[1]

print(f"---> {cfgData}")
if loaded_cfgData[1] == False:
    print("!!! P A N I K !!! could not load configuration")
    panik =  myTimers.append("Panik", 25, LED_Timer)
    while True:
        pass
    
sysData['uptime'] = 0
sysData['badTrans'] = 0
sysData['goodTrans'] = 0
sysData['RSSI'] = 0

blink = myTimers.append("Blinker", 500, LED_Timer)
maxtimer = myTimers.append('maxtimer', 2000)
utimer = myTimers.append('Uptimer', 1000, handle_uptimer)
DSTimer = myTimers.append('DS1820', 150000, handle_DS1820)
timerexample = myTimers.append("Timer_Example", 300000, handle_taskexample)

print(blink)
print(maxtimer)
print(utimer)

wifi = wf.do_connect(cfgData["SSID"], cfgData["password"])
if (wifi == None):
    print("OJE!!!")
else:
    print(f"\r\n{wifi.ifconfig()}")

cfgData["IP"] = wifi.ifconfig()[0]
cfgData["Server"] = wifi.ifconfig()[2]
cfgData["MAC"] = binascii.hexlify(wifi.config('mac')).decode()
#cfgData['hostname'] = cfgData['name'] + '_' + cfgData['MAC'].replace(':', '_') # this is the better line
cfgData['name'] = cfgData['hostname'] + '_' + cfgData['MAC'].replace(':', '_') #for compatibility use this
cfgData["chipID"] = binascii.hexlify(machine.unique_id()).decode()
cf.saveConfig(cfgData)

print(f"\r\n---> Hello from device: {cfgData['hostname']} <---" )
print(f"Architecture:      {cfgData['Architecture']}")
print(f"DEV_TYPE:          {cfgData['Hardware']}")
print(f"FNC_TYPE:          {cfgData['Type']} ")
print(f"MAC-Adress:        {cfgData['MAC']}")
print(f"Network:           {cfgData['SSID']}")
print(f"IP-Adress:         {cfgData['IP']}")
print(f"running with configuration:\r\n{cfgData}")
print("\r\neverything is initialized, let's go ahead now ->\r\n")

print("---> Directory:")
print(os.listdir('/'))

cfgData["WiFi"] = 0

#ws.webserv(cfgData)
#ws.webserv.do_web()
  
#print(TM.Timers('Timer_1', 500, LED_Timer))  
#TM.Timers('Timer_2', 1500, taskexample)  
#print(TM.Timers.timers)

loop = 475
while True:
    """
    print(f"elapsed time: {(time.ticks_ms() - start) / 1000}")    
    if p1.value():
        print("Button is released.")
    else:
        print("Button is pressed.")
    """
    print(f"downCnt: {maxtimer['downCnt']} - uptime: {sysData['uptime']} - loop: {loop} - uptime: {sysData['uptime']}")
    loop += 5
    if (maxtimer['downCnt'] == 0):
        print('maxtimer wird nicht mehr gebraucht')
        myTimers.stop(maxtimer)
        #myTimers.stop(blink)
        maxtimer = myTimers.append('maxtimer', loop)
    
    #print("active downConuters:")
    #for t in TM.Timers.timers.items():
    #    print (t)
    #print(TM.Timers.timers)
    #print("")
    time.sleep(5)
    
myTimers.stop(maxtimer)
