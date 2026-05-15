from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Permite que o Frontend acesse a API

# Simulação de usuários (em um sistema real, use um banco de dados)
users = {
    "admin@teste.com": "1234",
    "usuario@teste.com": "123456",
    "daniel@gmail.com": "1234"
}

@app.route('/login', methods=['POST'])
def verificar_login():
    data = request.get_json()
    email = data.get('email')
    senha = data.get('senha')

    print(f"Tentativa de login: {email}")

    if email in users and users[email] == senha:
        return jsonify({"mensagem": "Login realizado com sucesso!"}), 200
    else:
        return jsonify({"mensagem": "E-mail ou senha inválidos."}), 401

if __name__ == '__main__':
    app.run(port=5000, debug=True)