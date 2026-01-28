from os import getenv
from jwt import encode, decode, exceptions
from flask import jsonify

from datetime import datetime, timezone, timedelta

###
# documentacion https://pyjwt.readthedocs.io/en/stable/
# check token https://www.jwt.io/    -->> pasar sin b y sin ': 
# eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJub21icmUiOiJsdWlzIiwiZWRhZCI6MjIsImV4cCI6MTc2OTUwMjQ4NH0.aRpYlFg7SVw6TUh9Tvfo6mraSR4IkcFrAuuQpKtJvFE
###


def write_token(data:dict): 

    ## un token para siempre
    token = encode(payload={**data}, key=getenv('SECRET'), algorithm='HS256')

    return token.encode('UTF-8')


def write_token_with_expire_time(data:dict): 

    ## https://pyjwt.readthedocs.io/en/stable/usage.html#registered-claim-names

    # days=1, microseconds=0.000011, weeks=45

    token = encode(payload={**data, 'exp':datetime.now(tz=timezone.utc) + timedelta(minutes=30)}, key=getenv('SECRET'), algorithm='HS256')

    return token.encode('UTF-8')


## to pass jwt to, before route
# check si expired
# check si es valid
## NO HAY FORMA DE INVALIDAR TOKEN ->> SOLO PONER EN BLACK LIST EN DB
def validate_token(token, output=False): 
    try: 
        ### VERIFICAR EN DB BLACKLIST Y CAMBIAR OUTPUT A TRUE OR FALSE
        if output: 
            # puede pasar diferentes algoitmos decodifacion para que ententare usar los
            return decode(token, key=getenv('SECRET'), algorithms=['HS256'])
        
        # fuera de if - decodificar para manejar errores 
        decode(token, key=getenv('SECRET'), algorithms=['HS256'])

    except exceptions.DecodeError as e : 
        # no es valido token
        response = jsonify({"message": "Invalid Token"})
        response.status_code = 401

        return response
    
    except exceptions.ExpiredSignatureError as e: 
        # token expired -> en app.py deside what to do next
        response = jsonify({"message": "Token Expired"})
        response.status_code = 401
        ## si no hay access a admin - 403 forbiden
        ## claims NO public no puedes verificar con exeptions 
        ## https://datatracker.ietf.org/doc/html/rfc7519#section-4.2

        return response



