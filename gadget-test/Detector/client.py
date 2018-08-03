import socket
import os
import time

class TrasnferClient() :

    def __init__(self,ServerIP='192.168.0.2',PORT=5010,read_path='/home/cae/Desktop/',filename='crack.png') :

        self.read_path = read_path
        self.filename = filename
        self.ServerIP = ServerIP
        self.PORT = PORT

    def Transfer(self) :

        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

        if sock is not None:
            print("Connection ... OK")
            sock.connect((self.ServerIP, self.PORT))
            print("Server : ", self.ServerIP, self.PORT)

        file = open( self.read_path+self.filename,'rb')

        file_size = os.path.getsize(self.read_path+self.filename)

        data = file.read(file_size)

        file.close()

        sock.sendall(data)

        sock.close()

        time.sleep(3)

        print("Data Transfered ......")
