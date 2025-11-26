import socket, time

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client: 
    client.connect(('localhost', 65432))

    client_file = client.makefile('rw')
    client_file.write('hola\ntime\nclose\n')
    client_file.flush()

    
    
    
    line = client_file.readline()
    print('From server: ', line)


    


    """ lines = client_file.readlines()
    for l in lines: 
        print(l) """