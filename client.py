import socket
import os
import time

class TrasnferClient() :

    def __init__(self,ServerIP='192.168.0.2',PORT=5010) :

        self.ServerIP = ServerIP
        self.PORT = PORT

    def Transfer(self,read_path='/home/cae-lab/Desktop/',filename='result.png') :

        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

        if sock is not None:
            print("Connection ... OK")
            sock.connect((self.ServerIP, self.PORT))
            print("Server : ", self.ServerIP, self.PORT)

        file = open( read_path+filename,'rb')

        file_size = os.path.getsize(read_path+filename)

        data = file.read(file_size)

        file.close()

        sock.sendall(data)

        sock.close()

        time.sleep(3)

        print("Data Transfered ......")
