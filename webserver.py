import socket
from machine import Pin

import config as cfg
import settings as sett

class webserv():
    s = None
    cfgData = None
    sysData = None
    import html
    def __init__(self, data, sysData):
        print('=====> S O C K E T: ')
        self.cfgData = data
        self.sysData = sysData
        webserv.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        webserv.s.bind(('', 80))
        webserv.s.listen(5)
        print(webserv.s)
        print("****************************************************************************")
        webserv.do_web(self)
    
    def do_web(self):
        print("###############################################################################")
        while True:
            try:
                print("###")
                #if gc.mem_free() < 102000:
                #  gc.collect()
                conn, addr = webserv.s.accept()
                conn.settimeout(3.0)
                print('Got a connection from %s' % str(addr))
                request = conn.recv(1024)
                conn.settimeout(None)
                request = str(request)
                print('Content = %s' % request)
                request = request[:request.find("HTTP")]
                print('Cutted: %s' % request)
                print(f"######### {request.find('/info')}")
                print(f"######### {request.find('/config')}")
                response = webserv.web_page(self)
                conn.send('HTTP/1.1 200 OK\n')
                conn.send('Content-Type: text/html\n')
                conn.send('Connection: close\n\n')
                conn.sendall(response)
                conn.close()
            except OSError as e:
                conn.close()
                print('Connection closed')

    def web_page(self):
        st = webserv.html.HomePage.replace('{title}', self.cfgData["hostname"])
        st = st.replace('{hostname}', self.cfgData['hostname'])
        st = st.replace('{mainpage}', webserv.html.InfoMenu)
        st = st.replace('{apppage}', '')
        st = st.replace('{confpage}', '')
        st = st.replace('{content}', self.infoPage())
        return st
    
    def infoPage(self):
        st = '</h3>'
        st += sett.Version + '<br><br><br>Type: ' + sett.FNC_TYPE + '<br>Hardw: ' + sett.DEV_TYPE
        st += '<br>Chip-ID: ' + self.cfgData['chipID']
        st += '<br>MAC-Address: ' + self.cfgData['mac']
        st += '<br>Network:     ' + self.cfgData['SSID']
        st += '<br>Devicename:  ' + self.cfgData['hostname']
        st += '<br>AP-Name:     ' + self.cfgData['APName']
        st += '<br>cfg-Size:    ' + '1234567890'
        st += '<br>Hash:       ' + hex(self.cfgData['hash'])
        st += '<br>'
        st += 'uptime: ' + str(self.sysData['uptime'])
        return st