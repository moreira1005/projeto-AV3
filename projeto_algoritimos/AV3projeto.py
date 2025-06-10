usuarios = []
login = []
caronas = []
reservas = []
opcoes_encontradas = []
trajeto = ['[🚗..........]', '[.🚗.........]', '[..🚗........]', '[...🚗.......]', '[....🚗......]', '[.....🚗.....]', 
           '[......🚗....]', '[.......🚗...]', '[........🚗..]', '[.........🚗.]', '[..........🚗]']
import os
from cadastro import verificacao
from listar import listar_carona
from listar import detalhe_caronas
from listar import caronas_usuario
from listar import listar_usuarios
from login import verificar_login
from buscar_caronas import buscar_caronas
from motorista import cadastro_motorista
from remover_reserva import remover_reserva
from logout import logout

if (os.path.exists ('usuarios_cadastrados.txt')):
    with (open('usuarios_cadastrados.txt', 'r', encoding='utf-8') as usuarios_txt):
        for u in usuarios_txt:
            linhas = u.strip().split(';')
            if (len (linhas) == 3):
                (nome, email, senha) = linhas
                usuarios.append({f'nome: {nome}'
                                 f'email: {email}'
                                 f'senha: {senha}'})
                
if (os.path.exists ('avaliação.txt')):
        if (os.path.exists('avaliacao.txt')):
            with (open('avaliacao.txt', 'r', encoding='utf-8') as relatorio):
                for r in relatorio:
                    linhas2 = r.strip().split(';')
                    if (len(linhas2) == 9):
                        (motorista, origem, destino, data_hora, valor, vagas, nota, total, comentario) = linhas2
                        
                        reservas.append({
                            'motorista': motorista,
                            'avaliacao': f"{nota} estrela(s)",
                            'origem': origem,
                            'destino': destino,
                            'data_hora': data_hora,
                            'valor': f"R$ {valor}",
                            'vagas_restantes': vagas,
                            'total': f"R$ {total}",
                            'comentario': comentario})

while True:

    while True:
        print('\n\n')
        print('-'*50)
        print('Painel de controle!'.center(50))
        print('-'*50)
        print()

        opcao = input('Escolha uma opção: ' \
        '\n1- Cadastro ' \
        '\n2- Lista de usuarios' \
        '\n3- Login' \
        '\n\nEscolha: ')
        os.system('cls' if os.name == 'nt' else 'clear')

        if (opcao == '1'):
            verificacao.verificar_email(usuarios)

        elif (opcao == '2'):
            listar_usuarios.listar_usuarios(usuarios)
            
        elif (opcao == '3'):
            usuario_logado = verificar_login.efetuar_login(usuarios)
            if usuario_logado:
                login.append(usuario_logado)
                break
    
    while True:
        print('\n')
        print('~'*50)
        print('Menu principal'.center(50))
        print('~'*50)
        print('\n')
        print(f'Bem-vindo, {login[-1]['nome']}'.center(50))

        menu_opcao = input('\n\nEscolha uma opção abaixo: ' \
        '\n1 - Cadastro do motorista' \
        '\n2 - Lista de caronas disponíveis' \
        '\n3 - Buscar caronas' \
        '\n4 - Remover reserva' \
        '\n5 - Detalhes da carona' \
        '\n6 - Caronas do usuario' \
        '\n7 - Logout' \
        '\nEscolha: ')
        os.system('cls' if os.name == 'nt' else 'clear')

        if (menu_opcao == '1'):
            cadastro_motorista.cadastro_motorista(caronas,login)

        elif (menu_opcao == '2'):
            listar_carona.listarCarona(caronas)
            
        elif (menu_opcao == '3'):
            buscar_caronas.buscar_caronas(opcoes_encontradas, caronas, reservas, trajeto)

        elif(menu_opcao == '4'):
            remover_reserva.remover_reserva(reservas)
        
        elif(menu_opcao == '5'):
            detalhe_caronas.detalhe_da_carona(caronas, reservas)

        elif (menu_opcao == '6'):
            caronas_usuario.caronas_do_usuario(caronas, login)

        elif (menu_opcao == '7'):
            logout.logout(login)
            break