HomePage = f'''
<!DOCTYPE html>
<html lang="de">
<head>
<meta charset="utf-8">
<TITLE>{{title}}</TITLE>
<meta name="viewport" content="width=device-width, initial-scale=0.5">
<style>
body {{
    font-family: Verdana, sans-serif;
    font-size: 87.5%;
    background-color: #e8e8e8;
    color: black;
    padding: 0;
    margin:0;
}}

.div1 {{
    width: 100%;
    color: black;
    padding: 10px;
    position: absolute;
    top: 60px;
    left: 150px;
}}

.vertical-menu a {{
    background-color: #b9d8e9;
    color: black;
    display: block;
    padding: 12px;
    text-decoration: none;
}}

.vertical-menu {{
    width: 100px;
    background-color: #e8e8e8; /* menuefarbe ??? */
}}

.vertical-menu a:hover {{
    background-color: #4CAFf0;
}}

.vertical-menu a.active {{
    background-color: #4CAFf0;
    color: white;
}}

</style>
</head>
<body>

<h1>{{hostname}}</h1>
<div class="div1">{{content}}</div>
<div class="vertical-menu">
<a href="info">Info</a><br>
{{apppage}}
{{mainpage}}
{{confpage}}
</div>
</body>
</html>
'''
AppMenu = f'''
<a href="status">Status</a><br>
{{appmenu}}
'''

StatMenu = f'''
<a href="on">Ein</a><br>
<a href="off">Aus</a><br>
'''

InfoMenu = f'''
<a href="config">Config</a><br>
<a href="showlog">show log</a>
<a href="showdir">show Dir</a>
'''

ConfMenu = f'''
<a href="meascyc">MeasCyc</a>
<a href="transcyc">TransCyc</a>
<a href="pagereload">Pagereload</a>
<a href="server">Server</a>
<a href="port">Port</a>
<a href="hostname">Name</a>
<a href="led">LED</a>
<a href="default">set defaults</a>
<a href="reset">Reset</a></p>
<form method='POST' action='/update' enctype='multipart/form-data'><input type='file' name='update'><input type='submit' value='Update'></form>
'''

ConfMenu2= f'''
<a href="transcyc">TransCyc</a>
<a href="pagereload">Pagereload</a>
<a href="server">Server</a>
<a href="port">Portnummer</a>
<a href="hostname">Name</a>
<a href="led">LED</a>
<a href="default">set defaults</a>
<a href="reset">Reset</a></p>
<form method='POST' action='/update' enctype='multipart/form-data'><input type='file' name='update'><input type='submit' value='Update'></form>
'''


RadioButton = f'''
<form>
<p>mit welchem Netzwerk soll eine Verbindung hergestellt werden?</p>
'''


RadioStart = f'''
<input type="radio" name="SSID" value="{{SSID}}">  {{CRYPT}}{{SSID}}   ->   (Signal: {{RSSI}})
'''

RadioEnd = f'''
<br><br>
<input type="password" name="pass"> </label>
<input type="submit" value="senden">
</form>
'''

RadioLED_s = f'''
<form>
<p> soll die LED ein- oder ausgeschaltet sein?</p>
<input type="radio" name="Led" value="On" {{ontext}}>  On
<input type="radio" name="Led" value="Off" {{offtext}}>  Off
'''

RadioLED_e = f'''
<br><br>
<input type="submit" value="senden">
</form>
'''

Name = f'''
<form>
<p> {{nametext}}</p>
<input type="text" name="{{urltext}}"> </label>
<input type="submit" value="senden">
</form>
'''
