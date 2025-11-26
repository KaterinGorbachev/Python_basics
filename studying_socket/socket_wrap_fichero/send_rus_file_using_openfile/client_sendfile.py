import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect(('localhost', 65432))
    with open('wish-list.txt', 'r', encoding='utf-8') as f, client.makefile('w', encoding='utf-8') as client_file:
        for line in f:
            client_file.write(line)
        client_file.flush()   # ensure everything is sent
    # automatically closes and sends EOF when exiting 'with' block
