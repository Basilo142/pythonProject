import socketserver


class EchoUDOPHandler(socketserver.BaseRequestHandler):

    def handle(self):
        data, socket = self.request
        print('Address: {}'.format(self.client_address[0]))
        print('Data: {}'.format(data.decode()))
        print('All client_address - {}'.format(self.client_address))
        socket.sendto(data, self.client_address)


if __name__ == '__main__':
    with socketserver.UDPServer(('0', 8888), EchoUDOPHandler) as server:
        server.serve_forever()
