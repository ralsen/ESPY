import json
import sys
import settings as set

from logger import Logger
#log = Logger.getLogger(__name__, level="INFO", logfile="/log.txt")
log = Logger.getLogger(__name__)

class cfg():
    confData = dict()
    def __init__(self):
        log.info('init cfg-class')
        #self.confData = dict()
        
    def eraseConfig():
        log.info('eraseConfig()')
        for key, value in self.confData.items():
            self.confData[key] = ''
        self.saveConfig(self.confData)

    def saveConfig(self, data):
        log.info('saveConfig()')
        self.calcHash()
        with open('config.json', 'w') as f:
            log.info(f"---> writing: {data}")
            json.dump(data, f)
        with open('config.json', 'r') as cf:
            log.info(f"---> reading: {cf.read()}")

    def loadConfig(self):
        log.info('loadConfig()')
        try:
            log.info('try to read config.json ... ')
            with open('config.json', 'r') as f:
                self.confData = json.load(f)
                log.debug(self.confData)
                if(self.Hash_ok()):
                    log.info('Hash is OK')
                else:
                    log.info("Hash is not OK")
                    raise
        except Exception as err:
            log.info(f"file not found or corrupted, generating new one: ({err})")
            self.SetToDefault()
            try:
                with open('config.json', 'r') as cf:
                    self.confData = json.load(cf)
            except:
                log.info('can not find config.json')
                return False, False
            if not self.Hash_ok():
                log.info('can not generate config.json')
                return False, False
            else:  
                return False, self.confData
        return True, self.confData

    def SetToDefault(self):
        log.info('SetToDefault()')
        self.confData = set.defData
        self.confData['Architecture'] = sys.implementation._machine
        self.saveConfig(self.confData)

    def calcHash(self):
        log.info('calcHash()')
        self.confData['Size'] = hex(len(self.confData))
        self.confData.pop('Hash', '')
        sorted_string = ''.join(sorted(f"{key}{value}" for key, value in self.confData.items()))
        checksum = sum(ord(char) for char in sorted_string)
        log.info(f"calculated Hash: {hex(checksum)}")
        self.confData['Hash'] = hex(checksum)

    def Hash_ok(self):
        log.info('Hash_ok()?')
        currentHash = self.confData.pop('Hash', '')
        sorted_string = ''.join(sorted(f"{key}{value}" for key, value in self.confData.items()))
        checksum = sum(ord(char) for char in sorted_string)
        self.confData['Hash'] = currentHash
        log.info(f"calculated Hash: {hex(checksum)}, stored Hash: {currentHash}")
        return hex(checksum)==currentHash    