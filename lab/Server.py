import socket
import time
import sys
import os

def dirGen(path) :
    t = time.localtime()

    Year = t.tm_year
    Month = t.tm_mon
    MDay = t.tm_mday
    WDay = t.tm_wday
    Hour = t.tm_hour
    Min = t.tm_min
    
    dirname = str(Year)+str(Month)+str(MDay)+'_'+str(Hour)+str(Min)

    dirname =path+dirname

    os.mkdir(dirname)
    
    return dirname

def nameGen() :
    t = time.localtime()

    Year = t.tm_year
    Month = t.tm_mon
    MDay = t.tm_mday
    WDay = t.tm_wday
    Hour = t.tm_hour
    Min = t.tm_min
    Sec = t.tm_sec

    filename = str(Year)+str(Month)+str(MDay)+'_'+str(Hour)+str(Min)+str(Sec)+'.png'

    return filename

ServerIP = '192.168.0.2'
PORT = 5010

write_path = "C:\\Users\\Owner\\Desktop\\"

write_path = dirGen(str(write_path))
print("Directory : ", write_path)
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
        print("========================================")
        print("Client : ", addr[0], addr[1])

        data = conn.recv(1024)

        buffer = data

        if data :

            print("Data Recieving ......")

            while data :
                data = conn.recv(1024)
                buffer += data

            filename = nameGen()
            print("File : ",write_path+'\\'+filename)
            with open(write_path+'\\'+str(filename),'wb') as file :
                file.write(buffer)

            print(filename,sys.getsizeof(buffer),'KB')
            print("Data Recieved ......")
            print("========================================")
        data = None

        conn.close