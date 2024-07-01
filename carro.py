class Carro():
    portas = 4
    marca = 'Fiat'
    modelo = 'Uno'
    cor = 'verde'
    motor = 'v12'
    extra = 'escada'
    velocidade = 0

    def dar_partida(self):
        print('sente o ronco do motor!')

    def acelerar(self):
        self.velocidade += 100

    def frear(self):
        self.velocidade -= 100



carro1 = Carro()
carro1.dar_partida()
carro1.acelerar()
carro1.acelerar()
carro1.acelerar()
carro1.acelerar()
carro1.acelerar()
carro1.acelerar()
carro1.acelerar()
carro1.acelerar()
print (carro1.velocidade)
print('olha o pardal')
carro1.frear()
carro1.frear()
carro1.frear()
carro1.frear()
carro1.frear()
print(carro1.velocidade)
print('acelera')
print('velocidade:do som')