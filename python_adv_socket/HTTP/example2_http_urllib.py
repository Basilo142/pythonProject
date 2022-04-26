from urllib import request

response = request.urlopen('http://example.com')

print('status - ', response.status)
print('getcode() - ', response.getcode())
print('msg - ', response.msg)
print('reason - ', response.reason)
print('headers - ', response.headers)
print('getheaders() - ', response.getheaders())
print('headers.get - ', response.headers.get('Content-Type'))
print('Content-Type - ', response.getheader('Content-Type'))
