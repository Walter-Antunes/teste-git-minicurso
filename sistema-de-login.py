senha = str(input('Digite a tua senha: '))
for c in range(1, 5):
    if c == 4:
        print('O sistema está bloqueado!')
        break
    print(f'Tentativa {c} de 3.')
    senhaconf = str(input('Confirme a tua senha aqui: '))
    if senhaconf == senha:
        print('Bem vindo!')
        break
    else:
        print('Senha incorreta')
