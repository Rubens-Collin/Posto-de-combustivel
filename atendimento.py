from combustivel import *
from pagamento import *
from time import sleep

class Atendimento:
    def abastecer(self):
        print("\nTipos de COMBUSTÍVEIS disponíveis:")
        print("1. Gasolina")
        print("2. Etanol")
        print("3. Diesel")
        print("0. Encerrar o programa")
        tipo_combustivel = 0

        while tipo_combustivel >= 0 or tipo_combustivel <= 3:

            tipo_combustivel = leia_int("Selecione o tipo de combustível: ")

            if tipo_combustivel == 1:
                combustivel = Gasolina()
                break

            elif tipo_combustivel == 2:
                combustivel = Etanol()
                break

            elif tipo_combustivel == 3:
                combustivel = Diesel()
                break

            elif tipo_combustivel == 0:
                break
            else:
                print("Opção inválida. Digite outro valor")

        if tipo_combustivel != 0:
            valor = leia_float("Digite o valor: ")
            valor_abastecimento = combustivel.calcular_valor_abastecimento(valor)
            print(f"Litros abastecido {valor_abastecimento}L")
            print(f"Total a Pagar: R${valor}\n")
            sleep(1)

            print("Selecione o tipo de PAGAMENTO disponível:")
            print("1. Credito")
            print("2. Debito")
            print("3. Pix")
            print("4. Dinheiro")

            while True:
                opcao = leia_int("Selecione a forma de PAGAMENTO: ")

                if opcao == 1:
                    pagamento = Credito()
                    break
                elif opcao == 2:
                    pagamento = Debito()
                    break
                elif opcao == 3:
                    pagamento = Pix()
                    break
                elif opcao == 4:
                    pagamento = Dinheiro()
                    break
                else:
                    print("Forma de PAGAMENTO invalida. Digite novamente.")
            pagamento.mensagem()
            sleep(2)
            pagamento.confirmacao_pagamento()

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

#Essa função trata o erro se o usuário digitar algo alem de números
def leia_float(mensagem):
    while True:
        try:
            n = float(input(mensagem))
        except (TypeError, ValueError):
            print('O programa só aceita números e do tipo inteiro ou decimais. ')
            continue
        else:
            return n