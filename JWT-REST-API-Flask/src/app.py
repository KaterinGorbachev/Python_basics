from flask import Flask, jsonify, request
from dotenv import load_dotenv
from functions_jwt import write_token_with_expire_time

# import blueprints
from routes.auth import routes_auth
from routes.users_github import users_github

### blue prints 
# https://flask.palletsprojects.com/en/stable/blueprints/
# https://flask.palletsprojects.com/en/stable/tutorial/views/
## create modularisacion
## inside src create routes with file auth.py - rutas para login


load_dotenv()

app = Flask(__name__)

#register blueprint
app.register_blueprint(routes_auth, url_prefix='/api')
app.register_blueprint(users_github)

@app.route('/', methods=['GET'])
def index(): 
    print(write_token_with_expire_time({"nombre":"luis", "edad":22}))
    return jsonify({"message": "Welcome"})


# cambiar contrasena
@app.route('/recet_password/<string:token>')
def recet_password():
    ...
    # validar token 
    # si token es valido -> cambia contrasena
    # en otra ruta por click a cambiar contraseña genera token y rediriga a este pagina

if __name__ == '__main__': 

    ## 0.0.0.0 - app funciona en todas las interfases de la red
    app.run(debug=True, host='0.0.0.0')