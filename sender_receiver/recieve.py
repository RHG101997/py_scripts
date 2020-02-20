import socket
import threading
import os


def Main():
    

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    hostname = socket.gethostname()
    host = socket.gethostbyname(hostname)
    port  = 1235
    bytes_per_package = 1024

    s.bind((host,port))
    print("Waiting for connection")
    s.listen(3)
    while True:
        conn, addr = s.accept()
        print("Conection Established with : " + str(addr))
        filesize = int(conn.recv(bytes_per_package))
        confirm = input("File size: " + str(filesize) + "Bytes, donwload (Y/N)?")
        
        if confirm == 'Y':
            conn.send(b"FN")
            filename = conn.recv(bytes_per_package)
            conn.send(b"DL")
            f = open("new_" + filename.decode("utf-8"),'wb')
            data = conn.recv(bytes_per_package)
            totalRecv = len(data)
            f.write(data)
            while totalRecv < filesize:
                data = conn.recv(bytes_per_package)
                totalRecv += len(data)
                f.write(data)
                print(str(totalRecv/float(filesize))*100 + "%")
            print("Download completed...")
            f.close()
            break

    conn.close()
    s.close()


if __name__ == '__main__':
    Main()
