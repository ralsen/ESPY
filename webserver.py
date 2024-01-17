import socket
from machine import Pin

import config as cfg
import settings as set

class webserv():
    s = None
    cfgData = None
    import html
    def __init__(self, data):
        print('=====> S O C K E T: ')
        self.cfgData = data
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
                print("iam here")
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
        st += set.Version + '<br><br><br>Type: ' + set.FNC_TYPE + '<br>Hardw: ' + set.DEV_TYPE
        st += '<br>Chip-ID: ' + self.cfgData['chipID']
        st += '<br>MAC-Address: ' + self.cfgData['MAC']
        st += '<br>Network:     ' + self.cfgData['SSID']
        st += '<br>Devicename:  ' + self.cfgData['hostname']
        st += '<br>AP-Name:     ' + self.cfgData['APName']
        st += '<br>cfg-Size:    ' + '1234567890'
        st += '<br>Hash:       ' + hex(self.cfgData['hash'])
        st += '<br>'
        st += 'uptime: ' + str(self.cfgData['uptime'])
        st = self.newinfoPage()
        return st
    
    def newinfoPage(self):
        st = ""
        for sub in set.PageCont:
            try:
                print(f"try with: {sub}")
                if '{cfgData}' in set.PageData[sub]:
                    st += set.PageData[sub].replace('{cfgData}', str(self.cfgData[sub]))
                if '{cfgDataHEX}' in set.PageData[sub]:
                    st += set.PageData[sub].replace('{cfgDataHEX}', hex(self.cfgData[sub]))
            except Exception as err:
                print(f"exception with: {sub} - {err}")
                st += set.PageData[sub]
        print (st)
        return st