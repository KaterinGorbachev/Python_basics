#####-------------------------------------
### rutas con acceso si token es valido 
## rutas protegidas
#####-------------------------------------

# request objeto viene con la peticion
from flask import Blueprint, jsonify, request

## cd JWT-REST-API-Flask
# pip install requests - libreria like axios
from requests import get

from functions_jwt import validate_token

users_github = Blueprint('users_github', __name__)

## afecta solo todo que esta dentro blue print
@users_github.before_request
def verify_token_middleware(): 
    token = request.headers['Authorization'].split()[1]
    
    # solo validar y pasar token, no hacer nada mas por eso output is False
    return validate_token(token, output=False)


@users_github.route('/github/users', methods=['POST'])
def get_users_github(): 
    data = request.get_json()
    country = data['country']

    response = get('https://api.github.com/search/users?q=location:{}'.format(country))

    print(response)







