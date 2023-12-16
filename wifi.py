from machine import Pin
import time

p0 = Pin(2, Pin.OUT) 

def do_connect(SSID, Passw):
    import network
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print(f'\n\r\nconnecting to network {SSID} ', end='')
        wlan.connect(SSID, Passw)
        while not wlan.isconnected():
            p0.value(not p0.value())
            print(".", end='')
            time.sleep(0.1)
    print('\r\nnetwork config:', wlan.ifconfig())
