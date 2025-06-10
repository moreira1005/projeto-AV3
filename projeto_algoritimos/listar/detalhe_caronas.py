import os 
import time

def detalhe_da_carona (caronas, reservas):
    print('\n')
    print('~'*50)
    print('Detalhe de uma carona'.center(50))
    print('~'*50)

    email_motorista2 = input('\nDigite o email do motorista: ')
    data_carona = input('Digite a data da carona (dd/mm/aaaa): ')
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Bucando as caronas...'.center(50))
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')

    print('Carona achadas pelas as informações ditas:')
    print('-'*50)
    print('\n')
    
    encontrou_carona = False
    
    for i in caronas:
        
        if (i['email_motorista'] == email_motorista2 and i['data'] == data_carona):
            print('\nDetalhes da carona:')
            print(f'Origem: {i['origem']}')
            print(f'Destino: {i['destino']}')
            print(f'Data: {i['data']}')
            print(f'Horário: {i['hora']}')
            print(f'Valor por vaga: R${i['valor']}')
            print(f'Vagas restantes: {i['vagas']}')
            
            passageiros = 0
            for r in reservas:
                if (r['email_motorista'] == email_motorista2 and r['data'] == data_carona):
                    passageiros += 1

            print(f'Passageiros: {passageiros}')
            print('-'*50)
            encontrou_carona = True
            break

    if (not encontrou_carona):
        os.system('cls' if os.name == 'nt' else 'clear')
        print('~'*50)
        print('\nNenhuma carona encontrada com esses dados.')