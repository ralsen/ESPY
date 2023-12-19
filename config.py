import json

confData = dict()

def eraseConfig():
    print("eraseConfig()")
    for key, value in confData.items():
        confData[key] = ""
    saveConfig()

def saveConfig():
    print("saveConfig()")
    with open("config.json", "w") as f:
        json.dump(confData, f)

def loadConfig():
    print("loadConfig()")
    try:
        print("try to read config.json ... ", end="")
        with open("config.json", "r") as f:
            confData = json.load(f)
        print(f"done. {confData}")
    except Exception as err:
        print(f"Datei nicht vorhanden: {err}")
        SetToDefault()
        with open("config.json", "r") as cf:
            confData = json.load(cf)
        if not testHash(confData):
            return False
    return True

def SetToDefault():
    print("SetToDefault()")
#    confData["SSID"] = "TK800"
#    confData["password"] = "Lanecharge"
    confData["SSID"] = "janzneu"
    confData["password"] = "D1AFFE1234!"
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
    saveConfig()

def calcHash(data):
    print("calcHash()")
    # Entferne den letzten Wert aus dem Dictionary, um die Prüfsumme zu berechnen
    data.pop('hash', '')
    sorted_string = ''.join(sorted(f"{key}{value}" for key, value in data.items()))
    checksum = sum(ord(char) for char in sorted_string)
    confData['hash'] = checksum
    # Setze den berechneten checksum als Wert für 'checksum' im Dictionary

def testHash(data):
    print("testHash()")
    oldHash = data.pop('hash', '')
    sorted_string = ''.join(sorted(f"{key}{value}" for key, value in data.items()))
    checksum = sum(ord(char) for char in sorted_string)
    return checksum==oldHash    
