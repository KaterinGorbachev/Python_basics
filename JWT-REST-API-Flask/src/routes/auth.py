from flask import Blueprint, request, jsonify
from functions_jwt import write_token_with_expire_time, validate_token

## thunderclient simulate user

routes_auth = Blueprint('routes_auth', __name__)

@routes_auth.route('/login', methods=['POST'])
def login(): 

    ## 415 si no pasas json
    data = request.get_json()

    # DEBERIAMOS HACER LA LOGICA DE LA BASE DE DATOS PARA VALIDAR EL USUARIO
    if data['username'] == 'Bender' and data['password'] == 'bender': 

        data['id'] = 7   # mejor crear objeto nuevo con campos de usuario que necesites y pasar lo a write_token

        return write_token_with_expire_time(data)
    
    else: 
        response = jsonify({"message": "User not found"})
        response.status_code = 404 

        return response
    

## ruta para valiadr este token
@routes_auth.route('/validate/token')
def verify_token(): 
    # Postman - Authorization bearear token  - add token before request Get eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6IkJlbmRlciIsInBhc3N3b3JkIjoiYmVuZGVyIiwiaWQiOjcsImV4cCI6MTc2OTUwNzU3MH0.o1Pap19k6uNF_TmL01oghYyaehgWv6QU0m30q_ijyzc

    token = request.headers['Authorization'].split()[1]
        
    return validate_token(token, output=True)


