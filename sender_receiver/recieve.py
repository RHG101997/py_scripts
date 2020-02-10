import socket
import threading
import os


def Main():
    host = "10.0.0.46"
    port  = 1235
    bytes_per_package = 1024

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host,port))
    print("Waiting for connection")
    s.listen(3)
    while True:
        conn, addr = s.accept()
        print("Conection Established with : " + str(addr))
        filesize = int(conn.recv(bytes_per_package))
        confirm = raw_input("File size: " + str(filesize) + "Bytes, donwload (Y/N)?")
        
        if confirm == 'Y':
            conn.send("FN")
            filename = conn.recv(bytes_per_package)
            conn.send("DL")
            f = open("new_" + filename,'wb')
            data = conn.recv(bytes_per_package)
            totalRecv = len(data)
            f.write(data)
            while totalRecv < filesize:
                data = conn.recv(bytes_per_package)
                totalRecv += len(data)
                f.write(data)
                print "{0:.2f}".format((totalRecv/float(filesize))*100)+ "%"
            print("Download completed...")
            f.close()

    conn.close()
    s.close()


if __name__ == '__main__':
    Main()
