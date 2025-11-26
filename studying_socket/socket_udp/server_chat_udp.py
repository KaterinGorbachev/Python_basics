""" import socket
HOST = 'localhost'
PORT = 65432
buffersize = 4096

s_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s_sock.bind((HOST, PORT))
print('Server UDP is up... ')
while True: 
    print("Escuchando peticiones desde", s_sock.getsockname())
    data, addr = s_sock.recvfrom(buffersize)
    print("Mensaje del Cliente: ", data.decode('utf-8'), 'enviado por ', addr)
    msg = 'Hola soy un servidor UDP'
    s_sock.sendto(msg.encode(), addr) """

import socket 
import threading 
import queue

HOST = 'localhost'
PORT = 65432
buffersize = 4096

messages = queue.Queue()
clients = []

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((HOST, PORT))

def receive(): 
    '''recieve and safe in messages'''
    while True: 
        try: 
            message, addr = server.recvfrom(buffersize)
            messages.put((message, addr))
        except: 
            pass

def broadcast():
    while True: 
        while not messages.empty(): 
            message, addr = messages.get()
            print(message.decode())
            if addr not in clients: 
                clients.append(addr)

            for client in clients: 
                try: 
                    if message.decode().startswith("SIGNUP_TAG:"): 
                        #get nickname
                        name = message.decode()[message.decode().index(':')+1:]
                        #send a new name to each client
                        server.sendto(f"{name} joined".encode(), client)
                    else: 
                        #message was not decoded
                        server.sendto(message, client)

                except: 
                    clients.remove(client)

t1 = threading.Thread(target=receive)
t2 = threading.Thread(target=broadcast)

t1.start()
t2.start()


print(f"Server started on {HOST}:{PORT}")
t1.join()
t2.join() 



