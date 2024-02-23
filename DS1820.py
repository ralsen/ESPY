# see here for pin assignment https://randomnerdtutorials.com/esp8266-pinout-reference-gpios/

import machine, onewire, ds18x20, time
import binascii

ds_pin = machine.Pin(4)
ds_sensor = ds18x20.DS18X20(onewire.OneWire(ds_pin))

roms = ds_sensor.scan()
print('Found DS devices: ', roms)

def getDS1820():
    ds = {}    
    ds_sensor.convert_temp()
    time.sleep_ms(750)
    for rom in roms:
        dsadr = binascii.hexlify(rom).decode()
        ds[dsadr] = ds_sensor.read_temp(rom)
        print(dsadr)
        print(ds_sensor.read_temp(rom))
    return ds
