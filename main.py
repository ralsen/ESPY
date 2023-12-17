from machine import Pin
import time
import timers as TM

p0 = Pin(2, Pin.OUT) 
import time
import os
import json
import wifi as wf

VERNR = "0.0"
__DATE__ = "15.12.2023"
__TIME__ = "14:01"
RELEASE = "Debug"

MyName = "\r\n*************************************************************************************\r\n" \
              "*******************************     E S P N o d e      ******************************\r\n" \
              "*************************************************************************************"
Version = f"\r\n-----> V {VERNR} vom {__DATE__} {__TIME__} {RELEASE} <-----\r\n"

start = time.ticks_ms()

print(MyName)
print(Version)

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
data["hostname"] = "ich bins"
data["server"] = "servername or IP"
data["service"] = "service number"
data["MeasuringCycle"] = "5"
data ["TransmitCycle"] = "300"
data["PageReload"] = "10"
data["APtimeout"] = "60"
data["hash-hash"] = ""

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

cnt = 50
while True:
    print(f"elapsed time: {(time.ticks_ms() - start) / 1000}")    
    p0.value(not p0.value())
    time.sleep(0.25)
