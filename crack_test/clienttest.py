from socket import *

serverIP = '192.168.0.1'
PORT = 8080

read_path = '/home/cae/Desktop/'
filename = 'calibration.png'

sock = socket(AF_INET,SOCK_DGRAM)

#sock.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)

file = open( read_path+filename,'rb')

data = file.read()

file.close()

sock.sendto(data, (serverIP,PORT))
#4096