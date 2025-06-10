import os
import time

def efetuar_login (usuarios):
    print()
    print('~' * 50)
    print('Faça seu login!'.center(50))
    print()

    login_email = input('Digite seu email: ')
    login_senha = input('Digite sua senha: ')

    for i in usuarios:
        if login_email == i['email'] and login_senha == i['senha']:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('\nLogin efetuado com sucesso!')
            time.sleep(0.85)
            os.system('cls' if os.name == 'nt' else 'clear')
            return i
        
    os.system('cls' if os.name == 'nt' else 'clear')
    print('\nEsse usuário não existe ou a senha está incorreta. Tente novamente!')
    return None