import socket

serv_socket = socket.socket(
                                            socket.AF_INET,
                                            socket.SOCK_STREAM,
                                            proto=0)

##metodos de la Clase, no del objeto(serv_socket) socket
#print(socket.getaddrinfo("pccomponentes.com", 80))      ###nslookup devuelva lo mismo en cmd,
                                                                                    ##dir ip - no te da info lo que hay detras de este puerto

## traduce un nombre de host a una dir ip valida
#print(socket.gethostbyname("www.pccomponentes.com"))

##igual que ariba pero nos da mas info, alias [], ips
#print(socket.gethostbyname_ex("www.pccomponentes.com"))

##retorna una cadena con el hostname del equipo  como en systema
#print(socket.gethostname())

##retorna hostname a partir de una dir ipv4
#print(socket.gethostbyaddr("localhost"))       ##('KateG1lenovo', [], ['::1'])
                                                                    ##ipconfig devuelve ipv4


###Methodos de objeto serv_socket
#print(serv_socket)

##retorna un archivo descriptor del socket - es el numero
##si falla devuelve -1
##print(serv_socket.fileno())

###primero ejecutar servedor-servedor y despues servidor-cliente

serv_socket.bind(("",65432))
serv_socket.listen()
conn, addr = serv_socket.accept()

print("DATOS DESDE EL OBJETO: ", serv_socket)
##DATOS DESDE EL OBJETO:  <socket.socket fd=604, family=2, type=1,
##proto=0, laddr=('0.0.0.0', 65432)>

## retorna la dir remota a la que se conecta
##el socket. HOST, PORT
print("PEERNAME_REMOTE: ", conn.getpeername())
##PEERNAME_REMOTE:  ('127.0.0.1', 50719)
print(conn)   ##<socket.socket fd=608, family=2, type=1, proto=0,
##laddr=('127.0.0.1', 65432), raddr=('127.0.0.1', 50719)>
print(conn.fileno())  ###608

###netstat -n para ver que conexion established

##retorna la dir del propio socket HOST, PORT
print("DIRECCION PROPIA DEL SERV: ", serv_socket.getsockname())
#DIRECCION PROPIA DEL SERV:  ('0.0.0.0', 65432)
print("DIRECCION PROPIA DE LA CONEXION: ", conn.getsockname())
#DIRECCION PROPIA DE LA CONEXION:  ('127.0.0.1', 65432)

## True si es bloqueante el socket False si no lo es
print(serv_socket.getblocking())  ###True

serv_socket.settimeout(1.0)

## retorna el tiempo de espera en segundos asociado
## a las operaciones
print(serv_socket.gettimeout())   ### sin settimeout devuelve None

### sin with tenemos que cerrar manualmente

#serv_socket.close()   ### SHUT_RD SHUT_WR close va cerrar todos constantes y
## si servidor tiene algo de enviar, no puede enviar

### socket.shutdown(how)

##Shut down one or both halves of the connection.
##If how is SHUT_RD, further receives are disallowed. If how is SHUT_WR,
##further sends are disallowed.
##If how is SHUT_RDWR, further sends and receives are disallowed.

###SI DEJA ESCRIBIR - EN LADO DEL CLIENTE O EN LADO DE SERVIDOR
### NORMALMENTE EN CLIENTE
## no tiene sentido servidor sordo

##cerrar la escritura, que cliente envia que no va enviar mas cosas,
## pero cliente NO deja escuchando que envia servidor
conn.shutdown(socket.SHUT_WR) 


## cerrar que no puede recibir mas datos
conn.shutdown(socket.SHUT_RD)    ##aplicamos al Clase
conn.close()





