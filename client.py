import socket

sock = socket.socket()
sock.connect(('10.100.1.2', 5000))

while True:
    sock.send(input(':').encode())
    data = sock.recv(1024)
    print(data.decode('utf8'))
    sock.close()


