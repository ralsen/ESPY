# test
import socket
from machine import Pin

import config as cfg

relay = Pin(0, Pin.OUT)

class webserv():
    s = None
    def __init__(self):
        print('=====> S O C K E T: ')
        webserv.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        webserv.s.bind(('', 80))
        webserv.s.listen(5)
        print(cfg.confData)
        print(webserv.s)
        webserv.do_web(self)
    
    def do_web(self):
        while True:
            try:
                #if gc.mem_free() < 102000:
                #  gc.collect()
                conn, addr = webserv.s.accept()
                conn.settimeout(3.0)
                print('Got a connection from %s' % str(addr))
                request = conn.recv(1024)
                conn.settimeout(None)
                request = str(request)
                print('Content = %s' % request)
                relay_on = request.find('/?relay=on')
                relay_off = request.find('/?relay=off')
                print(f"######### {request.find('/info')}")
                if relay_on == 6:
                    print('RELAY ON')
                relay.value(0)
                if relay_off == 6:
                    print('RELAY OFF')
                relay.value(1)
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
        if relay.value() == 1:
            relay_state = ''
        else:
            relay_state = 'checked'
        html = """
            <html><head><meta name="viewport" content="width=device-width, initial-scale=1"><style>
            body{font-family:Arial; text-align: center; margin: 0px auto; padding-top:30px;}
            .switch{position:relative;display:inline-block;width:120px;height:68px}.switch input{display:none}
            .slider{position:absolute;top:0;left:0;right:0;bottom:0;background-color:#ccc;border-radius:34px}
            .slider:before{position:absolute;content:"";height:52px;width:52px;left:8px;bottom:8px;background-color:#fff;-webkit-transition:.4s;transition:.4s;border-radius:68px}
            input:checked+.slider{background-color:#2196F3}
            input:checked+.slider:before{-webkit-transform:translateX(52px);-ms-transform:translateX(52px);transform:translateX(52px)}
            </style><script>function toggleCheckbox(element) { var xhr = new XMLHttpRequest(); if(element.checked){ xhr.open("GET", "/?relay=on", true); }
            else { xhr.open("GET", "/?relay=off", true); } xhr.send(); }
            </script></head><body>
            <h1>ESP Relay Web Server</h1><label class="switch"><input type="checkbox" onchange="toggleCheckbox(this)" %s><span class="slider">
            </span></label></body></html>""" % (relay_state)

        HomePage = """
<!DOCTYPE html><html lang="de"><head><meta charset="utf-8"><TITLE> {title} </TITLE><meta name="viewport" content="width=device-width, initial-scale=0.5">
<style>body{font-family: Verdana, sans-serif;font-size: 87.5%;background-color: #e8e8e8;color: black;padding: 0;margin:0;}
div1 {width: 100%;color: black;padding: 10px;position: absolute;top: 60px;left: 150px;}
.vertical-menu a {background-color: #b9d8e9;color: black;display: block;padding: 12px;text-decoration: none;
.vertical-menu {width: 100px;background-color: #e8e8e8;
.vertical-menu a:hover {background-color: #4CAFf0;
.vertical-menu a.active {background-color: #4CAFf0;color: white;
</style></head><body>
<h1>{hostname}</h1>
<div1>{content}</div1>
<div class="vertical-menu">
<a href="info">Info</a><br>
{appmenu}
{mainpage}
{confpage}
</div>
</body>
</html>}"""

        AppMenu = """
<a href="status">Status</a><br>{appmenu}"""

        StatMenu = """
<a href="on">Ein</a><br><a href="off">Aus</a><br>"""

        InfoMenu = """
<a href="config">Config</a><br>
<a href="showlog">show log</a>
<a href="showdir">show Dir</a>"""

        ConfMenu = """
<a href="meascyc">MeasCyc</a><a href="transcyc">TransCyc</a><a href="pagereload">Pagereload</a><a href="server">Server</a>
<a href="port">Port</a>
<a href="hostname">Name</a>
<a href="led">LED</a>
<a href="default">set defaults</a>
<a href="reset">Reset</a></p>
<form method='POST' action='/update' enctype='multipart/form-data'><input type='file' name='update'><input type='submit' value='Update'></form>"""

        ConfMenu2= """
<a href="transcyc">TransCyc</a>
<a href="pagereload">Pagereload</a>
<a href="server">Server</a>
<a href="port">Portnummer</a>
<a href="hostname">Name</a>
<a href="led">LED</a>
<a href="default">set defaults</a>
<a href="reset">Reset</a></p>
<form method='POST' action='/update' enctype='multipart/form-data'><input type='file' name='update'><input type='submit' value='Update'></form>"""


        RadioButton = """
<form>
<p>mit welchem Netzwerk soll eine Verbindung hergestellt werden?</p>"""


        RadioStart = """"
<input type="radio" name="SSID" value="{SSID}">  {CRYPT}{SSID}   ->   (Signal: {RSSI})"""

        RadioEnd = """
<br><br>
<input type="password" name="pass"> </label>
<input type="submit" value="senden">
</form>"""

        RadioLED_s = """
<form>
<p> soll die LED ein- oder ausgeschaltet sein?</p>
<input type="radio" name="Led" value="On" {ontext}>  On
<input type="radio" name="Led" value="Off" {offtext}>  Off"""

        RadioLED_e = """
<br><br>
<input type="submit" value="senden">
</form>"""

        Name = """
<form>
<p> {nametext}</p>
<input type="text" name="{urltext}"> </label>
<input type="submit" value="senden">
</form>"""
        
        tesstr = """
dies ist ein %s Teststring.
noch einer.""" %("toller")

        print(tesstr)
        return HomePage.replace("{title}", cfg.confData["hostname"])
