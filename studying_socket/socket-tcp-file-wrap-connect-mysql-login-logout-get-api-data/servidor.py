import socket, logging, mysql.connector, requests, hashlib, json

# The lines `HOST = 'localhost'` and `PORT = 65432` are setting up the host and port for a socket
# connection.
HOST = 'localhost'
PORT = 65432

###-------------hash password ------------
def hash_password(password): 
    """
    The above Python functions are used for hashing a password and checking if a password matches a
    stored hash.
    
    :param password: The `password` parameter is a string that represents the user's password
    :return: The `hash_password` function returns the SHA-256 hash of the input password as a
    hexadecimal string. The `check_password` function compares the hash of the input password with a
    stored hash and returns `True` if they match, indicating that the password is correct, and `False`
    otherwise.
    """
    return hashlib.sha256(password.encode()).hexdigest()

def check_password(password, stored_hash): 
    return hash_password(password) == stored_hash

###--------------loggers-----------------------
# The code `logger = logging.getLogger(__name)` is creating a logger object named `logger` using the
# `logging` module in Python. The `__name__` variable refers to the name of the current module. By
# using this, each module can have its own logger with a unique name.
logger = logging.getLogger(__name__)
logger.setLevel('DEBUG')

###--------------------------------
def formatLoggs(): 
    """
    The function `formatLoggs` returns a logging formatter that includes the timestamp, log level, and
    message.
    """
    return logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

###-----------------------

def consoleLogger(logger): 
    """ Setting up a console handler for logging in Python. 
    :param logger: The `logger` parameter in the `infoLogger` function is an instance of the
    `logging.Logger` class from the Python `logging` module. It is used to configure and manage logging
    in your Python application""" 
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatLoggs())
    console_handler.setLevel('DEBUG')
    logger.addHandler(console_handler)

# Setting up a console handler for logging. 
consoleLogger(logger)

###-----------------------
def infoLogger(logger): 
    """
    The `infoLogger` function adds an INFO level file handler to a logger object.
    :param logger: The `logger` parameter in the `infoLogger` function is an instance of the
    `logging.Logger` class from the Python `logging` module. It is used to configure and manage logging
    in your Python application
    """
    info_handler = logging.FileHandler('access.log', 'a', encoding='utf-8')
    info_handler.setFormatter(formatLoggs())
    info_handler.setLevel('INFO')
    logger.addHandler(info_handler)

# Setting up a file handler for INFO level logging in Python.
infoLogger(logger)

###--------------------------
def errorLogger(logger): 
    """
    The `errorLogger` function adds an ERROR level file handler to a logger object.
    :param logger: The `logger` parameter in the `infoLogger` function is an instance of the
    `logging.Logger` class from the Python `logging` module. It is used to configure and manage logging
    in your Python application
    """
    error_handler = logging.FileHandler('errors.log', 'a', encoding='utf-8')
    error_handler.setFormatter(formatLoggs())
    error_handler.setLevel('ERROR')
    logger.addHandler(error_handler)

# Setting up a file handler for ERROR level logging in Python.
errorLogger(logger)

###-----------------functions for data base-----------------------
def connectDB(logger):
    """ Establish a connection to a MySQL database using the `mysql.connector` library. """
    try: 
        connection = mysql.connector.connect(
            user='', 
            password='',
            host='localhost',
            database='examen_users'

        )

        return connection

    except Exception as e: 
        
        logger.error(f'Error de conexion de DB: {e}')
        return None
    
def closeDB(conex, logger):
    """ Close a connection to a MySQL database using the `mysql.connector` library. """
    if conex: 
        conex.close()

    if not conex.is_connected(): 
        logger.debug('conexion DB cerrado')

