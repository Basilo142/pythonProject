import socket


def parser_http_response(text_result: str):
    lines = text_result.split('\n')
    status_raw, lines = lines[0], lines[1:]
    protocol, status_code, *message = status_raw.split(' ')
    empty_index = 1
    headers = {}
    for index, line in enumerate(lines):
        line = line.strip()
        line = line.strip('\r')
        if line == '':
            empty_index = index
            break
        print(line)
        k, _, v = line.partition(':')
        headers.setdefault(k.strip(), v.strip())
    content = ''.join(lines[empty_index + 1:])
    print('statys = {}'.format(int(status_code)))
    print('headers = {}'.format(headers))
    print('content = {}'.format(content))
    return int(status_code), headers, content


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('example.com', 80))
# sock.connect(('google.com', 80))
content_items = [
    'GET / HTTP/1.1',
    # 'Host: google.com',
    'Host: example.com',
    'Connection: keep-alive',
    'Accept: text/html',
    '\n'
]
content = '\n'.join(content_items)
print('*** MESSAGE ***')
print(content)
print('*** END ***')
sock.send(content.encode())
result = sock.recv(10024)
print(result.decode())
text_result = result.decode()


if __name__ == '__main__':
    print('*** parser ***')
    param = parser_http_response(text_result)

