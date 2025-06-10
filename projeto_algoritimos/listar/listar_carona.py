import time
import os
def listarCarona(caronas):
    print('\n')
    print('Buscando caronas...'.center(50))
    time.sleep(1.5)
    os.system('cls' if os.name == 'nt' else 'clear')

    print('\n')
    print('-'*50)
    print('Lista de caronas disponíveis:'.center(50))
    print('-'*50)

    caronas_verificar = False

    for i in caronas:
        if (i['vagas'] > 0):
            print('\n')
            print(f'Nome do motorista: {i['motorista']}')
            print(f'Origem: {i['origem']}')
            print(f'Destino: {i['destino']}')
            print(f'Data: {i['data']}')
            print(f'Horário: {i['hora']}')
            print(f'Vagas disponíveis: {i['vagas']}')
            print(f'Valor por vaga: R${i['valor']}')
            print('-'*50)
            caronas_verificar = True

    if (not caronas_verificar):
        print('Ainda não tem caronas disponíveis. :(')