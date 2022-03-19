import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(b'Welcome to hell', ('127.0.0.1', 8888))
