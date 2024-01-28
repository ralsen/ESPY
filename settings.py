VERNR = "0.0"
__DATE__ = "12.01.2024"
__TIME__ = "15:50s"
RELEASE = "Debug"
FNC_TYPE = "DS1820"
DEV_TYPE = "D1MINI"

MyName = "\r\n*************************************************************************************\r\n" \
              "*******************************     E S P N o d e      ******************************\r\n" \
              "*************************************************************************************"
Version = f"\r\n-----> V {VERNR} vom {__DATE__} {__TIME__} {RELEASE} <-----\r\n"

PageData =  {}
PageData['Version'] = f"</h3>{Version}<br><br><br>Type: {FNC_TYPE}<br>Hardw: {DEV_TYPE}"
PageData['Hardware'] = f"<br>Hardw: {DEV_TYPE}"
PageData['MAC'] = "<br>MAC-Address: {cfgData}"
PageData['Network'] = "<br>Network: {cfgData}"
PageData['IP'] = "<br>Network-IP: {cfgData}"
PageData['TransmitCycle'] = "<br>Transmit Cycle: {cfgData}"
PageData['chipID'] = "<br>Chip-ID: {cfgData}"
PageData['Architecture'] = "<br>Architecture: {cfgData}"
PageData['name'] = "<br>Devicename: {cfgData}"
PageData['APName'] = "<br>AP-Name: {cfgData}"
PageData['hash'] = "<br>Hash: {cfgDataHEX}"
PageData['divider'] = "<br><br><br>"
PageData['uptime'] = "<br>uptime: {cfgData}"
PageData['delivPages'] = "<br>Pages delivered: {cfgData}"

ServerCont = [
            'hostname',
            'IP',
            'name',
            'SSID',
            'Hardware',
            'uptime',
            'Architecture'
            ]

PageCont =  [
            'Version',
            'chipID',
            'MAC',
            'Architecture',
            'Network',
            'IP',
            'name',
            'APName',
            'hash',
            'divider',
            'TransmitCycle',
            'uptime',
            'delivPages'
            ]

defData = {}
#    defData['SSID'] = 'TK800'
#    defData['password'] = 'Lanecharge'
defData['SSID'] = 'janzneu'
defData['password'] = 'D1AFFE1234!'
defData['name'] = 'MyName'
defData['IP'] = ''
defData['Type'] = 'DS1820-0'
defData['Version'] = VERNR
defData['Hardware'] = DEV_TYPE
defData['Architecture'] = ''
defData['Network'] = 'WiFi.SSID'
defData['APName'] = 'ESPY_NET'
defData['MAC'] = 'xx.xx.xx.xx.xx.xx'
defData['TransmitCycle'] = '300'
defData['MeasuringCycle'] = '5'
defData['PageReload'] = '10'
defData['hostname'] = 'MyName'
defData['fixip'] = '1.1.1.1'
defData['Server'] = 'servername'
defData['Port'] = 'number'
defData['LED'] = True
defData['hash'] = '0815'
