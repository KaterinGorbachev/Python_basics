import socket 

with socket.socket(socket.AF_INET, 
                   socket.SOCK_STREAM) as c: 
    
    c.connect(('localhost', 40000))

    c.sendall('GET /images/firefox-icon.png HTTP/1.1\r\nHost: localhoat.es\r\nAccept: image/png\r\nConnection: close\r\n\r\n'.encode('utf-8'))

    ##------guardar imagen ------
    f = open('imagen_robada.png', 'wb')
    while True: 
        data= c.recv(1024)
        imagen += data

        if not data: 
            break 


    pos = (imagen.find(b'\x89PNG'))

    f.write(imagen[pos:])
    f.close()
    print('Imagen Robada')
        