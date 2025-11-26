import socket, time, datetime

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server: 
    server.bind(('', 65432))
    server.listen()
    print('Esperando clientes.. ')

    while True: 
        socket_cliente, datos_cliente = server.accept()

        with socket_cliente: 
            print('Conectado', datos_cliente)
            seguir = True
            socket_file = socket_cliente.makefile('r')
            socket_write = socket_cliente.makefile('w')
            message = ''
            while seguir: 
                print('Entro en while seguir')
                line = socket_file.readline()
                l = line.rstrip('\n')

                
                
                 
                print('Recibido', l, sep='_')
                if l == 'hola': 
                    print(datos_cliente, "envia hola:contesto caracola" )
                    message += 'contesto caracola'+' '
                    print(message)
                if l == 'time': 
                    print(datos_cliente, "envia time:contesto datetime" )
                    message += str(datetime.datetime.now())+' '
                    print(message)
                                        

                if l == 'close': 
                    message += 'Adios Mario Bross\n'
                    print(message)
                    print('contesto', message)
                    socket_write.write(message)
                    socket_write.flush()
                    socket_cliente.close()
                    print('Desconectado', datos_cliente)
                    seguir=False

                
                    