import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server: 
    server.bind(('', 65432))
    server.listen()
    print('Esperando clientes')

    while True: 
        sock_client, _ = server.accept()
        
        seguir = True
        with sock_client: 
            sock_file = sock_client.makefile('rw', encoding='utf-8')
            while seguir:
                file = open('server_file.txt', 'a', encoding='utf-8')
                line = sock_file.readline()
                file.write(line)
                file.close()
                if not line: 
                    seguir = False