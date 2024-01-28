import json
import sys
import settings as set

class cfg():
    confData = dict()
    def __init__(self):
        print('init cfg-class')
        #self.confData = dict()
        
    def eraseConfig():
        print('eraseConfig()')
        for key, value in self.confData.items():
            self.confData[key] = ''
        self.saveConfig(self.confData)

    def saveConfig(self, data):
        print('saveConfig()')
        self.calcHash()
        with open('config.json', 'w') as f:
            json.dump(data, f)

    def loadConfig(self):
        print('loadConfig()')
        try:
            print('try to read config.json ... ')
            with open('config.json', 'r') as f:
                self.confData = json.load(f)
                print(self.confData)
                if(self.Hash_ok()):
                    print('Hash OK')
                else:
                    print("Hash not ok")
                    raise
        except Exception as err:
            print(f"file not found or corrupted, generating new one: ({err})")
            self.SetToDefault()
            try:
                with open('config.json', 'r') as cf:
                    self.confData = json.load(cf)
            except:
                print('can not find config.json')
                return False, False
            if not self.Hash_ok():
                print('can not generate config.json')
                return False, False
            else:  
                return False, self.confData
        return True, self.confData

    def SetToDefault(self):
        print('SetToDefault()')
        self.confData = set.defData
        self.confData['Architecture'] = sys.implementation._machine
        self.saveConfig(self.confData)

    def calcHash(self):
        print('calcHash()')
        # Entferne den letzten Wert aus dem Dictionary, um die Prüfsumme zu berechnen
        self.confData.pop('hash', '')
        sorted_string = ''.join(sorted(f"{key}{value}" for key, value in self.confData.items()))
        checksum = sum(ord(char) for char in sorted_string)
        # Setze den berechneten checksum als Wert für 'checksum' im Dictionary
        self.confData['hash'] = checksum

    def Hash_ok(self):
        temp = ''
        print('Hash_ok()')
        currentHash = self.confData.pop('hash', '')
        sorted_string = ''.join(sorted(f"{key}{value}" for key, value in self.confData.items()))
        checksum = sum(ord(char) for char in sorted_string)
        self.confData['hash'] = currentHash
        return checksum==currentHash    