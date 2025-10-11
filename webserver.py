import socket
from machine import Pin

import config as cfg
import settings as set

from logger import Logger
#log = Logger.getLogger(__name__, level="DEBUG", logfile="/log.txt")
log = Logger.getLogger(__name__)
class webserv():
    s = None
    cfgData = None
    import html
    def __init__(self, cfgData, sysData):
        log.info('=====> S O C K E T: ')
        self.cfgData = cfgData
        self.sysData = sysData
        webserv.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        webserv.s.bind(('', 80))
        webserv.s.listen(5)
        log.info(webserv.s)
        log.info("****************************************************************************")
        #webserv.do_web(self)
    
    def do_web(self):
        log.info("###############################################################################")
        while True:
            try:
                log.info("###")
                #if gc.mem_free() < 102000:
                #  gc.collect()
                conn, addr = webserv.s.accept()
                log.info("iam here")
                conn.settimeout(3.0)
                log.info(f'Got a connection from {str(addr)}')
                conn.settimeout(None)
                request = conn.recv(1024)
                request = request.decode('utf-8')
                request = request[:request.find("HTTP")]
                request = str(request)
                log.info(f'Content = {request}')
                log.info(f'cutted: {request}')
                log.info(f"######### {request.find('/info')}")
                log.info(f"######### {request.find('/config')}")
                response = webserv.web_page(self)
                conn.send('HTTP/1.1 200 OK\n')
                conn.send('Content-Type: text/html\n')
                conn.send('Connection: close\n\n')
                conn.sendall(response)
                conn.close()
            except OSError as e:
                conn.close()
                log.info('Connection closed')

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
        st += set.Version
        """
        for key in set.PageContent:
            st += key[2]
            if key[0] == '':
                continue
            if key[1] == 'cfgData':
                data = str(self.cfgData[key[0]])
            elif key[1] == 'sysData':
                data = str(self.sysData[key[0]])
            else:   
                data = f"no data found in {key[1]} key: {key[0]}"
            st += data
        """
        return st    
