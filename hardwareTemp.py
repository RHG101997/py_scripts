"""
You have to run this script as administrator.
PowerShell is used.
I am not sure, if the temperature reading is right.
"""

import subprocess
import os
import datetime

psscript = """
$t = Get-WmiObject MSAcpi_ThermalZoneTemperature -Namespace “root/wmi”

while (1) {$t.CurrentTemperature; sleep 5}
"""

si = subprocess.STARTUPINFO()
si.dwFlags |= subprocess.STARTF_USESHOWWINDOW

cmd = ['powershell.exe', '-Command',  psscript]
proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, startupinfo=si)

with open(r'C:\Users\skyradar\Desktop\temp.txt', 'w') as fd:
    while True:
        tmp = proc.stdout.readline()
        proc.stdout.readline() # hack to prevent output twice
        celsius = int(tmp) / 10 - 273.15
        celsius_str = f'{celsius:.2f};{datetime.datetime.now().isoformat()}'
        print(celsius_str)
        fd.write(celsius_str)
        fd.write(os.linesep)