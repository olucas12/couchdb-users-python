import os
import couchdb
import time
from getpass import getpass
import admin as adm

couch = couchdb.Server(f'http://{adm.user}:{adm.password}@127.0.0.1:5984/')
banco = 'usuarios'

try:
    db = couch[banco]
except:
    db = couch.create(banco)

def alteraSenha():
    os.system('clear')
    print('Alterar Senha')

    username = input('\nDigite o seu login: ')

    if username in db:
        senhaAtual = getpass('Digite sua senha atual: ')
        
        doc = db[username]
        
        if senhaAtual == doc['senha']:
            novaSenhaValida = False
            while not novaSenhaValida:
                novaSenha = getpass('Digite sua nova senha: ')
                confirmaSenha = getpass('Confirme sua nova senha: ')
                
                if novaSenha == confirmaSenha:
                    doc['senha'] = novaSenha
                    db.save(doc)
                    print('Senha alterada com sucesso')
                    novaSenhaValida = True
                    time.sleep(2)
                else:
                    print('As senhas não coincidem. Tente novamente.')
                    time.sleep(2)
        else:
            print('Senha atual incorreta!')
            time.sleep(2)
    else:
        print('Usuário não encontrado')
        time.sleep(2)

def removeUser():
    adminPasswordValida = False

    while adminPasswordValida == False:
        os.system('clear')
        print('Remover Usuário')
        username = input('\nDigite o login para remover: ')
        for id in db:
            if id == username:
                os.system('clear')
                adminPassword = getpass('Digite a senha de administrador: ')
                if adminPassword == adm.password:
                    db.delete(db[username])
                    print('Usuário foi removido')
                    adminPasswordValida = True
                    time.sleep(2)
                else:
                    print('Senha incorreta!')
                    time.sleep(2)
def listaUser():
    i=0
    os.system('clear')
    print('Lista de Usuários')
    for id in db:
        i+=1
        print(f'\n{i}. Nome:  {db[id]["nome"]}\n   Login: {db[id]["username"]}')
    input('')

def cadastrarUser():

    senhaValida = False
    usernameValida = False

    os.system('clear')

    print('Cadastrar Usuário\n')

    while usernameValida == False:
        username = input('Digite o login do usuário: ')
        if username in db:
            print('Usuário já cadastrado!')
            time.sleep(1)
            os.system('clear')
        else:
            usernameValida = True

    nome = input('Digite o nome do usuário: ')

    while senhaValida == False:
        senha = getpass('Digite a senha: ')
        verificaSenha = getpass('Confirme a senha: ')
        if senha == verificaSenha:
            senhaValida = True
        else:
            print('Senha inválida!\nDigite novamente...\n')

    info = {
        "_id": username,
        "username": username,
        "nome": nome,
        "senha": senha
    }

    db.save(info)
    os.system('clear')
    print('Usuário foi cadastrado com sucesso!')
    time.sleep(1)

op=1

while op != 0:
    op=9
    os.system('clear')

    print('Usuários')
    print(f'\n1. Cadastrar Novo Usuário\n2. Listar Usuários\n3. Remover Usuário\n4. Alterar Senha\nSua Opção: ', end='')
    try:
        op = int(input(''))
    except:
        os.system('clear')
        print('Digite um valor válido.')
        time.sleep(1)
    

    match op:
        case 1:
            cadastrarUser()
        case 2:
            listaUser()
        case 3:
            removeUser()
        case 4:
            alteraSenha()
        case _:
            pass