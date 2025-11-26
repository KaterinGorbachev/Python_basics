import socket, time

HOST = 'localhost'
PORT = 65432
buffersize = 4096

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client: 
    print(f'client> soy un cliente UDP')
    
    client.sendto('soy un cliente UDP'.encode(), (HOST, PORT))
    time.sleep(0.3)

    data, _ = client.recvfrom(buffersize)
    print(f'server>> {data.decode()}')

    print(f'client> adios')
    client.sendto('adios'.encode(), (HOST, PORT))
    data, _ = client.recvfrom(buffersize)
    print(f'server>> {data.decode()}')

    client.close()


