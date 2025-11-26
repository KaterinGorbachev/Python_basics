import requests
import random
import socket
import json
from colorama import just_fix_windows_console
just_fix_windows_console()
from colorama import Fore, Back, Style

HOST = '' 
PORT = 65432
clients_limit = 10

class Server: 
    def __init__(self, host: str = HOST, port:int = PORT, backlog: int = clients_limit): 
        self.host = host
        self.port = port
        self.backlog = backlog
        self.sock: socket.socket | None = None

    def start(self): 
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((self.host, self.port))
        self.sock.listen(self.backlog)

        print(Style.DIM+ f"Server listening on {self.host}:{self.port}")
        print(Style.RESET_ALL)

    def connect_clients(self):
        conn, addr = self.sock.accept()
        
        return conn, addr
    
    def close_connection(self, query:str):
        print(Style.DIM+ f"Client closed connection")
        print(Style.RESET_ALL)

def get_info_ip(ip):
    ###consulta a la api de localizacion 
    ### en una lista ip, pais, ciudada, lat, long
    
    try:
        r = requests.get(f'http://ip-api.com/json/{ip}?fields=country,city,lat,lon&lang=fr')
        data = r.json()
          
    except Exception as e: 
        print("Error en API: ", e)

    return data

def get_weather(ip): 
    units = 'metric'
    API_key = ''###get api key on the api website
    data_user = get_info_ip(ip)
    lat = data_user['lat']
    lon = data_user['lon']
    w = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units={units}&appid={API_key}')
    weather = w.json()
    #[print(k,d,sep=':'weather]
    response={}
    response['country'] = data_user['country']
    response['city'] = data_user['city']
    response['weather'] = {}
    response['weather']['temp'] = weather['main']['temp']
    response['weather']['feels_like']=weather['main']['feels_like']
    response['weather']['temp_min'] = weather['main']['temp_min']
    response['weather']['temp_max'] = weather['main']['temp_max']
    response['weather']['humidity'] = weather['main']['humidity']
    response['wind'] = weather['wind']
    return response

def handle_client(conn, addr): 
    try: 
        with conn: 
            print(Style.DIM + f"Connected user:{addr}")
            print(Style.RESET_ALL)
            while True: 
                data = conn.recv(4096)
                if not data: # EOF -> client disconnected
                    print(Style.DIM+f"Client {addr} disconnected")
                    print(Style.RESET_ALL)
                    break
                msg = data.decode()
                if msg.lower() == 'weather': 
                    # using fake ip
                    retWeather = get_weather('146.197.246.74')
                    jsonWeather = json.dumps(retWeather)   ### dictionary no encode 
                    print(jsonWeather)
                    conn.sendall(jsonWeather.encode())

    except Exception as e: 
        print(Style.DIM+ f"Error {e}")
        print(Style.RESET_ALL)
        exit

serv = Server()
serv.start()
print(Style.DIM+"Waiting for requests")
print(Style.RESET_ALL)

while True:
    conn, addr = serv.connect_clients()
    handle_client(conn, addr)








