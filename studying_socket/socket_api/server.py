import requests, json
import socket


try:
    api_data = requests.get("https://rickandmortyapi.com/api/character/?page=2")
    characters = api_data.json()
    

except Exception as e: 
    print('API error', e)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server: 
    server.bind(('', 65432))
    server.listen()
    print('Esperando clientes')

    while True: 
        client_sock, client_data = server.accept()

        with client_sock: 
            file = client_sock.makefile('rw')
            seguir = True
            while seguir: 
                line = file.readline()
                print('Clients message: ', line.rstrip('\n'))
                if not line:
                    break 
                if line.rstrip('\n') == 'who': 
                    answer = characters['results'][0]['name']
                    print('Servers answer', answer)
                    file.write(answer+ '\n')
                    file.flush() 

                if line.rstrip('\n') == 'exit': 
                    seguir = False
                    print('Connection closed with', client_data)
                    client_sock.close()
                    

