from flask import Flask, jsonify, request
from dotenv import load_dotenv

from functions_jwt import write_token_with_expire_time


load_dotenv()

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index(): 
    print(write_token_with_expire_time({"nombre":"luis", "edad":22}))
    return jsonify({"message": "Welcome"})

if __name__ == '__main__': 

    ## 0.0.0.0 - app funciona en todas las interfases de la red
    app.run(debug=True, host='0.0.0.0')