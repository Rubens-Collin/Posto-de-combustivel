class Administrador:
    def adicionar_combustivel(self):
        print("Selecione o TANQUE que você deseja abastecer")
        print("1. Gasolina")
        print("2. Etanol")
        print("3. Diesel")

        while True:

            self.opcao = leia_int("Digite o número do TANQUE: ")

            if self.opcao == 1:
                litros = leia_float("Quantos litros você deseja adicionar no tanque de gasolina? ")
                gasolina = 1000 + litros
                print(f"{litros}L de gasolina adicionado com sucesso!!\n")
                print(f"Qantidade de litros disponíveis no tanque atualizado é :{gasolina}")
                break
            elif self.opcao == 2:
                litros = leia_float("Quantos litros você deseja adicionar no tanque de ETANOL? ")
                etanol = 3500 + litros
                print(f"{litros}L de ETANOL adicionado com sucesso!!\n")
                print(f"Qantidade de litros disponíveis no tanque atualizado é :{etanol}")
                break
            elif self.opcao == 3:
                litros = leia_float("Quantos litros você deseja adicionar no tanque de DIESEL? ")
                diesel = 2000 + litros
                print(f"{litros}L de DIESEL adicionado com sucesso!!\n")
                print(f"Qantidade de litros disponíveis no tanque atualizado é :{diesel}")
                break
            else:
                print("Opção invalida")


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