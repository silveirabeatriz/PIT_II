from flask import Flask, request, jsonify

app = Flask(_name_)

# Lista para armazenar os usuários cadastrados (simulação de banco de dados)
usuarios = []

# Lista para armazenar os pedidos
pedidos = []

# Rota para cadastro de usuários


@app.route('/cadastro', methods=['POST'])
def cadastrar_usuario():
    dados = request.json
    nome = dados.get('nome')
    email = dados.get('email')
    senha = dados.get('senha')

    # Verifica se todos os campos foram fornecidos
    if nome and email and senha:
        # Verifica se o email já está em uso
        if not any(usuario['email'] == email for usuario in usuarios):
            usuario = {'nome': nome, 'email': email, 'senha': senha}
            usuarios.append(usuario)
            return jsonify({'mensagem': 'Usuário cadastrado com sucesso!'}), 201
        else:
            return jsonify({'mensagem': 'Email já cadastrado!'}), 400
    else:
        return jsonify({'mensagem': 'Todos os campos são obrigatórios!'}), 400

# Rota para login de usuários


@app.route('/login', methods=['POST'])
def fazer_login():
    dados = request.json
    email = dados.get('email')
    senha = dados.get('senha')

    # Verifica se o usuário existe e a senha está correta
    for usuario in usuarios:
        if usuario['email'] == email and usuario['senha'] == senha:
            return jsonify({'mensagem': 'Login bem-sucedido!'}), 200

    return jsonify({'mensagem': 'Credenciais inválidas!'}), 401

# Rota para fazer um pedido


@app.route('/pedido', methods=['POST'])
def fazer_pedido():
    dados = request.json
    usuario_email = dados.get('email')
    itens = dados.get('itens')

    # Verifica se o usuário existe
    if any(usuario['email'] == usuario_email for usuario in usuarios):
        pedido = {'usuario': usuario_email, 'itens': itens}
        pedidos.append(pedido)
        return jsonify({'mensagem': 'Pedido realizado com sucesso!'}), 201
    else:
        return jsonify({'mensagem': 'Usuário não encontrado!'}), 404

# Rota para escolher a forma de pagamento e finalizar o pedido


@app.route('/finalizar_pedido', methods=['POST'])
def finalizar_pedido():
    dados = request.json
    forma_pagamento = dados.get('forma_pagamento')

    if forma_pagamento == 'dinheiro' or forma_pagamento == 'cartao' or forma_pagamento == 'pix':
        return jsonify({'mensagem': f'Pedido finalizado. Forma de pagamento: {forma_pagamento}'}), 200
    else:
        return jsonify({'mensagem': 'Forma de pagamento inválida!'}), 400


if _name_ == '_main_':
    app.run(debug=True)


@app.route('/')
def index():
    return


render_template('index.html')


@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

# Rota para a página de login


@app.route('/login')
def login():
    return render_template('login.html')

# Rota para a página de cardápio


@app.route('/cardapio')
def cardapio():
    return render_template('cardapio.html')

# Rota para a página de bebidas


@app.route('/bebidas')
def bebidas():
    return render_template('bebidas.html')

# Rota para a página de finalização de pedido


@app.route('/finalizacao')
def finalizacao():
    return render_template('finalizacao.html')


if _name_ == '_main_':
    app.run(debug=True)
