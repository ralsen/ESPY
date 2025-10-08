from machine import Pin
import time
import network
import socket

import timers as TM

LED_Pin = Pin(2, Pin.OUT) 
class wifi():
    def __init__(self, cfgData, sysData):
        print("wifi class initialized.")
        self.cfgData = cfgData
        self.sysData = sysData

    def connectBlink(self, blink):
        LED_Pin.value(not LED_Pin.value())

    def do_connect(self, SSID, Passw):
        myTimers = self.sysData['myTimers']
        blink = myTimers.append("WLAN", 100, self.connectBlink)
        print(blink)
        #maxtimer = myTimers.append('maxtimer', 3000, 'downtimer')
        #print(maxtimer)
        wlan = network.WLAN(network.STA_IF)
        time.sleep(3)
        wlan.active(True)
        if not wlan.isconnected():
            print(f'\n\rconnecting to network {SSID} - {Passw}', end='')
            wlan.connect(SSID, Passw)
            while not wlan.isconnected():
                print(".", end='')
                time.sleep(0.1)
                if(myTimers.timers['WLAN'] == 0):
                    print(" ")
                    #myTimers.stop(maxtimer)
                    return None
        print(" ")
        myTimers.stop(blink)
        return(wlan)