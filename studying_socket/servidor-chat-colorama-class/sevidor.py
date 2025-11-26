import socket
from colorama import just_fix_windows_console
just_fix_windows_console()
from colorama import Fore, Back, Style
import ipaddress

HOST = '' 
PORT = 65432
clients_limit = 10

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
            


def handle_request(conn,  s): 
    
    while True:
        data = conn.recv(1024)
        if not data: 
            break

        data_decoded = data.decode('UTF-8')

        print(Style.DIM + f"Recieved from user:{data_decoded}")
        print(Style.RESET_ALL)

        if data_decoded.lower() == 'close': 
            serv.shutdown(socket.SUT_RDWR)
            break

        respuesta = s.check_ip_hostname(data_decoded)

        print(Style.DIM + f"Servers answer:{respuesta}")
        print(Style.RESET_ALL)

        conn.send(respuesta.encode('UTF-8'))


serv = Server()
serv.start()
print(Style.DIM+"Waiting for requests")
print(Style.RESET_ALL)

conn, addr = serv.connect_clients() 

with conn:
    print(Style.DIM + f"Connected with:{addr}")
    print(Style.RESET_ALL)

    handle_request(conn, serv)
     
        

        
