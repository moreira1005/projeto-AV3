import os
def verificar_email(usuarios):
    print('\n\nÁrea do cadastro')
    print('*'*50)
    nome = input('Digite seu nome: ')
    email = input('Digite um email: ')
    email_verificador = False
    for i in usuarios:
        if(email == i['email']):
            email_verificador = True
            break

    if (email_verificador):
        print('\nEste email já pertence a um usuario, tente outro.')

    else:
        if ('@gmail' not in email or not email.endswith('.com') ):
            print('\nEmail inválido')
        else:
            senha = input('Digite uma senha: ')
            usuarios.append({'nome': nome, 
                            'email': email, 
                            'senha': senha
                            })
            
            with(open('usuarios_cadastrados.txt', 'a', encoding='utf-8') as usuarios_txt):
                usuarios_txt.write(f'Nome: {nome}\nEmail: {email}\nSenha: {senha}\n')
            
            os.system('cls' if os.name == 'nt' else 'clear')
            print('\nCadastro efetuado com sucesso!')