def loginDBCheck(conex, logger, data): 
    """
    The `loginDBCheck` function queries a database for a user's password hash based on their email and
    logs relevant information.
    
    :param conex: The `conex` parameter is a database connection object that allows you to
    interact with a database in your code. It is used to establish a connection to the database and
    execute SQL queries. The `conex` parameter is used to create a cursor. 
    :param logger: is an instance of a logging object that is used to
    record events that occur during the execution of a program. 
    :param data: is typically the email address of the user for whom you are trying to retrieve the password hash from the database
    :return: is returning the password hash for the user with the provided email address if the user is found in the database. If the user is not found, it logs an error and returns an empty string. 
    If there is an exception during the database query, it logs an error and returns nothing.
    """
    logger.debug(f'consulta en db para {data}')
    try: 
        mi_cursor = conex.cursor()
        sql = 'SELECT password_hash FROM users WHERE email = %s'
        mi_cursor.execute(sql, (data,))
        row = mi_cursor.fetchone()
        if row is None: 
            logger.error(f'ususario {data} no encontrado')
            return ''
        return row[0]

    except Exception as e: 
        logger.error(f'consulta en db para {data} con error: {e}')

    finally: 
        closeDB(conex, logger)


def registerEnDB(conex, logger, email, password): 
    """
    The function `registerEnDB` registers a user in a database by inserting their email and hashed
    password, logging the process, and handling exceptions.
    
    :param conex: The `conex` parameter is a database connection object that allows you to
    interact with a database from your Python code. 
    :param logger: The `logger` parameter is used for logging messages at various levels of severity in
    your code. It helps in tracking the flow of your program and identifying issues during execution. In
    the provided function `registerEnDB`, the logger is used to record debug, info, and error messages
    related to registering a user.
    :param email: is the email address of the user who is registering in the database
    :param password: is the password that the user wants to register with. This password will be hashed before sending to data base for security reasons.
    :return: returning the string '200OK' if the user registration in the database is successful.
    """
    logger.debug(f'registro en db para {email}:{password}')
    try: 
        password_hash = hash_password(password)
        mi_cursor = conex.cursor()
        sql = ("INSERT INTO users" "(email, password_hash) " "VALUES (%s, %s)")
        mi_cursor.execute(sql, (email,password_hash))
        conex.commit()
        logger.info(f'registro en db para {email}:{password} success')
        return '200OK'

    except Exception as e: 
        logger.error(f'no se pudo registrar usuario {email} con passwrod {password}: {e}')

    finally: 
        closeDB(conex, logger)

def testBD():
    """
    The function `testBD` connects to a database and registers user with test data: an email and password hash.
    """
    conex=connectDB(logger)
    registerEnDB(conex, logger, 'email2@test', 'password_hash_test')

###------------functions for socket-----------------
def read_line(file):
    """Reads a line and strips newline safely."""
    line = file.readline()
    return line.rstrip('\n') if line else None

###-----------registration in db------------------------
def handle_register(file, logger):
    """
    This Python function handles user registration by checking if the user already exists in the
    database, logging relevant information, and writing appropriate messages to a file.
    
    :param file: is used to interact with a socket file  wrapper. It is used for reading and sending data from/to a client socket. 
    :param logger: is used for logging messages at different levels of severity. 
    :return: If the user is already registered, the function will write an error message to the client and
    return without further processing. If the user is not registered, the function will read the
    password from the file, register the user in the database, write a success message to the client, add success info to access.log file and return.
    """
    file.write("200\n")
    file.flush()
    email = read_line(file)
    logger.debug(f'email recibido {email}')

    conex = connectDB(logger)
    is_registered = loginDBCheck(conex, logger, email)

    if is_registered:
        file.write("Error: El usuario ya existe\n")
        file.flush()
        return
    else: 
        file.write('200\n')
        file.flush()
        password = read_line(file)
        logger.debug(f'passwd recibido {password}')
        conex = connectDB(logger)
        registerEnDB(conex, logger, email, password)
        logger.info("Registro completado")
        file.write("Registro completado con exito\n")
        file.flush()


###--------------login------------------------
def handle_login(file, logger):
    """
    The `handle_login` function reads an email and password from a file, checks the password against a
    stored password in a database, and logs the login status.
    
    :param file: is used to interact with a socket file  wrapper. It is used for reading and sending data from/to a client socket. 
    :param logger: is used for logging messages at different levels of severity. 
    :return: if the user is not found or the password is incorrect: loggs an error message in error.log file and write error message to the client socket. If user was found: loggs success in access.log and sends to client socket a success message with a TEST session token.
    """
    email = read_line(file)
    logger.debug(f'email recibido {email}')

    conex = connectDB(logger)
    stored_password = loginDBCheck(conex, logger, email)

    if not stored_password:
        logger.error("usuario no encontrado")
        file.write("Error: Usuario no registrado\n")
        file.flush()
        return
    else: 
        file.write("200\n")
        file.flush()


    password = read_line(file)

    if not check_password(password, stored_password):
        logger.error("Password incorrecto")
        file.write("Error: Password incorrecto\n")
        file.flush()
        return

    # Login OK
    token = "ABC12345"  # Test token
    logger.info("Login correcto")

    file.write("session\n")
    file.flush()
    file.write(token + "\n")
    file.flush()

