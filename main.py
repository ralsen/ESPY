from machine import Pin, PWM
import machine
import time
import os
import binascii
import json

import wifi as WF
import webserver as ws
import settings as set
import timers as TM
import config as cfg
import util as ut

from logger import Logger
log = Logger.getLogger(__name__, level="INFO", logfile="/log.txt")

p0 = Pin('LED', Pin.OUT) 
p1 = Pin(0, Pin.IN)

start = time.ticks_ms()

log.info(set.MyName)
log.info(set.Version)

log.info("Key service started!")            
log.info("10ms Timer service started!")
log.info("1s timer services started!")

sysData = {}

cf = cfg.cfg()

# ############################# Timer handlers ############################## 
def LED_Timer(timer):
    #print(f"task-ID: {blink['id']} - {blink['name']} executed")
    p0.value(not p0.value())

def handlePost(timer):
    PostTimer['start'] = time.ticks_ms() + cfgData['TransmitCycle'] * 1000
    log.info(f"task-ID: {PostTimer['id']} - {PostTimer['name']} executed")
    if ut.post(wifi, cfgData, sysData):
        sysData['goodTrans'] += 1
    else:
        sysData['badTrans'] += 1
        
def handleUptimer(timer):
    sysData['uptime'] += 1
   
def handleMain(timer):
    global maxtimer

    # GPIO 15 als PWM
    pwm = PWM(Pin(15))

    # Frequenz setzen (z.B. 1 kHz)
    pwm.freq(1000)

    # Duty Cycle setzen (0 - 65535)
    for duty in range(0, 128, 4):
        pwm.duty_u16(duty)
        #print(f"Duty Cycle: {duty}")
        time.sleep(0.05)
        
    log.info(f"elapsed time: {(time.ticks_ms() - start) / 1000}")    
    if p1.value():
        log.info("Button is released.")
    else:
        log.info("Button is pressed.")
    
    #print(f"---> TransmitRemain: {sysData['PostTimer_rem']} - MeasuringRemain: {sysData['DS1820_rem']}")
    #log.info(f"downCnt: {maxtimer['downCnt']} - uptime: {sysData['uptime']}") # - loop: {sysData['loop']}")
    #sysData['loop'] += 5
    #if (maxtimer['downCnt'] == 0):
    #    log.info('maxtimer wird nicht mehr gebraucht')
    #    myTimers.stop(maxtimer)
        #myTimers.stop(blink)
        #maxtimer = myTimers.append('maxtimer', sysData['loop'])
    #print("active downConuters:")
    #for t in TM.Timers.timers.items():
    #    print (t)
    #print(TM.Timers.timers)
    #print("")
    #time.sleep(5)
    
# ############################## Timer handlers ##############################

loaded_cfgData = cf.loadConfig()
if loaded_cfgData[1] == False:
    log.info("!!! P A N I K !!! could not load configuration")
    panik =  myTimers.append("Panik", 25, LED_Timer)
    while True:
        pass

cfgData = loaded_cfgData[1]
log.debug(f"-----> {cfgData}")
 
log.info("-----> initialize system data and variables")   
sysData['uptime'] = 0
sysData['badTrans'] = 0
sysData['goodTrans'] = 0
sysData['RSSI'] = 0
sysData['myTimers'] = TM.Timers()
sysData['wifi'] = WF.wifi(cfgData, sysData) 
myTimers = sysData['myTimers']
myWifi = sysData['wifi']

"""
if set.FNC_TYPE == 'DS1820':
    import DS1820 as DS
    myDS1820 = DS.DS1820()
    temps = myDS1820.read(sysData)

    def handleDS1820(timer):
        print(f"task-ID: {DSTimer['id']} - {DSTimer['name']} executed")
        DSTimer['start'] = time.ticks_ms() + cfgData['MeasuringCycle'] * 1000
        temps = myDS1820.read(sysData)
        print(temps)

    #DSTimer = myTimers.append('DS1820', cfgData['MeasuringCycle'] * 1000, handleDS1820)
"""

log.info("-----> connect to wifi")
wifi = myWifi.do_connect(cfgData["SSID"], cfgData["password"])
if (wifi == None):
    log.info("OJE!!!")
else:
    log.info("connected to wifi")
    sysData['RSSI'] = wifi.status('rssi')
    log.info(f"RSSI: {sysData['RSSI']} dBm")
    log.info(f"\r\n{wifi.ifconfig()}")


cfgData["IP"] = wifi.ifconfig()[0]
cfgData["Server"] = wifi.ifconfig()[2]
cfgData["MAC"] = binascii.hexlify(wifi.config('mac')).decode()
#cfgData['hostname'] = cfgData['name'] + '_' + cfgData['MAC'].replace(':', '_') # this is the better line
cfgData['name'] = cfgData['hostname'] + '_' + cfgData['MAC'].replace(':', '_') #for compatibility use this
cfgData["chipID"] = binascii.hexlify(machine.unique_id()).decode()
cf.saveConfig(cfgData)

log.info(f"\r\n---> Hello from device: {cfgData['hostname']} <---" )
log.info(f"Architecture:      {cfgData['Architecture']}")
log.info(f"DEV_TYPE:          {cfgData['Hardware']}")
log.info(f"FNC_TYPE:          {cfgData['Type']} ")
log.info(f"MAC-Adress:        {cfgData['MAC']}")
log.info(f"Network:           {cfgData['SSID']}")
log.info(f"IP-Adress:         {cfgData['IP']}")
log.debug(f"running with configuration:\r\n{cfgData}")
log.info("everything is initialized, let's go ahead now ->\r\n")

log.info("---> Directory:")
log.info(os.listdir('/'))
log.info(" <--- Directory\r\n")

    
blink = myTimers.append("Blinker", 500, LED_Timer)
#maxtimer = myTimers.append('maxtimer', 1000)
utimer = myTimers.append('Uptimer', 1000, handleUptimer)
#PostTimer = myTimers.append("PostTimer", cfgData['TransmitCycle'] * 1000, handlePost)
#print(blink)

log.debug("---> Timers: #############################")
log.debug(myTimers.timers)

"""
Remainers = [
              PostTimer
              #DSTimer
           ]

def handleRemainers(timer):
    for val in Remainers:
        print(f"handleRemainers for {val['name']}: {myTimers.remain(val)}")
        sysData[val['name']+'_rem'] = myTimers.remain(val)
        
for val in Remainers:
    sysData[val['name']+'_rem'] = 0
    print(f"Remain for {val['name']}: {sysData[val['name']+'_rem']}")
#remainers = myTimers.append('RemainTimer', 1000, handleRemainers)
"""
        
    #myTimers.stop(maxtimer)
    
#MainTimer = myTimers.append("MainTimer", 500, handleMain)
web = ws.webserv(cfgData, sysData)
webTimer = myTimers.append("WebTimer", 100, web.do_web())

log.info("!!!let's wait 5 seconds !!")
time.sleep(5)

#print(TM.Timers('Timer_1', 500, LED_Timer))  
#TM.Timers('Timer_2', 1500, taskexample)  
#print(TM.Timers.timers)

sysData['loop'] = 475
log.info("starting main loop - press CTRL+C to abort")
try:
    while True:
        log.info("main loop")
        log.info(f"uptime: {sysData['uptime']}")
        time.sleep(1)
except KeyboardInterrupt:
    log.info("CTRL+C pressed – terminate Threads…")
    myTimers.stopall()
    with open('config.json', 'r') as f:
        log.info(f"this is the last configuration -> {f.read()}")
    log.info("bye, bye")