'''
https://pythonprogramming.net/python-port-scanner-sockets/
'''
## open a server on a local host first 

import socket
 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = ''

file = open('ports.txt', 'a')

def pscan(port): 
    try: 
        s.connect((server, port))
        return True
    except: 
        return False
    
for x in range(1, 55000): 
    if pscan(x): 
        print(f'Port {x} is open')
        file.write(f'Port {x} is open\n')
        
    else: 
        print('Port', x, 'is closed')
        file.write(f'Port {x} is closed\n')
        
        
file.close()
    



