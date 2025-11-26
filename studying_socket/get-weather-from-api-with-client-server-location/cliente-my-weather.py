import socket
from colorama import just_fix_windows_console
just_fix_windows_console()
from colorama import Fore, Back, Style
import json

HOST = 'localhost' 
PORT = 65432

class TCPClient: 
    def __init__(self, host: str = HOST, port:int = PORT, timeout=5):
        self.host = host
        self.port = port
        self.sock = None
        self.timeout = timeout

    def connect(self): 
        self.sock = socket.create_connection((self.host, self.port), timeout=self.timeout)

    def send(self, data: bytes): 
        if not self.sock: 
            raise RuntimeError("Not connected")
        self.sock.sendall(data)

    def recv(self, n=4096) -> bytes: 
        return self.sock.recv(n)
    
    def close(self): 
        try: 
            self.sock.shutdown(socket.SHUT_RDWR)
        except Exception: 
            pass

        if self.sock: 
            self.sock.close()
            self.sock = None

    def __enter__(self): 
        self.connect()
        return self
    
    def __exit__(self, exc_type, exc, tb): 
        self.close()


with TCPClient(HOST, PORT) as c: 
    c.send(b'weather')
    respWeather = c.recv().decode()
    data = json.loads(respWeather)
    [print(Fore.GREEN+k,d,sep=':') for k,d in data.items()]
    print(Style.RESET_ALL)
    

    


    