import socket, select, datetime

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setblocking(False)
server.bind(('', 65432))
server.listen()

inputs = [server]
outputs = []
output_messages= {}

while True: 
    readables, writables, exceptions = select.select(inputs, outputs, inputs)

    for socket in readables:
        # debetia usar simpre la palabra reservada socket???????
        if socket is server: 
            print('Aceptando clientes')
            #como podemos usar cl_data???
            client, cl_data = server.accept()
            client.setblocking(False)
            inputs.append(client)

        else: 
            message = socket.recv(2048).decode()
            if message == 'hola': 
                output_messages[socket] = 'Hola caracola'
                outputs.append(socket) 
                ### se pone en writables
            elif message == '': 
                #### ???? how to terminate socket connection carefuly
                #### after sending '' client disconected without sending anything else
                #output_messages[socket] = 'Adios Marios Bross'
                #outputs.append(socket)
                socket.close()
                inputs.remove(socket)
                
                
            else: 
                output_messages[socket] = str(datetime.datetime.now())
                outputs.append(socket)



    for socket in writables: 
        socket.send(output_messages[socket].encode())
        outputs.remove(socket)
