import os
import time
import datetime

def cadastro_motorista (caronas, login):
    email_logado = login[-1]['email']
    ja_cadastrou = False

    for i in caronas:
        if i['email_motorista'] == email_logado:
            ja_cadastrou = True
            break

    if (ja_cadastrou):
        print('\nVocê já cadastrou uma carona como motorista.')
        return
    
    print('\n')
    print('-'*50)
    motorista = input('Digite o nome do motorista: ')
    email_motorista = input('Digite o email: ')
    origem = input('Digite o local de origem: ').upper()
    destino = input('Digite o local do destino: ').upper()
    data = input('Digite a data da carona (dd/mm/aaaa): ')
    hora = input('Digite o horário da carona (hh:mm): ')
    vagas = int(input('Digite a quantidade de vagas: '))
    valor = float(input('Digite o valor da vaga: '))
    
    if (email_motorista != login[-1]['email']):
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Email inválido, deve ser o mesmo do login')
        return

    if (vagas <= 0):
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Quantidade de vagas deve ser um número maior que zero.')
        return

    if (data.count('/') == 2 and hora.count(':') == 1):
        dia, mes, ano = data.split('/')
        h, m = hora.split(':')

        if (dia.isdigit() and mes.isdigit() and ano.isdigit() and h.isdigit() and m.isdigit()):
            dia = int(dia)
            mes = int(mes)
            ano = int(ano)
            h = int(h)
            m = int(m)

            try:
                datetime.datetime(ano, mes, dia, h, m)
            except ValueError:
                os.system('cls' if os.name == 'nt' else 'clear')
                print('\nData ou hora não são válidos!')
                return

            caronas.append({
                'motorista': motorista,
                'email_motorista': email_motorista,
                'origem': origem,
                'destino': destino,
                'data': data,
                'hora': hora,
                'vagas': vagas,
                'valor': valor
            })
            os.system('cls' if os.name == 'nt' else 'clear')
            print('\nCarona cadastrada com sucesso!')
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('\nData ou hora contêm caracteres inválidos!')
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('\nFormato de data ou hora incorreto!')