VERNR = "0.0"
__DATE__ = "24.02.2024"
__TIME__ = "16:58"
RELEASE = "Debug"
FNC_TYPE = "DS1820"
DEV_TYPE = "D1MINI"


DEFAULT_SSID       = "unknown"
DEFAULT_PASSWORD   = "unknown"
DEFAULT_HOSTNAME   = "No-Name"
DEFAULT_APNAME     = "ESPY_NET"
DEFAULT_MEASCYCLE  = 150        # in sec.
DEFAULT_PAGERELOAD = 10         # in sec.

if (FNC_TYPE) == 'DS1820':
  DEFAULT_TRANSCYCLE = 300      # transmit cycle to server in sec.
else:
  DEFAULT_TRANSCYCLE = 3600

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
PageData['Hash'] = "<br>Hash: {cfgDataHEX}"
PageData['divider'] = "<br><br><br>"
PageData['uptime'] = "<br>uptime: {cfgData}"
PageData['delivPages'] = "<br>Pages delivered: {cfgData}"

ServerContent = [
                'hostname',
                'IP',
                'name',
                'SSID',
                'RSSI',
                'Hardware',
                'uptime',
                'Version',
                'APName',
                'MAC',
                'TransmitCycle',
                'MeasuringCycle',
                'Hash',
                'Size',
                'PageReload',
                'Server',
                'Port',
                'uptime',
                'delivPages',
                'goodTrans',
                'badTrans',
                'LED',
                'Type',
                'Adress_0',
                'Value_0',
                'Adress_1',
                'Value_1',
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
defData['name'] = ''                    # this is the full name "Devicename+MAC"
defData['hostname'] = DEFAULT_HOSTNAME  # this is the Devicename only, given by user
defData['IP'] = ''
defData['Type'] = 'DS1820'
defData['Version'] = VERNR
defData['Hardware'] = DEV_TYPE
defData['Architecture'] = ''
defData['APName'] = 'ESPY_NET'
defData['MAC'] = ''
defData['chipID'] = ''
defData['TransmitCycle'] = DEFAULT_TRANSCYCLE
defData['MeasuringCycle'] = DEFAULT_MEASCYCLE
defData['PageReload'] = DEFAULT_PAGERELOAD
defData['delivPages'] = 0
defData['fixip'] = '1.1.1.1'
defData['Server'] = 'servername'
defData['Port'] = 'number'
defData['LED'] = True
defData['Size'] = 4711
defData['Hash'] = 815
