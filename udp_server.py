import socket



def run():
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_sock.bind(('127.0.0.1', 5000))
    server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    clients = []
    while 1:
        data, addres = server_sock.recvfrom(1024)
        if addres not in clients:
            clients.append(addres)
            print(clients)
        for client in clients:
            if client == addres:
                continue
            server_sock.sendto(data, client)

if __name__ == '__main__':
    run()
