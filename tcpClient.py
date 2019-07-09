import socket
import json
import math

TCP_IP = '10.0.0.194'
TCP_PORT = 5200
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
while True:
    data = s.recv(BUFFER_SIZE)
    data = json.loads(data)
    temp = data["CpuInfo"]["fTemp"]
    print("Temp:\t" + str(temp[0]))

s.close()