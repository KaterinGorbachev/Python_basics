import socket, struct
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client: 
    server_address = ('', 5557)
    client.bind(server_address) ### al utilizar la misma maquina otro cliente no deja

    multicast_grp = '224.3.29.71'
    group=socket.inet_aton(multicast_grp)
    mreq = struct.pack('4sl', group, socket.INADDR_ANY)

    client.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

    while True: 
        msg, server = client.recvfrom(2048)
        print(str(server))
        print(msg.decode())


### ??? puede ser solo 1 client por client.bind(server_address)