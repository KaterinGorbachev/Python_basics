import socket
import os

HOST = ''       # Listen on all interfaces
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind((HOST, PORT))
    server.listen(1)
    print('Server listening on', PORT)

    while True:
        conn, addr = server.accept()
        with conn:
            print('Connected by', addr)
            filename = 'server_received.txt'

            # receive header: first 8 bytes = file size
            header = conn.recv(8)
            if not header:
                break
            filesize = int.from_bytes(header, 'big')
            print(f"Expecting {filesize} bytes")

            received = 0
            with open(filename, 'wb') as f:
                while received < filesize:
                    chunk = conn.recv(4096)
                    if not chunk:
                        break
                    f.write(chunk)
                    received += len(chunk)
            print('File received:', filename)