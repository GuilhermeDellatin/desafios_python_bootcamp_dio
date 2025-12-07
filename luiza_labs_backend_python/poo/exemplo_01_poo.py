class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print("Trim trim...")

    def parar(self):
        print("Parando bicicleta...")
        print("Bicicleta parada!")

    def correr(self):
        print("Vrummmm...")

    def trocar_marcha(self, numero_marcha):
        print(f"Marcha trocada para {numero_marcha}")

    # def __str__(self):
    # return f"Bicicleta: cor = {self.cor}, modelo = {self.modelo}, ano = {self.ano}, valor = {self.valor}"

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


bicicleta1 = Bicicleta(cor="Prata", modelo="JNA 1", ano=2001, valor=150)
bicicleta1.buzinar()
bicicleta1.correr()
bicicleta1.parar()
print(bicicleta1.cor, bicicleta1.modelo, bicicleta1.ano, bicicleta1.valor)

# Quando fazemos essa chamada:
# bicicleta1.buzinar é equivalente a Bicicleta.buzinar(bicicleta1)

bicicleta2 = Bicicleta(cor="Verde", modelo="Monark", ano=1995, valor=50)
print(bicicleta2)
