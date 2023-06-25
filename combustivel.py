class Combustivel:
    def __init__(self, tipo, preco_litro):
        self.tipo = tipo
        self.preco_litro = preco_litro

    def calcular_valor_abastecimento(self, valor):
        return valor / self.preco_litro


class Gasolina(Combustivel):
    def __init__(self):
        super().__init__("Gasolina", 5.0)
        
class Etanol(Combustivel):
    def __init__(self):
        super().__init__("Etanol", 3.6)
        

class Diesel(Combustivel):
    def __init__(self):
        super().__init__("Diesel", 5.0)
        