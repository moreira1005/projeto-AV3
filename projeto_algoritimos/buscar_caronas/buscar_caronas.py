import os
import time

def buscar_caronas (opcoes_encontradas, caronas, reservas, trajeto):
    opcoes_encontradas.clear()
    print('\n')
    print('Para onde deseja ir? '.center(50))
    print('-'*50)
    origem_busca = input('Digite a origem: ').upper()
    destino_busca = input('Digite o destino: ').upper()
    
    for i in caronas:
        if (i['origem'] == origem_busca and i['destino'] == destino_busca and i['vagas'] > 0):
            opcoes_encontradas.append(i)

    if (len(opcoes_encontradas) == 0):
        print('\nAinda não tem caronas disponíveis para onde você quer ir.')
    else:
        print('\nCaronas encontradas:\n')
        contador = 1
        for i in opcoes_encontradas:
            print(f'{contador} - {i["data"]} às {i["hora"]}')
            print(f'  Motorista: {i["motorista"]}')
            print(f'  Origem: {i["origem"]}')
            print(f'  Destino: {i["destino"]}')
            print(f'  Vagas disponíveis: {i["vagas"]}')
            print(f'  Valor por vaga: R${i["valor"]}')
            print('-'*50)
            contador += 1

        escolha = input('Digite o número da carona que deseja reservar (ou Enter para cancelar): ')

        if (escolha.isdigit()):
            escolha = int(escolha)

            if (escolha >= 1 and escolha <= len(opcoes_encontradas)):
                carona_escolhida = opcoes_encontradas[escolha - 1]
                carona_escolhida['vagas'] -= 1
                reservas.append(carona_escolhida)
                os.system('cls' if os.name == 'nt' else 'clear')
                
                print('\nreservando carona...'.center(50))
                time.sleep(1)
                os.system('cls' if os.name == 'nt' else 'clear')
                
                print('\nCarona reservada com sucesso! :)')

                resposta_ir_agora = input('\nDeseja ir agora? (S/N): ').upper()

                if (resposta_ir_agora == 'S'):
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print('Localizando motorista no mapa...\n')
                    time.sleep(1)

                    for i in trajeto:
                        print(f'\rChegando: {i}' , end='', flush=True)
                        time.sleep(1)

                    print('\n\nMotorista chegou! Boa viagem :)')
                    time.sleep(1.5)
                    os.system('cls' if os.name == 'nt' else 'clear')

                    print('Viagem finalizada.'.center(50))
                    avaliacao = input('\nComo você avalia essa carona de 0 a 5? ')

                    if (avaliacao.replace('.', '', 1).isdigit()):
                        nota = float(avaliacao)
                        
                        if (0 <= nota <= 5):
                            print(f'\nObrigado pela sua avaliação de {nota} estrelas!')
                            
                            comentario = input('Deseja colocar um comentário como avalaiação?(opcional): ')

                            salvar_comentario = input('deseja salvar o comentário como arquivo .txt? (S/N): ').upper()
                            if (salvar_comentario == 'S'):
                                vagas_ocupadas = 1
                                total = float(carona_escolhida['valor']) * vagas_ocupadas
                                
                                with (open('avaliação.txt', 'a', encoding= 'utf-8') as arquivos):
                                    arquivos.write(f'Motorista: {carona_escolhida['motorista']}\n') 
                                    arquivos.write(f'Avaliação: {nota} estrela(s)\n')
                                    arquivos.write(f'Origem: {carona_escolhida['origem']}\n')
                                    arquivos.write(f'Destino: {carona_escolhida['destino']}\n')
                                    arquivos.write(f'Data/Hora: {carona_escolhida['data']},{carona_escolhida['hora']}\n')
                                    arquivos.write(f'Valor : R$ {carona_escolhida['valor']}\n')
                                    arquivos.write(f'Vagas restantes: {carona_escolhida['vagas']}\n')
                                    arquivos.write(f'Total recebido nesta carona: R${total}\n')
                                    if (comentario.strip()):
                                        arquivos.write(f'Comentario: {comentario}\n')
                                    arquivos.write ('-' * 40)
                                print('Avaliação salva com sucesso')
                            else:
                                print('Avaliação não foi salva')
                        else:
                            print('\nAvaliação fora do intervalo válido (0 a 5).')
                    else:
                        print('\nAvaliação inválida. Deve ser um número entre 0 e 5.')

            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print('\nNúmero inválido.')
                
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('\nCancelando reserva...'.center(50))
            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')
            
            print('\nReserva cancelada.')