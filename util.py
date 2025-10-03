import settings as set
import urequests

def ServerInfo(contend, data1, data2):
    st = {}
    for element in contend:
        print(f"Element: {element}")
        try:
            if element in data1:
                st[element] = str(data1[element])
            elif element in data2:
                st[element] = str(data2[element])
            else:
                raise Exception(f"Element '{element}' not found in both data1 and data2")
        except Exception as err:
            print(f"Exception with: {element} - {err}")
            return False
    return st

def post(wifi, cfgData, sysData):
    sysData['RSSI'] = wifi.status('rssi')
    print(f"cfgData: {cfgData} ###---### sysData: {sysData}")
    srvData = ServerInfo(set.ServerContent, cfgData, sysData)
    if srvData == False:
        print("no data available !!!")
        return False
    try:
        print(f"sending to http://192.168.2.87:8080:\r\n{srvData}")
        response = urequests.post('http://192.168.2.87:8080', json=srvData)
        print(response.content)
        return response
    except:
        sysData['badTrans'] += 1
        print('habe niemanden erreicht')
        return False
    