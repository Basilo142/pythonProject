import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', 8888))
sock.listen(5)
# sock.setblocking(True)
# sock.setblocking(5)
# sock.setblocking(0)  # sock.blocking(False)
sock.setblocking(None)  # sock.blocking(True)


try:
    client, addr = sock.accept()
except socket.error:
    print('No conaction')
except socket.timeout:
    print('Timeout')
else:
    result = client.recv(1024)
    client.close()
    print('Message', result.decode('utf-8'))
