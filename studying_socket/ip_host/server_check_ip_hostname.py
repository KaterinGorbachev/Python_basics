import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST = 'localhost'
PORT = 65432

with s: 
    
    s.bind((HOST, PORT))
    s.listen(1)

    ##ip to hostname 
    hostname = socket.gethostbyaddr('146.197.246.74')
    print(hostname)
    ipname = socket.gethostbyname('whq-anyconnect.nike.com')
    print(ipname)