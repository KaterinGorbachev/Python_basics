import socket 

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('', 65432))
server.listen()
print('Esperando clientes')

while True:
    socket_cliente, datos_cliente = server.accept()
    print('Conectado', datos_cliente)

    socket_cliente.settimeout(1)

    seguir = True
    while seguir: 
        try: 
            peticion = socket_cliente.recv(1000)
            print('Recibido', peticion.decode())

        except TimeoutError: 
            print('Timeout cerramos')
            seguir = False 

        