###-------------------API requets------------------------
def perform_user_action(file, logger):
    """Handles 'id' and 'especie' API requests after login,
    requiring a valid token first.
    """

    # ---- TOKEN CHECK ----
    received_token = read_line(file)
    logger.debug(f"Token recibido: {received_token}")

    
    EXPECTED_TOKEN = "ABC12345" # Test token

    if received_token != EXPECTED_TOKEN:
        logger.error("Token inválido")
        file.write("Error: Token inválido\n")
        file.flush()
        return
    else: 
        file.write('200\n')
        file.flush()


    # ---- NEXT ACTION ----
    request = read_line(file)

    # ----- ID -----
    if request == 'id':
        rid = read_line(file)
        try:
            characters = requests.get(f"https://rickandmortyapi.com/api/character/{int(rid)}")
            data = characters.json()
            response = (
                f"Nombre: {data['name']} "
                f"Estado: {data['status']} "
                f"Especie: {data['species']}"
            )
            file.write(response + "\n")
            file.flush()
        except Exception:
            logger.error("API error")
            file.write("API error\n")
            file.flush()
        return

    # ----- ESPECIE -----
    if request == 'especie':
        especie = read_line(file)
        try:
            characters = requests.get(
                f"https://rickandmortyapi.com/api/character/?species={especie}"
            )
            data = characters.json()

            if "error" in data.keys():
                file.write("No se encontraron personajes para esa especie\n")
                file.flush()
                return

            first_five = data["results"][:5]
            file.write(json.dumps(first_five) + "\n")
            file.flush()

        except Exception:
            logger.error("API error")
            file.write("API error\n")
            file.flush()

    

####--------------SERVER socket part-------------------------------

# setting up a TCP server using the Python `socket` module. It creates a
# socket object `ssock` with the specified address family `AF_INET` and socket type `SOCK_STREAM`. It
# then binds the socket to a specific host and port, listens for incoming connections with a backlog
# of 1, and logs a debug message indicating the start of the server.
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as ssock: 
    ssock.bind((HOST, PORT))
    ssock.listen(1)
    logger.debug('Inicio del servidor')

    # creating a while loop that continuously accepts incoming client connections on
    # a socket named `ssock`. When a client connects, it retrieves the client socket and address
    # information, and then logs a debug message indicating that the client at that address has connected.
    while True: 
        client, addr = ssock.accept()
        logger.debug(f'{addr} conectado')

        # using a `with` statement to work with a client object. It then creates a
        # file object using the `makefile()` method of the client object with read and write permissions.
        with client:
            file = client.makefile('rw')

            # reads message from a client line by line until there
            # are no more lines to read. 
            seguir = True
            while seguir: 
                line = file.readline()
                logger.debug(f'opcion elegida {line}')
                if not line: 
                    break

                # The above Python code is message from a Client socket and checking the content of each message. If the line contains the word 'registrar', it calls the function
                # `handle_register()`. If the line contains 'login', it calls `handle_login()`. If the
                # line contains 'token', it calls `perform_user_action()`. If the line contains
                # 'salir', it logs a message and sets the variable `seguir` to False. The connection will be closed by the Client side. If none of these conditions are met, it writes 'Incorrect request' to the file and sets `seguir` to False.
                if line.rstrip('\n') == 'registrar':                     
                    handle_register(file, logger)
                elif line.rstrip('\n') == 'login':
                    handle_login(file, logger)
                elif line.rstrip('\n') == 'token': 
                    perform_user_action(file, logger)                    
                elif line.rstrip('\n') == 'salir':
                    logger.debug('Cierra session')
                    seguir = False 
                else: 
                    answer = 'Incorrect request\n'
                    file.write(answer)
                    file.flush()
                    seguir = False 

                    
                    

                            








