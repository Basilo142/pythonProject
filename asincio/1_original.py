import socket
from select import select

list_with_sock = []


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('localhost', 2525))
server_socket.listen()


def accept_connection(server_socket):
    print('Before .accept()')
    client_socket, addr = server_socket.accept()
    print('Connect from ', addr)
    send_message(client_socket)
    list_with_sock.append(client_socket)


def send_message(client_socket):
    request = client_socket.recv(4096)
    if request:
        response = 'Hello ...\n'.encode()
        client_socket.send(response)
    else:
        client_socket.close()


def event_loop():
    while True:
        redy_to_read, _, _ = select(list_with_sock, [], [])

        for soc in redy_to_read:
            if soc is server_socket:
                accept_connection(soc)
            else:
                send_message(soc)


if __name__ == '__main__':
    list_with_sock.append(server_socket)
    event_loop()
