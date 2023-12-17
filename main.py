from machine import Pin
import time

import time
import os
import json

import wifi as wf
import settings as set
import timers as TM

p0 = Pin(2, Pin.OUT) 

start = time.ticks_ms()

print(set.MyName)
print(set.Version)

print("Key service started!")            
print("10ms Timer service started!")
print("Hash FAILED !!!")
print( "Hello from device: " )
print("DEV_TYPE")
print("Function:          ")
print("MAC-Adress:        " )
print("1s timer services started!")
print("\r\neverything is initialized, let's go ahead now ->\r\n")

os.umount('/')
os.VfsLfs2.mkfs(bdev)
os.mount(bdev, '/')

data = dict()
data["SSID"] = "ich bins"
data["password"] = "PW"
data["hostname"] = "MyName"
data["APName"] = "ESPY_NET"
data["MACAddress"] = "xx.xx.xx"
data["ChipID"] = "666"
data["localIP"] = "0.0.0.0"
data["fixip"] = "1.1.1.1"
data["server"] = "servername or IP???"
data["port"] = "number"
data["MeasuringCycle"] = "5"
data["TransmitCycle"] = "300"
data["PageReload"] = "10"
data["hash"] = "0815"

with open("myfile.txt", "w") as f:
    json.dump(data, f)
    #f.write(str(data))

with open("myfile.txt", "r") as f:
    edata = json.load(f)

print(edata)
print(edata["hostname"])
  
#do_connect("TK800", "Lanecharge")
wf.do_connect("janzneu", "D1AFFE1234!")


def task1(timer):
    print(f"task {timer1.timer_id} - {timer1.name} executed")
def task2(timer):
    print(f"task {timer2.timer_id} - {timer2.name} executed")
def task3(timer):
    print(f"task {timer3.timer_id} - {timer3.name} executed")

timer1 = TM.TI("blink schnell", 1000, task1)
timer2 = TM.TI("blink mittel", 2000, task2)
timer3 = TM.TI("blink langsam", 3000, task3)
   
timer1.start()
timer2.start()
timer3.start()

while True:
    print(f"elapsed time: {(time.ticks_ms() - start) / 1000}")    
    p0.value(not p0.value())
    time.sleep(0.25)
