import socket
from colorama import just_fix_windows_console, Fore, Style

just_fix_windows_console()

HOST = 'localhost'
PORT = 65432
BUFFERSIZE = 4096

clients = []
messages = ""  # <-- your chat history

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((HOST, PORT))

print(Fore.GREEN + f"Server started on {HOST}:{PORT}" + Style.RESET_ALL)

while True:
    try:
        msg, addr = server.recvfrom(BUFFERSIZE)
        text = msg.decode()

        # add new client
        if addr not in clients:
            clients.append(addr)
            print(Fore.CYAN + f"New client connected: {addr}" + Style.RESET_ALL)

        # handle signup messages
        if text.startswith("SIGNUP_TAG:"):
            name = text.split(":", 1)[1].strip()
            join_msg = f"{name} joined the chat!"
            messages += join_msg + "\n"  # add to history

            # send full chat history to the new user
            server.sendto(f"--- Chat history ---\n{messages}".encode(), addr)

            # tell everyone that a new user joined
            for client in clients:
                if client != addr:
                    server.sendto(join_msg.encode(), client)

            print(Fore.YELLOW + join_msg + Style.RESET_ALL)

        else:
            # add message to history
            messages += text + "\n"

            # broadcast the message to everyone
            for client in clients:
                try:
                    server.sendto(text.encode(), client)
                except Exception as e:
                    print(Fore.RED + f"Broadcast error to {client}: {e}" + Style.RESET_ALL)
                    clients.remove(client)

        # Print updated server log
        print(Fore.MAGENTA + "Chat log:" + Style.RESET_ALL)
        print(messages)

    except Exception as e:
        print(Fore.RED + f"Receive error: {e}" + Style.RESET_ALL)

        


        
