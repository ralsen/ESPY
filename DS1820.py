# see here for pin assignment https://randomnerdtutorials.com/esp8266-pinout-reference-gpios/

import machine, onewire, ds18x20, time
import binascii

class DS1820():
    def __init__(self):    
        pass
        ds_pin = machine.Pin(4)
        self.ds_sensor = ds18x20.DS18X20(onewire.OneWire(ds_pin))
        self.romsbyte = self.ds_sensor.scan()
        self.romstr = {}
        for rom in self.romsbyte:
            self.romstr[binascii.hexlify(rom).decode()] = rom
        self.ds = {}
        print(f"found {len(self.romstr)} x DS1820")
        print(f"Found DS1820 devices: {self.romstr}")
        
    def read(self, data):
        pass
        self.ds_sensor.convert_temp()
        time.sleep_ms(750)
        i = 0
        for rom in self.romstr.keys():
            self.ds[rom] = self.ds_sensor.read_temp(self.romstr[rom])
            data['Adress_'+str(i)] = rom
            data['Value_'+str(i)] = self.ds[rom]
            i += 1
        return self.ds
    