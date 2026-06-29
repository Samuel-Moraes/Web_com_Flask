def cadastrar(nome, cpf, senha, email, idade):
    with open('usuarios.txt', 'w', encoding='utf-8') as arquivo:
        arquivo.write(f"{nome} | {cpf} | {senha} | {email} | {idade} |\n")

def login(usuario, password):
    statusUsuario = 0
    with open('usuarios.txt', 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            try:
                nome, cpf, senha, email, idade = map(str.strip, linha.strip().split("|"))
            except:
                statusUsuario = 0 

            if usuario == nome and password == senha:
                statusUsuario = 1
                break
    arquivo.close()
    return statusUsuario