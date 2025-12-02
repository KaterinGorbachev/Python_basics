# Python basics

## Python educational scripts

Code [description](https://github.com/KaterinGorbachev/Python---basics-/blob/main/hangman_python.md) for Hangman game.


## Studying socket

Create [TCP server](https://github.com/KaterinGorbachev/Python_basics/tree/main/studying_socket/servidor-chat-colorama-class) that returns IP address or Hostname back to the clients request. Using classes to create reusable Server object where all functionality (start server, accept clients, resolve hostnames, close connection) is grouped into methods.

```python 

    class Server: 
    def __init__(self, host: str = HOST, port: int = PORT, backlog: int = clients_limit):
        self.host = host
        self.port = port 
        self.backlog = backlog
        self.sock: socket.socket | None = None

    def start(self): 
        """Start listening and accepting clients"""
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((self.host, self.port))
        self.sock.listen(self.backlog)

        print(Style.DIM+ f"Server listening on {self.host}:{self.port}")
        print(Style.RESET_ALL)


    def connect_clients(self): 
        conn, addr = self.sock.accept() 
        return conn, addr


    def check_ip_hostname(self, query: str): 
        """required: import ipaddress """
        try: 
            ip = ipaddress.ip_address(query)
            try: 
                host_name,_,_ = socket.gethostbyaddr(query)
                return f"Hostname for {query}: {host_name}"
            except socket.herror:
                return f"No hostname found for IP {ip}."
        except ValueError:
        # Not an IP address → treat as hostname
            try:
                ip = socket.gethostbyname(query)
                return f"IP for {query}: {ip}"
            except socket.gaierror:
                return f"Unknown hostname: {query}"
            
    def close_connection(self):
        """Stop the server and close the listening socket."""
        
        if self.sock:
            try:
                self.sock.close()
            except Exception as e:
                print(Style.DIM+ f"Error {e}")
                print(Style.RESET_ALL)
                pass
```


```python 
    def __init__(self, host: str = HOST, port: int = PORT, backlog: int = clients_limit):

```
Runs automatically when you create a new Server instance.
Stores:
    - host → the IP address/interface the server listens on (e.g. "127.0.0.1" or "0.0.0.0")

    - port → the port number (e.g. 8000 or 9999)

    - backlog → how many clients can wait in queue before being accepted

self.sock is set to None initially — socket is not created yet.


Colourfully prints states in console with

```python 
    from colorama import just_fix_windows_console
    just_fix_windows_console()
    from colorama import Fore, Back, Style
``` 

```python 
    print(Style.DIM+ f"Server listening on {self.host}:{self.port}")
    print(Style.RESET_ALL)
```


Start server on a given HOST and PORT 

```python
    serv = Server()
    serv.start()
```

Accept clients

```python 
    conn, addr = serv.connect_clients()
```

connect_clients() internally calls:

```python 
    conn, addr = self.sock.accept()
```


Create TCP client for the server. 

```python
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))
```


Function to get user input: 

```python
    def user_input(): 
    print(Style.DIM + "Enter hostname or IPv4 address")
    print(Style.RESET_ALL)
    msg = input(Fore.BLUE + "> ").strip()
    print(Style.RESET_ALL)
    return msg
```


Request to the server with slight delay for nicer UX: 

```python 
    print(Style.DIM + "Searching...")
    print(Style.RESET_ALL)
    time.sleep(0.3)
    client_socket.sendall(msg.encode('UTF-8'))
```


Close clients socket and connetion with word 'close': 

```python 
    if msg == "close": 
    print(Fore.GREEN + "Connection closed")
    print(Style.RESET_ALL)
    client_socket.sendall(msg.encode('UTF-8'))
    client_socket.shutdown(socket.SHUT_RDWD)
    client_socket.close()
    break
```


Create [TCP server and client](https://github.com/KaterinGorbachev/Python_basics/tree/main/studying_socket/socket-tcp-file-wrap-connect-mysql-login-logout-get-api-data) to make user registration in MySQL, users login, advanced functionality with API request for logged in users, closing users session and closing connection with server from the clients part. Logging in console and file. 


Non-Blocking [TCP Server Using select](https://github.com/KaterinGorbachev/Python_basics/tree/main/studying_socket/chat_tcp_select)


The server accepts multiple clients, receives messages without blocking the main loop, and responds depending on the input.


Non-Blocking Mode

```python
    select.select
```


The server uses select to monitor:

    - readable sockets → data received or new client connections

    - writable sockets → ready for sending responses

    - exception sockets → error conditions

This allows the server to efficiently handle multiple clients in a single thread.

Message Buffer

Outgoing messages are stored in the dictionary:
output_messages[socket]
so that each client keeps its own response.



```python 
    # Create a TCP server socket
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setblocking(False)               # Non-blocking mode
    server.bind(('', 65432))                # Listen on all interfaces, port 65432
    server.listen()
```


# Lists required by select()
inputs = [server]                       # Sockets to read from (server + clients)
outputs = []                            # Sockets ready to write responses
output_messages = {}                    # Stores messages for each client


How It Works
1. Server Setup

Creates a TCP socket

Enables non-blocking mode

Starts listening for new clients

Registers the server socket in inputs so select can notify when a new client connects

2. Handling New Connections

When the server socket becomes readable, it means a client is trying to connect:

client, address = server.accept()
inputs.append(client)


The new client socket is also set to non-blocking and added to the inputs list.

3. Handling Incoming Data

If a client socket is readable, it means the client sent data:

message = socket.recv(2048).decode()


Then the server decides how to respond:

If the client says "hola" → respond with "Hola caracola"

If the message is empty ('') → client disconnected. Empty string indicates a clean disconnect. The server closes the socket and removes it from the list of active inputs.

Otherwise → send the current timestamp

Responses are placed in a message buffer, not sent immediately.

4. Sending Responses

If a socket becomes writable, meaning it is ready for sending:

socket.send(output_messages[socket].encode())

Once the message is sent, the socket is removed from outputs.














