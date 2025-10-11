import settings as set
import urequests

from logger import Logger
log = Logger.getLogger(__name__, level="DEBUG", logfile="/log.txt")

def ServerInfo(contend, data1, data2):
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

def post(wifi, cfgData, sysData):
    sysData['RSSI'] = wifi.status('rssi')
    log.info(f"cfgData: {cfgData} ###---### sysData: {sysData}")
    srvData = ServerInfo(set.ServerContent, cfgData, sysData)
    if srvData == False:
        log.info("no data available !!!")
        return False
    try:
        log.info(f"sending to http://192.168.2.87:8080:\r\n{srvData}")
        response = urequests.post('http://192.168.2.87:8080', json=srvData)
        log.info(response.content)
        return response
    except Exception as err:
        sysData['badTrans'] += 1
        log.info(f'habe niemanden erreicht: {err}')
        return False
    