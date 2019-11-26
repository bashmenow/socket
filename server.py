import socket



def run():
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_sock.bind(('10.100.1.2', 5000))
    server_sock.listen(3)

    clients = []
    while True:
        client, addr = server_sock.accept()
        if client not in clients:
            clients.append(client)
        request = client.recv(1024)
        print('[{}]'.format(addr[0]), ':  ', request.decode('utf8'))
        for cl in clients:
            cl.send('[{}]:  {}'.format(addr[0], request).encode())
    client.close()


if __name__ == '__main__':
    run()
