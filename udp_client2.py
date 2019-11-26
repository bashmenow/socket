import socket
import threading

def read_sock():
    while 1:
        data = client_sock.recv(1024)
        print(data.decode('utf8'))

server = '127.0.0.1', 5000
alias = input()
client_sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
client_sock.bind(('', 0))
client_sock.sendto((alias+' Connect to server').encode('utf-8'), server)
stream = threading.Thread(target=read_sock)
stream.start()

while 1 :
     message = input()
     client_sock.sendto(('['+alias+']'+message).encode('utf-8'), server)