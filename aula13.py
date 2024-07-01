class Animal:  
    def __init__(self):
        print('animal criado')

    def oQueE(self):
        print ('animal')

    def comer(self):
        print ('comendo')

class Abelha(Animal):
    def __init__(self):
        print('abelha criado')

    def oQue(self):
        print('abelha')
    
    def bzz(self):
        print('bzzz')

abelha = Abelha
abelha.comer()
