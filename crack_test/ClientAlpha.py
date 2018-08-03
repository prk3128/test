import socket
import os
import time

def TransferClient() :
    ServerIP = '192.168.0.2'
    PORT = 5010

    read_path = '/home/cae/Desktop/'
    filename = 'crack.png'

    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    file = open( read_path+filename,'rb')

    file_size = os.path.getsize(read_path+filename)

    data = file.read(file_size)

    file.close()

    sock.connect((ServerIP,PORT))

    sock.sendall(data)

    time.sleep(3)

    print("Data Transfered ......")

    sock.close()

TransferClient()
