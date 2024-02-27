from machine import Pin
import machine
import time
import time
import os
import binascii

import wifi as wf
import webserver as ws
import settings as set
import timers as TM
import config as cfg
import util as ut

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

# ############################# Timer handlers ############################## 
def LED_Timer(timer):
    #print(f"task-ID: {blink['id']} - {blink['name']} executed")
    p0.value(not p0.value())

def handlePost(timer):
    print(f"task-ID: {PostTimer['id']} - {PostTimer['name']} executed")
    if ut.post(wifi, cfgData, sysData):
        sysData['goodTrans'] += 1
    else:
        sysData['badTrans'] += 1
        
def handleUptimer(timer):
    sysData['uptime'] += 1

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
utimer = myTimers.append('Uptimer', 1000, handleUptimer)

if set.FNC_TYPE == 'DS1820':
    import DS1820 as DS
    myDS1820 = DS.DS1820()
    temps = myDS1820.read(sysData)

    def handleDS1820(timer):
        temps = myDS1820.read(sysData)
        print(temps)

    DSTimer = myTimers.append('DS1820', cfgData['MeasuringCycle'] * 1000, handleDS1820)


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

# first post and then cyclic posting
if ut.post(wifi, cfgData, sysData):
    sysData['goodTrans'] += 1
else:
    sysData['badTrans'] += 1
PostTimer = myTimers.append("Timer_Example", cfgData['TransmitCycle'] * 1000, handlePost)

ws.webserv(cfgData, sysData)
ws.webserv.do_web()
  
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
