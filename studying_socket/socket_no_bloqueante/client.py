import socket, time

counter = 0

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as c:
    c.connect(('localhost', 65432))

    while counter<5: 
        time.sleep(0.5)
        c.send('Message'.encode())
        counter+=1

    time.sleep(10)