import socket, ssl

hostname = 'www.python.org'

context = ssl._create_unverified_context(ssl.PROTOCOL_TLS_CLIENT)
context.load_verify_locations('.../ssl_fakecertificados/certificadonew.crt')

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client: 
    client.connect(('localhost', 65432))
    with context.wrap_socket(client) as sclient: 
        msg = sclient.recv(1024)
        msg = msg.decode()
        print(msg)