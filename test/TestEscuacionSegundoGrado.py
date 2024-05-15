import unittest
from src.logica.EcuacionSegundoGrado import EcuacionSegundoGrado

class TestEcuacionSegundoGrado(unittest.TestCase):
    def setUp(self):
        self.calculoRaices = EcuacionSegundoGrado()

        def tearDown(self):
            self.calculoRaices = None
    def test_CalculoESG_dosNumeros_Solucion(self):
        # Arrange
         a= 1
         b= 2
         c= 1
        resultadoEsperadoRaiz1 = -1
        resultadoEsperadoRaiz2 = -1
        # DO
        resultadoActualRaiz1, resultadoActualRaiz2 = self.calculoRaices.Sa,b,c)

        #Assert
        self.assertEqual(resultadoEsperadoRaiz1,resultadoActualRaiz1Raiz2)
        self.assertEqual(resultadoEsperadoRaiz1, resultadoActualRaiz2)



        #self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
