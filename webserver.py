import socket
import _thread
import time
import gc
import html     # dein HTML-Modul oder Dummy

import settings as set
from logger import Logger
#log = Logger.getLogger(__name__, level="INFO", logfile="/log.txt")
log = Logger.getLogger(__name__)

class webserv:
    s = None
    import html
    def __init__(self, cfgData, sysData):
        self.cfgData = cfgData
        self.sysData = sysData
        self.running = False

    def start(self):
        if self.running:
            log.info("Webserver already running.")
            return
        self.running = True
        log.info("Starting web server thread ...")
        _thread.start_new_thread(self.do_web, ())

    def stop(self):
        log.info("Stopping web server ...")
        self.running = False
        if webserv.s:
            try:
                webserv.s.close()
                log.info("Socket closed.")
            except Exception as e:
                log.info(f"error during closing Sockets: {e}")
        log.info("Webserver stopped.")

    def do_web(self):
        try:
            webserv.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            webserv.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            webserv.s.bind(('', 80))
            webserv.s.listen(5)
            log.info("Webserver started, listening on Port 80.")
        except Exception as e:
            log.info(f"error during starting socket: {e}")
            self.running = False
            return

        while self.running:
            try:
                if gc.mem_free() < 102000:
                    gc.collect()

                conn, addr = webserv.s.accept()
                log.info(f"connection from {addr}")

                conn.settimeout(3.0)
                request = conn.recv(1024)
                conn.settimeout(None)

                if not request:
                    log.info("Empty request – connection closed.")
                    conn.close()
                    continue

                request = request.decode('utf-8')
                log.info(f"Content = {request}")

                request_line = request.split('\r\n')[0]
                path = request_line.split(' ')[1] if ' ' in request_line else '/'

                log.info(f"Path requested: {path}")
                # Routing
                if path == '/info':
                    response = self.web_info()
                elif path == '/config':
                    response = self.web_config()
                else:
                    response = self.web_page()
                log.info(f"Seite generiert. {response}")
                # Antwort senden
                conn.send('HTTP/1.1 200 OK\r\n')
                conn.send('Content-Type: text/html\r\n')
                conn.send('Connection: close\r\n\r\n')
                conn.sendall(response)

            except OSError as e:
                log.info(f"OSError: {e}")
            except Exception as e:
                log.info(f"general error: {e}")
            finally:
                try:
                    conn.close()
                except Exception:
                    pass

        # Nach Verlassen der Schleife:
        try:
            webserv.s.close()
        except Exception:
            pass
        log.info("Webserver loop finished.")

    # Example pages:
    def web_page(self):
        st = html.HomePage
        st = st.replace('{title}', self.cfgData["hostname"])
        st = st.replace('{hostname}', self.cfgData['hostname'])
        st = st.replace('{mainpage}', html.InfoMenu)
        st = st.replace('{apppage}', '')
        st = st.replace('{confpage}', '')
        st = st.replace('{content}', self.web_info())
        return st

    def web_info(self):
        st = '<h3>'
        st += set.Version
        st += '</h3>'
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

    def web_config(self):
        return f"""<html><body><h1>Konfiguration</h1><p>{self.cfgData}</p></body></html>"""

