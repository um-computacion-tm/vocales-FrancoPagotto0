import unittest

from vocales import contar_vocales


class TestContarVocales(unittest.TestCase):
    def test_nada(self):
        resultado = contar_vocales( "zzz")
        self.assertEqual(resultado, {})

    def test_contar_a(self):
        resultado = contar_vocales( "cas")
        self.assertEqual(resultado, {"a": 1})

    def test_contar_aa(self):
        resultado = contar_vocales( "casa")
        self.assertEqual(resultado, {"a": 2})

    def test_contar_Franco(self):
        resultado = contar_vocales( "Franco")
        self.assertEqual(resultado, {"a": 1 , "o" : 1})
    
    def test_contar_ubuntu(self):
        resultado = contar_vocales( "ubuntu")
        self.assertEqual(resultado, {"u": 3})
    
    def test_contar_redireccionar(self):
        resultado = contar_vocales( "redireccionar")
        self.assertEqual(resultado, {"a": 1 , "e" : 2 ,"i" : 2 ,"o" : 1})
    
    def test_contar_cebolla(self):
        resultado = contar_vocales( "cebolla")
        self.assertEqual(resultado, {"a": 1 , "e" : 1 , "o" : 1})

    
    def test_contar_OSO(self):
        resultado = contar_vocales( "OSO")
        self.assertEqual(resultado, { "o" : 2})    
    
    
    def test_contar_RAMA(self):
        resultado = contar_vocales( "RAMA")
        self.assertEqual(resultado, { "a" : 2})   
    
    def test_contar_REMAR(self):
        resultado = contar_vocales( "REMAR")
        self.assertEqual(resultado, { "a" : 1 ,"e" : 1})   
                         
unittest.main()