import socket

s_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s_socket.bind(('localhost', 5000))
s_socket.listen()


while True:
    c_socket, addr = s_socket.accept()
    print('Connection from', addr)

    while True:
        request = c_socket.recv(4096)


        if not request:
            break

        else:
            response = 'Hello Bro!!!!\n'.encode()
            c_socket.send(response)

    c_socket.close()
