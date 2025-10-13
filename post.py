import _thread
import urequests

import settings as set
from logger import Logger
#log = Logger.getLogger(__name__, level="INFO", logfile="/log.txt")
log = Logger.getLogger(__name__)

class Post:
    s = None
    def __init__(self, cfgData, sysData):
        self.cfgData = cfgData
        self.sysData = sysData
        self.running = False
        
    def start(self):
        if self.running:
            log.info("Post already running.")
            return
        self.running = True
        log.info("Starting post thread ...")
        #_thread.start_new_thread(self.do_post, ())

    def stop(self):
        log.info("Stopping post ...")

    def ServerInfo(self, contend, data1, data2):
        st = {}
        return data1
        for element in contend:
            try:
                if element in data1:
                    st[element] = str(data1[element])
                elif element in data2:
                    st[element] = str(data2[element])
                else:
                    raise Exception(f"Element '{element}' not found in both data1 and data2")
            except Exception as err:
                log.info(f"Exception with: {element} - {err}")
                return False
        return st

    def do_post(self):
        #self.sysData['RSSI'] = self.wifi.status('rssi')
        log.info(f"cfgData: {self.cfgData} ###---### sysData: {self.sysData}")
        srvData = self.ServerInfo(set.ServerContent, self.cfgData, self.sysData)
        if srvData == False:
            log.info("no data available !!!")
            return False
        try:
            log.info(f"sending to http://192.168.2.87:8080:\r\n{srvData}")
            response = urequests.post('http://192.168.2.87:8080', json=srvData)
            log.info(response.content)
            return response
        except Exception as err:
            self.sysData['badTrans'] += 1
            log.info(f'habe niemanden erreicht: {err}')
            return False