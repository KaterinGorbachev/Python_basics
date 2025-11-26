import socket
import time 

HOST = 'localhost'
PORT = 65432
buffersize = 4096

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client: 
    exit = 'client starts conversation'
    print(exit)
    while exit != 'adios': 
        client.sendto(exit.encode(), (HOST, PORT))
        time.sleep(0.3)
        data, _ = client.recvfrom(buffersize)
        print(f'server> {data.decode()}')
        exit = input('User> ')

    if exit == 'adios': 
        client.sendto(exit.encode(), (HOST, PORT))
        client.close()
