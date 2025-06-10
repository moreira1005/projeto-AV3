import os
import time

def caronas_do_usuario (caronas, login):
    encontrou_carona_usuario = False
    print('Caronas cadatradas pelo seu usuario')
    print('\n')
    login_email = login[-1]['email']

    for i in caronas:
        if (i['email_motorista'] == login_email):  
            print('\n')
            print('~'*50)
            print(f'\nOrigem: {i['origem']}')
            print(f'Destino: {i['destino']}')
            print(f'Data: {i['data']}')
            print(f'Horário: {i['hora']}')
            print(f'Valor por vaga: R${i['valor']}')
            print(f'Vagas restantes: {i['vagas']}')
            encontrou_carona_usuario = True
    
    if(not encontrou_carona_usuario):
        print('='*50)
        print('\nSeu usuario não tem nenhuma carona cadastrada ')