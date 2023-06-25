import datetime
class Pagamento:
    def __init__(self, tipo_pagamento):
        self.tipo_pagemnto = tipo_pagamento

    def confirmacao_pagamento(self):
        data_hora = datetime.datetime.now()
        print(f"Transação Aprovada: {data_hora.strftime('%d/%m/%Y %H:%M')}")

class Credito(Pagamento):
    def __init__(self):
        super().__init__('Credito')
    def mensagem(self):
        print("Insira o cartão ou aproxime")

class Debito(Pagamento):
    def __init__(self):
        super().__init__('Debito')
    def mensagem(self):
        print("Insira o cartão ou aproxime")

class Pix(Pagamento):
    def __init__(self):
        super().__init__('Pix')
    def mensagem(self):
        print("Envie o PIX para essa chave (11)99501-9006 ou (11)974867749.")

class Dinheiro(Pagamento):
    def __init__(self):
        super().__init__('Dinheiro')

    def mensagem(self):
        print("Dinheiro recebido!")


