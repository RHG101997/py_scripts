import socket
import os

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "10.0.0.46"
port = 1235
bytes_per_package = 1024

filename = raw_input("Filename: ->")
if os.path.isfile(filename):
    s.connect((host,port))
    s.send(str(os.path.getsize(filename)))
    print("Requesting Permission")
    response = s.recv(bytes_per_package)
    if response[:2] == 'FN':
        print("Sending File: Please wait")
        s.send(filename)
        response = s.recv(bytes_per_package)
        if response[:2] == 'DL':
            with open(filename,'rb') as f:
                data =f.read(bytes_per_package)
                s.send(data)
                while data != "":
                    data = f.read(bytes_per_package)
                    s.send(data)
                print("Done...")
        else: 
            print("Response: DL error \n Exiting")
    else:
        print("Response: FN error \n Exiting")
else:
    print("File not FOUND")

s.close()


