import json

class cfg():
    confData = dict()
    def __init__(self):
        print('init cfg-class')
        self.confData = dict()
        
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
                if(self.testHash()):
                    print('Hash OK')
                else:
                    print("Hash not ok")
                    return False
        except Exception as err:
            print(f"file not found, generating new one: ({err})")
            self.SetToDefault()
            with open('config.json', 'r') as cf:
                self.confData = json.load(cf)
            if self.testHash():
                print('can not generate config.json')
                return False
        return self.confData

    def SetToDefault(self):
        print('SetToDefault()')
        confData = dict()
        confData['SSID'] = 'TK800'
        confData['password'] = 'Lanecharge'
    #    confData['SSID'] = 'janzneu'
    #    confData['password'] = 'D1AFFE1234!'

        confData['name'] = 'MyName'
        confData['Type'] = 'DS1820-0'
        confData['hostname'] = 'MyName'
        confData['APName'] = 'ESPY_NET'
        confData['mac'] = 'xx.xx.xx.xx.xx.xx'
        confData['chipID'] = ''
        confData['localIP'] = '0.0.0.0'
        confData['fixip'] = '1.1.1.1'
        confData['server'] = 'servername'
        confData['port'] = 'number'
        confData['MeasuringCycle'] = '5'
        confData['TransmitCycle'] = '300'
        confData['PageReload'] = '10'
        confData['hash'] = '0815'
        confData['LED'] = True
        self.saveConfig(confData)

    def calcHash(self):
        print('calcHash()')
        # Entferne den letzten Wert aus dem Dictionary, um die Prüfsumme zu berechnen
        self.confData.pop('hash', '')
        sorted_string = ''.join(sorted(f"{key}{value}" for key, value in self.confData.items()))
        checksum = sum(ord(char) for char in sorted_string)
        self.confData['hash'] = checksum
        # Setze den berechneten checksum als Wert für 'checksum' im Dictionary

    def testHash(self):
        print('testHash()')
        currentHash = self.confData.pop('hash', '')
        sorted_string = ''.join(sorted(f"{key}{value}" for key, value in self.confData.items()))
        checksum = sum(ord(char) for char in sorted_string)
        self.confData['hash'] = currentHash
        return checksum==currentHash    