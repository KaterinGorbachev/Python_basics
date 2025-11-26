import socket, ssl

context = ssl._create_unverified_context(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain('.../ssl_fakecertificados/certificadonew.crt', '.../ssl_fakecertificados/private.key')

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock: 
    sock.bind(('', 65432))
    sock.listen(5)
    print('Waiting clients... ')
    with context.wrap_socket(sock, server_side=True) as ssock: 
        conn, addr = ssock.accept()
        print(addr)
        conn.send('Hola desde servidor'.encode())
        
