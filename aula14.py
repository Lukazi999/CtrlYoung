import unittest

class Pokemon: 
   
    def __init__(self, nome, hpmaximo):
        self.nome = nome
        self.hp_maximo = hpmaximo
        self.hp_atual = hpmaximo

    def recebe_dano(self, dano):
        self.hp_atual -= dano
        if self.hp_atual <= 0:
             self.hp_atual = 0
        print(f'{self.nome}foi jogar no fluminense')
    def curar(self, pv):
        self.hp_atual += pv
        if self.hp_atual > self.hp_maximo:
            self.hp_atual = self.hp_maximo
pikachu = Pokemon
    
class PokemonTest(unittest.TestCase):
    def test_recebe_dano(self):
        pikachu = Pokemon('pikachu', 200 )
        pikachu.recebe_dano(50)
        self.assertEqual(self.pokemon.hp_atual)
