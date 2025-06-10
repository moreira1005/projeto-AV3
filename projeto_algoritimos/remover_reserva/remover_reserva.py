import os
import time

def remover_reserva (reservas):
    print('\n')
    print('Qual reversa deseja remover?')
    
    contador_cancelar = 1

    for i in reservas:
        print(f'{contador_cancelar} - {i['data']} às {i['hora']}')
        print(f'  Motorista: {i['motorista']}')
        print(f'  Origem: {i['origem']}')
        print(f'  Destino: {i['destino']}')
        print(f'  Vagas disponíveis: {i['vagas']}')
        print(f'  Valor por vaga: R${i['valor']}')
        print('-'*50)
        
        contador_cancelar += 1

    escolha_cancelar = input('Digite o numero da reverva que deseja remover: ')
    
    if(escolha_cancelar.isdigit()):
        escolha_cancelar = int(escolha_cancelar)

    if (escolha_cancelar >= 1 and escolha_cancelar <= len(reservas)):
        confirmacao = input('Tem certeza que deseja remover? (S/N): ').lower()
        
        if (confirmacao == 's'):
            reserva_cancelar = reservas[escolha_cancelar - 1]
            reserva_cancelar['vagas'] += 1
            reservas.pop(escolha_cancelar - 1)
            
            os.system('cls' if os.name == 'nt' else 'clear')
            print('Removendo reserva...'.center(50))
            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')
            
            print('~'*50)
            print('\nReserva Removida com sucesso!'.center(50))
        
        elif(confirmacao == 'n'):
            os.system('cls' if os.name == 'nt' else 'clear')
            print('~'*50)
            print('\nProcesso cancelado!'.center(50))

        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('~'*50)
            print('\nResposta inválida...'.center(50))

    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('~'*50)
        print('\nNúmero inválido.'.center(50))