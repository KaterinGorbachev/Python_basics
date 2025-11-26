import socket, time, re

HOST = 'localhost'
PORT = 65432

###----------------check user data---------------------------------------------
def getUserPswd():
    password = input("Enter password: ").strip()
    allowed_specials = "!@#$%^&*()_+-=[]{};:,.?/"
    
    if len(password) < 8:
        return False, "Password must be at least 8 characters long."
    if not re.search(r"[A-Z]", password):
        return False, "Password must contain at least one uppercase letter."
    if not re.search(r"[a-z]", password):
        return False, "Password must contain at least one lowercase letter."
    if not re.search(r"[0-9]", password):
        return False, "Password must contain at least one number."
    if not re.search(rf"[{re.escape(allowed_specials)}]", password):
        return False, "Password must contain at least one special character."

    
    if re.search(r"[`~'\"\\|<> \t]", password):
        return False, "Password must not contain [`~'\"\\|<> \t] characters."

    return True, password

def isIntegerId(id): 
    try: 
        test = int(id)
        return True, id
    
    except Exception as e: 
        return False, 'ID incorrecto: introduce integer entre 1 y 10'   

def isNotEmpty(data: str): 
    data = data.strip()
    if data == '':
        return None
    return data
    
# HTML5 + Django-style regex (safe, practical, not overly strict)
EMAIL_REGEX = re.compile(
    r"^[A-Za-z0-9.!#$%&'*+/=?^_`{|}~-]+@"
    r"[A-Za-z0-9](?:[A-Za-z0-9-]{0,61}[A-Za-z0-9])?"
    r"(?:\.[A-Za-z0-9](?:[A-Za-z0-9-]{0,61}[A-Za-z0-9])?)+$"
)

def is_valid_email(email: str) -> tuple:
    """Validate email using best practices.
    - Reject empty string
    - Strip whitespace
    - Use widely accepted email regex (HTML5/Django style)
    """
    if not email:
        return False, 'El email introducido no es válido. Debe tener un formato como "usuario@dominio.com" y no está vacío'

    email = email.strip()
    if email == "":
        return False, 'El email está vacío'
    
    if EMAIL_REGEX.match(email) is None: 
        
        return False, 'El email introducido no es válido. Debe tener un formato como "usuario@dominio.com" y no está vacío'

    return True, email
        

###------------functions for client socket-----------------
def send_line(file, text):
    file.write(text + "\n")
    file.flush()

def read_line(file):
    """Reads a line and strips newline safely."""
    line = file.readline()
    return line.rstrip('\n') if line else None

###----------menu--------------------------------------------
def menu_not_logged():
    print("""
        ------  MENU  -------
          1: Registrarse
          2: Iniciar sesión
          3: Salir
    """)
    return input("Pulsa 1, 2 o 3: ").strip()

def menu_logged():
    print("""
        ------  MENU USUARIO  -------
          1: Consultar personaje por ID
          2: Buscar personajes por especie
          3: Cerrar sesión
          4: Salir
    """)
    return input("Pulsa 1, 2, 3 o 4: ").strip()

###-----------register user--------------
def client_register(file):
    send_line(file, "registrar")
    answer = read_line(file)
    if answer != '200': 
        print('\n>>> Servidor error: answer')
        return 
    email = input("Introduce email: ")
    valid, valid_email = is_valid_email(email)
    while not valid: 
        print(valid_email)
        email = input("Introduce email: ")
        valid, valid_email = is_valid_email(email)

    if valid:     
        send_line(file, valid_email)
        answer = read_line(file)
        if answer !='200': 
            print("\n>>> Servidor:", answer)
            return
        else:     
            is_correct_pswd, password = getUserPswd()
            while not is_correct_pswd: 
                print(password)
                is_correct_pswd, password = getUserPswd()

            if is_correct_pswd: 

                send_line(file, password)
                answer = read_line(file)
                print("\n>>> Servidor:", answer)
     
        

###------------login user-----------------------------
def client_login(file):
    send_line(file, "login")

    email = input("Introduce email: ")
    send_line(file, email)

    answer = read_line(file)
    if answer != '200': 
        print(answer)
        return

    password = input("Introduce password: ")
    send_line(file, password)

    first_line = read_line(file)
    print("\n>>> Servidor:", first_line)

    if first_line == "session":
        token = read_line(file)
        print("Token recibido:", token)
        return token

    return None

###---------------logged in users actions--------------------------
def action_id(file, token):
    """User must send their token first."""
    send_line(file, 'token')
    send_line(file, token)
    answer = read_line(file)
    if answer != '200': 
        print("\n>>> Servidor:", answer)
        return
    else: 

        send_line(file, "id")
        rid = input("Introduce ID: ")
        valid, message = isIntegerId(rid)
        while not valid: 
            print(message)
            rid = input("Introduce ID: ")
            valid, message = isIntegerId(rid)

        if valid: 
            send_line(file, rid)
            answer = read_line(file)
            print("\n>>> Servidor:", answer)
        



def action_especie(file, token):
    """User must send their token first."""
    send_line(file, 'token')
    send_line(file, token)
    answer = read_line(file)
    if answer != '200OK': 
        print("\n>>> Servidor:", answer)
        return
    else: 
        send_line(file, "especie")
        especie = isNotEmpty(input("Introduce especie: "))
        while especie is None: 
            print('Has olvidado escribir algo')
            especie = isNotEmpty(input("Introduce especie: "))

        send_line(file, especie)
        answer = read_line(file)
        print("\n>>> Servidor:", answer)






###-------------Client socket---------------------------------------------------

# creating a TCP socket connection to a server running on 'localhost'
# at port 65432 using the `socket` module in Python. 
# token for logged users starts with None

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client: 
    client.connect((HOST, PORT))
    file = client.makefile('rw')
    token = None
    salir = False

    while not salir: 

        # --- FIRST MENU (not logged) ---
        while not token and not salir:
            option = menu_not_logged()
            if option == "1":
                client_register(file)

            elif option == "2":
                token = client_login(file)

            elif option == "3":
                send_line(file, "salir")
                salir = True
                file.close()
                client.close()
                break

            else:
                print("Opción incorrecta")

        
        # --- SECOND MENU (logged in user) ---
        logout = False
        while token and not logout:
            option = menu_logged()

            if option == "1":
                action_id(file, token)

            elif option == "2":
                action_especie(file, token)

            elif option == "3":
                print("Cerrando sesión…")
                
                token = None
                logout = True
                
                break
                
                
            elif option == "4":
                send_line(file, "salir")
                print("Saliendo…")
                logout = True
                salir = True
                file.close()       # closes file wrapper
                client.close()     # closes socket
                exit()

            else:
                print("Opción incorrecta")



    



