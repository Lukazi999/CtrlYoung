class Onintorinco():
    animal = 'Onintorinco'
    reino = 'Animalia'
    filo = 'Chordata'
    classe = 'Mammalia'
    ordem = 'Monotremata'
    familia = 'Ornithorhynchidae'
    genero = 'Ornithorhynchus'
    especie = 'Ornithorhynchus anatinus'
    def __init__ (self, animal, classe):
        self.animal = animal
        self.classe = classe
    
    def __str__(self):
        return f'Este é um {self.animal} da classe {self.classe}'

    def comer(self): 
        print('comeu um peixe')

    def cacou(self):
        print('matou um peixe')

    def botou_um_ovo(self):
        print('pam pam pam pam colocou uma nova vida no mundo Parabéns pelo ovo')

onintorinco1 = Onintorinco('onintorinco', 'mamalia')
onintorinco1.cacou()
onintorinco1.comer()
onintorinco1.botou_um_ovo()
print (onintorinco1)