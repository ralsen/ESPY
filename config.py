import json

confData = dict()

def eraseConfig():
    for key, value in confData.items():
        confData[key] = ""

def saveConfig():
    with open("config.json", "w") as f:
        json.dump(confData, f)

def loadConfig():
    with open("config.json", "r") as f:
        confData = json.load(f)
    return testHash(confData)

def SetToDefault():
    confData["SSID"] = "ich bin"
    confData["password"] = "PW"
    confData["hostname"] = "MyName"
    confData["APName"] = "ESPY_NET"
    confData["MACAddress"] = "xx.xx.xx"
    confData["ChipID"] = "666"
    confData["localIP"] = "0.0.0.0"
    confData["fixip"] = "1.1.1.1"
    confData["server"] = "servername or IP???"
    confData["port"] = "number"
    confData["MeasuringCycle"] = "5"
    confData["TransmitCycle"] = "300"
    confData["PageReload"] = "10"
    confData["hash"] = "0815"
    calcHash(confData)

def calcHash(data):
    # Entferne den letzten Wert aus dem Dictionary, um die Prüfsumme zu berechnen
    data.pop('hash', '')
    sorted_string = ''.join(sorted(f"{key}{value}" for key, value in data.items()))
    checksum = sum(ord(char) for char in sorted_string)
    confData['hash'] = checksum
    # Setze den berechneten checksum als Wert für 'checksum' im Dictionary

def testHash(data):
    oldHash = data.pop('hash', '')
    sorted_string = ''.join(sorted(f"{key}{value}" for key, value in data.items()))
    checksum = sum(ord(char) for char in sorted_string)
    return checksum==oldHash    
