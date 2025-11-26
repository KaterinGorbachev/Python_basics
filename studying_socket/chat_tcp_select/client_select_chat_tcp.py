import socket

msg = 'hola'

server_address = ('localhost', 65432)
client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Conecting to {} port {}'.format(*server_address))

client_sock.connect(server_address)

while msg != '':
    print('Click Enter to exit')
    out_msg = msg.encode()
    print('{}: sending {}'.format(client_sock.getsockname(), out_msg))
    client_sock.send(out_msg)

    data = client_sock.recv(2048)
    print('Server {}>> {}'.format(client_sock.getsockname(), data.decode()))

    msg = input('Client>> ')

print('Disconected')
client_sock.close()### does not recieve last message from server -> produce error

'''
el orden es importante!!!! 

socket.close()
inputs.remove(socket)

'''