import socket
import os

HOST = 'localhost'
PORT = 65432
FILENAME = 'wish-list.txt'

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((HOST, PORT))

    filesize = os.path.getsize(FILENAME)
    # Send the file size as 8 bytes (header)
    client.sendall(filesize.to_bytes(8, 'big'))

    with open(FILENAME, 'rb') as f:
        client.sendfile(f)

    print('File sent successfully.')