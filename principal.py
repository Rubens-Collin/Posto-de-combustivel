from bd import *
from admin import *
from atendimento import *

print("$$$ Bem-vindo ao Posto de Combustível LEGAL!! $$$\n")

print("""Escolha o seu usuário:
1. Administrador
2. Atendente""")
while True:

    opcao = leia_int("Digite a sua escolha: ")
    if opcao == 1:
        print('A senha é 1234')
        while True:
            senha = leia_int('Digite a senha do Administrador:')
            if senha == 1234:
                imprimir_tanques_combustivel = Tanque_combustivel()
                adicionar_combustivel = Administrador()
                imprimir_tanques_combustivel.consulatar_combustiveis()
                adicionar_combustivel.adicionar_combustivel()
                break
            else:
                print('Senha invalida. Digite novamente...')
        break


    if opcao == 2:
        atendimento = Atendimento()
        atendimento.abastecer()
        break

    else:
        print("Escolha invalida. Digite novamente...")

#Essa função trata o erro se o usuário digitar algo alem de números
def leia_int(mensagem):
    while True:
        try:
            n = int(input(mensagem))
        except (TypeError, ValueError):
            print('O programa só aceita números e do tipo inteiro. ')
            continue

        else:
            return n
