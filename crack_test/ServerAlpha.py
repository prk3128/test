import socket
import os
import time
import sys


def nameGen() :
    t = time.localtime()

    Year = t.tm_year
    Month = t.tm_mon
    MDay = t.tm_mday
    WDay = t.tm_wday
    Hour = t.tm_hour
    Min = t.tm_min
    Sec = t.tm_sec

    filename = str(Year)+str(Month)+str(MDay)+'_'+str(Hour)+':'+str(Min)+':'+str(Sec)+'.png'

    return filename

ServerIP = '127.0.0.1'
PORT = 5010

write_path = '/home/cae/Desktop/'
    #'c:\\Users\\Owner\\Desktop\\'

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((ServerIP,PORT))
sock.listen(5)

print("Server initialzed ......")

while(1) :

    try :
        conn, addr = sock.accept()

    except KeyboardInterrupt :
        print("Server terminated ......")
        conn.close()
        break

    if conn is not None :

        print("Client : ", addr[0], addr[1])

        data = conn.recv(1024)

        buffer = data

        if data :

            print("Data Recieving ......")

            while data :
                data = conn.recv(1024)
                buffer += data

            filename = nameGen()

            with open(write_path+filename,'wb') as file :
                file.write(buffer)

            print(filename,sys.getsizeof(buffer),'KB')
            print("Data Recieved ......")

        data = None

        conn.close


