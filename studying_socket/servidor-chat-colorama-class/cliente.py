import socket 
from colorama import just_fix_windows_console
just_fix_windows_console()
from colorama import Fore, Back, Style
import time

HOST='localhost'
PORT=65432

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

def user_input(): 
    print(Style.DIM + "Enter hostname or IPv4 address" )
    print(Style.RESET_ALL)
    msg = input(Fore.BLUE + "> ").strip()
    #msg = "www.nike.com"
    #msg = "146.197.246.73"
    print(Style.RESET_ALL)
    return msg

try: 

    msg = user_input()
    while True: 
            
        if msg == "close": 
            print(Fore.GREEN + "Connection closed")
            print(Style.RESET_ALL)
            client_socket.sendall(msg.encode('UTF-8'))
            client_socket.shutdown(socket.SHUT_RDWD)
            client_socket.close()
            break

        print(Style.DIM + "Searching... ")
        print(Style.RESET_ALL)
        time.sleep(0.3)
        client_socket.sendall(msg.encode('UTF-8'))

       
        data = client_socket.recv(2048)
        msg_server = data.decode('UTF-8')
        print(Fore.GREEN + f"Server> {msg_server}")
        print(Style.RESET_ALL)

        msg = user_input()

        

except Exception as e: 
    print(Style.DIM + f"Error> {e}")
    print(Style.RESET_ALL)

   
