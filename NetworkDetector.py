import urllib.request
import socket

host = 'http://matrix-live.com/'

def connection(host):
    try:
        urllib.request.urlopen(host)
        print('Connected')
        return True
    except:
        print('Not Connected')
        return False

def ip():
    host = socket.gethostname()
    ip_address = socket.gethostbyname(host)
    print(host)
    print(ip_address)

connection(host)
ip()