import socket, time, datetime

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 1)
    message = 'Hello World desde el PUBLISHER'
    multicast_group = ('224.3.29.71', 5557)
    print('Server iniciando... ')

    while True:
        sock.sendto((message+' '+str(datetime.datetime.now())).encode(), multicast_group)
        time.sleep(1)