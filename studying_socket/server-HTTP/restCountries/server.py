import socket

HOST = 'localhost'
PORT = 65534

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_sock:
    server_sock.bind((HOST, PORT))
    server_sock.listen()
    print(f"Server running on {PORT}...")

    while True:
        conn, addr = server_sock.accept()
        with conn:
            request = b''
            # Read until end of headers (\r\n\r\n)
            while b'\r\n\r\n' not in request:
                chunk = conn.recv(1024)
                if not chunk:
                    break
                request += chunk

            request_decoded = request.decode('utf-8', errors='replace')
            print("Request received:\n", request_decoded)

            # Parse request line
            request_line = request_decoded.splitlines()[0]
            method, path, version = request_line.split()

            if path == '/':
                #response_body = '<!DOCTYPE html><html><head><meta charset="UTF-8"></head><body><h1>Hola Mundo</h1></body></html>'
                with open('index.html', 'r', encoding='utf-8') as f:
                    index_content = f.read()
                response_headers = (
                    "HTTP/1.1 200 OK\r\n"
                    "Content-Type: text/html; charset=UTF-8\r\n"
                    f"Content-Length: {len(index_content.encode('utf-8'))}\r\n"
                    "Connection: close\r\n"
                    "\r\n"
                )
                full_response = response_headers + index_content
                conn.sendall(full_response.encode('utf-8'))

            if path == '/favicon.ico':
                response_body = '<h1>Not Found</h1>'
                response_headers = (
                    "HTTP/1.1 404 Not Found\r\n"
                    "Content-Type: text/html; charset=UTF-8\r\n"
                    f"Content-Length: {len(response_body.encode('utf-8'))}\r\n"
                    "Connection: close\r\n"
                    "\r\n"
                )
                full_response = response_headers + response_body
                conn.sendall(full_response.encode('utf-8'))

            if path == '/styles/style.css': 
                with open('styles/style.css', 'r', encoding='utf-8') as f:
                    css_content = f.read()
                response_headers = (
                    "HTTP/1.1 200 OK\r\n"
                    "Content-Type: text/css; charset=UTF-8\r\n"
                    f"Content-Length: {len(css_content.encode('utf-8'))}\r\n"
                    "Connection: close\r\n"
                    "\r\n"
                )
                full_response = response_headers + css_content
                conn.sendall(full_response.encode('utf-8'))

            if path == '/scripts/isValidCountryName.js': 
                with open('scripts/isValidCountryName.js', 'r', encoding='utf-8') as f:
                    css_content = f.read()
                response_headers = (
                    "HTTP/1.1 200 OK\r\n"
                    "Content-Type: text/javascript; charset=UTF-8\r\n"
                    f"Content-Length: {len(css_content.encode('utf-8'))}\r\n"
                    "Connection: close\r\n"
                    "\r\n"
                )
                full_response = response_headers + css_content
                conn.sendall(full_response.encode('utf-8'))

            if path == '/scripts/script.js': 
                with open('scripts/script.js', 'r', encoding='utf-8') as f:
                    css_content = f.read()
                response_headers = (
                    "HTTP/1.1 200 OK\r\n"
                    "Content-Type: text/javascript; charset=UTF-8\r\n"
                    f"Content-Length: {len(css_content.encode('utf-8'))}\r\n"
                    "Connection: close\r\n"
                    "\r\n"
                )
                full_response = response_headers + css_content
                conn.sendall(full_response.encode('utf-8'))



            else:
                response_body = '<h1>Not Found</h1>'
                response_headers = (
                    "HTTP/1.1 404 Not Found\r\n"
                    "Content-Type: text/html; charset=UTF-8\r\n"
                    f"Content-Length: {len(response_body.encode('utf-8'))}\r\n"
                    "Connection: close\r\n"
                    "\r\n"
                )
                full_response = response_headers + response_body
                conn.sendall(full_response.encode('utf-8'))


