import socket

serverIP = '192.168.1.74'
PORT = 8080

write_path = '/home/cae/Desktop/'
filename = 'comm.png'

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.bind((serverIP,PORT))

while True :

    data, addr = sock.recvfrom(100000)

    print("Client : ",addr[0], addr[1])

    with open( write_path+filename,'wb') as f :
        try :
            f.write(data)
        except Exception as x :
            print(x)

    print('Data Received')
    # 1599-7569
    # 시트 앤 몰