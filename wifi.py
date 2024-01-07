from machine import Pin
import time
import network
import socket

import timers as TM

LED_Pin = Pin(2, Pin.OUT) 

myTimers = TM.Timers()

def connectBlink(timer):
    LED_Pin.value(not LED_Pin.value())

def do_connect(SSID, Passw):
    blink = myTimers.append("WLAN-Blinker", 100, connectBlink)
    #blink.start()
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print(f'\n\rconnecting to network {SSID} - {Passw}', end='')
        myTimers.append('WLAN', 3000, 'downtimer')
        ##TM.downTimers.downCnter["WLAN"] = 3000
        wlan.connect(SSID, Passw)
        while not wlan.isconnected():
            print(".", end='')
            time.sleep(0.1)
            if(myTimers.timers['WLAN'] == 0): ## TM.downTimers.downCnter["WLAN"] == 0):
                print(" ")
                #blink.stop()
                return None
    print(" ")
    print(blink)
    myTimers.stop(blink)
    return(wlan)