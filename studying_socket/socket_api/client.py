import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
with client: 
    client.connect(('localhost', 65432))

    file = client.makefile('rw')
    file.write('who\n')
    file.flush()
    line = file.readline()
    print('Servers answer', line)
    file.write('exit\n')
    file.flush()
    client.close()
