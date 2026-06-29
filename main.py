from flask import Flask, render_template, request, jsonify, redirect, url_for
import userFunction

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("index.html")


@app.route("/cadastro/cadastroPessoa", methods=["GET", "POST"])
def cadastro_pessoa():
    mensagem = None
    dados = {}  # garante que existe mesmo no GET

    if request.method == "POST":
        dados = request.form.to_dict()  # captura todos os valores enviados

        nome = dados.get("nome", "")
        cpf = dados.get("cpf", "")
        email = dados.get("email", "")
        idade = dados.get("idade", "")
        senha = dados.get("senha", "")

        if not cpf.isdigit() or len(cpf) != 11:
            mensagem = "Erro: CPF deve conter 11 números."
        elif "@" not in email:
            mensagem = "Erro: Email inválido."
        elif not idade.isdigit() or int(idade) <= 0:
            mensagem = "Erro: Idade inválida."
        else:
            mensagem = "Cadastro realizado com sucesso!"
            dados = {}  # limpa os campos quando sucesso
        userFunction.cadastrar(nome, cpf, senha, email, idade)

    return render_template("cadastro/cadastroPessoa.html", mensagem=mensagem, dados=dados)

@app.route("/cadastro/produto", methods=["GET", "POST"])
def cadastro_produto():
    mensagem = None
    dados = {}

    if request.method == "POST":
        dados = request.form.to_dict()
        # aqui você pode validar e salvar os dados no banco
        mensagem = "Produto cadastrado com sucesso!"
        dados = {}  # limpa os campos após sucesso

    return render_template("cadastro/cadastroProduto.html", mensagem=mensagem, dados=dados)

@app.route("/login", methods=["GET", "POST"])
def login():
    mensagem = None
    if request.method == "POST":
        usuario = request.form.get("usuario")
        senha = request.form.get("senha")

        status = userFunction.login(usuario, senha)
        print(usuario, senha)
        if status == True:
            mensagem = "Login realizado com sucesso! - Sucesso"
            return redirect(url_for("home"))
        else:
            mensagem = "Usuário ou senha inválidos. - Erro"

    return render_template("login.html", mensagem=mensagem)
@app.route("/relatorios/produtos", methods=["GET", "POST"])
def lista_produtos():
    produtos = [
        {"nome": "Arroz", "categoria": "alimento", "preco_venda": 25.00, "preco_custo": 18.00, "pis_cofins": "7,6%", "cfop": "5102"},
        {"nome": "Sabonete", "categoria": "higiene", "preco_venda": 5.00, "preco_custo": 3.00, "pis_cofins": "3,65%", "cfop": "5101"},
        {"nome": "Cerveja", "categoria": "bebida", "preco_venda": 8.00, "preco_custo": 5.00, "pis_cofins": "7,6%", "cfop": "5102"},
    ]

    if request.method == "POST":
        nome = request.form.get("nome", "").lower()
        categoria = request.form.get("categoria", "").lower()
        cfop = request.form.get("cfop", "").lower()

        if nome:
            produtos = [p for p in produtos if nome in p["nome"].lower()]
        if categoria:
            produtos = [p for p in produtos if categoria == p["categoria"].lower()]
        if cfop:
            produtos = [p for p in produtos if cfop in p["cfop"].lower()]

    return render_template("relatorios/produtos.html", produtos=produtos)




if __name__ == "__main__":
    app.run(debug=True)
