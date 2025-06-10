import time
import os

def listar_usuarios(usuarios):
    print('\nLista de usuarios:'.center(50))
    if (len(usuarios) == 0):
        print('*'*50)
        print('Ainda não tem nenhum usuario cadatrado!'.center(50))
        print('*'*50)
    else:
        for i in usuarios:
            print(f'\nNome: {i['nome']}')
            print(f'Email: {i['email']}')
            print('-'*50)