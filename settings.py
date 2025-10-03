VERNR = "0.01"
__DATE__ = "27.02.2024"
__TIME__ = "18:15"
RELEASE = "Debug"
FNC_TYPE = 'Switch'
DEV_TYPE = "D1MINI"


DEFAULT_SSID        = "unknown"
DEFAULT_PASSWORD    = "unknown"
DEFAULT_HOSTNAME    = "No-Name"
DEFAULT_APNAME      = "ESPY_NET"
DEFAULT_PORT        = '8080'
DEFAULT_MEASCYCLE   = 150        # in sec.
DEFAULT_PAGERELOAD  = 10         # in sec.

if (FNC_TYPE) == 'DS1820':
  DEFAULT_TRANSCYCLE = 300      # transmit cycle to server in sec.
else:
  DEFAULT_TRANSCYCLE = 3600

MyName = "\r\n*************************************************************************************\r\n" \
              "*******************************     E S P N o d e      ******************************\r\n" \
              "*************************************************************************************"
Version = f"\r\n-----> V {VERNR} vom {__DATE__} {__TIME__} {RELEASE} <-----\r\n"

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

PageContent =  [
                ['', '',                      '<br><br>'],
                [ 'Version', 'cfgData',        '<br>Version: V'],
                ['Type', 'cfgData',           '<br>Type: '],
                ['Hardware', 'cfgData',       '<br>Hardw: '],
                ['Architecture', 'cfgData',   '<br>Architecture: '],
                ['chipID', 'cfgData',         '<br>chipID: '], 
                ['MAC', 'cfgData',            '<br>MAC-Address: '],
                ['SSID', 'cfgData',           '<br>Network: '],
                ['IP', 'cfgData',             '<br>Network-IP: '],
                ['name', 'cfgData',           '<br>Name: '],
                ['APName', 'cfgData',         '<br>AP-Name: '],
                ['Size', 'cfgData',           '<br>cfg-Size: '],
                ['Hash', 'cfgData',           '<br>Hash: '],
                ['', '',                      '<br><br>Display: False<br>'],
                ['uptime', 'sysData',         '<br>uptime: '],
                ['MeasuringCycle', 'cfgData', '<br>Measuring cycle: '],
                ['DS1820_rem', 'sysData',     ' (remaining: '],
                ['', '',                      ')'],
                ['TransmitCycle', 'cfgData',  '<br>Transmit cycle: '],
                ['PostTimer_rem', 'sysData',  ' (remaining: '],
                ['', '',                      ')'],
                ['', '',                      '<br><br>'],
                ['RSSI', 'sysData',           '<br>RSSI: '],
                ['delivPages', 'cfgData',     '<br>Pages delivered: ']
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
defData['Port'] = DEFAULT_PORT
defData['LED'] = True
defData['Size'] = 4711
defData['Hash'] = 815
