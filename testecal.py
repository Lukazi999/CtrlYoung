import unittest
from calculadora import Calculadora

class CalculadoraTest(unittest.TestCase):
    def setUp(self):
        self.calculadora = Calculadora()

    def teste_divisao(self):
        val =  self.calculadora.divisao(2, 3)
        self.assertEqual(self.calculadora,val, 2)

    def teste_multiplicacao(self):
        val =  self.calculadora.multiplicacao(self.calculadora,2, 3)
        self.assertEqual(val, 2)

    def teste_subtracao(self):
        val =  self.calculadora.subtracao(self.calculadora,3, 2)
        self.assertEqual(l, 2)

    def teste_soma(self):
        val =  self.calculadora.soma(self.calculadora,2, 3)
        self.assertEqual(val, 2)

unittest.main(argv=[''], exit= False)
