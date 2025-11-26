import socket
import random

BUFFERSIZE = 4096
HOST = 'localhost'
PORT = 65432

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.bind((HOST, random.randint(8000, 9000)))

name = input("Nickname: ")

# Send signup message
client.sendto(f"SIGNUP_TAG:{name}".encode(), (HOST, PORT))

print("Type !q to quit")

while True:
    
    msg, _ = client.recvfrom(BUFFERSIZE)
    print(msg.decode())
    
    message = input("> ")
    if message == "!q":
        client.sendto(f"{name} has left the chat.".encode(), (HOST, PORT))
        break

    client.sendto(f"{name}: {message}".encode(), (HOST, PORT))