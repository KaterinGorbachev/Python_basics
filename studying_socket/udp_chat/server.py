import socket

HOST = 'localhost'
PORT = 65432
buffersize = 4096

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as ssock: 
    ssock.bind((HOST, PORT))
    data, addr = ssock.recvfrom(buffersize)
    print(f'server> conexion ok')
    message = 'conexion ok'
    ssock.sendto(message.encode(), addr)

    seguir = True

    while seguir:

        data, addr = ssock.recvfrom(buffersize)
        
        print(f'{addr}> {data.decode()}')
        if data.decode() =='adios': 
            print(f'server> adios')
            message = 'adios'
            ssock.sendto(message.encode(), addr)
            seguir = False
            ssock.shutdown(socket.SHUT_WR)
            break
        print(f'server> response server')
        message = 'response server'
        ssock.sendto(message.encode(), addr)
        
            
            


