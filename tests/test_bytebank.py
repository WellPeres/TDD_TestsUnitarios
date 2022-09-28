from os import lseek
from codigo.bytebank import Funcionario

class TestClass:
    def test_quando_idade_recebe_13_03_2000_deve_retornar_22(self):
        # Given-Contexto
        entrada = '13/03/2000'
        esperado = 22
        
        funcionario_teste = Funcionario('Teste', entrada, 1111 )
        #When-Ação
        resultado = funcionario_teste.idade()
        
        #Then-Desfecho
        assert resultado == esperado
        
    def test_quando_sobrenome_recebe_Lucas_Carvalho_deve_retornar_apenas_Carvalho(self):
        #Give-Contexto
        entrada = 'Lucas Carvalho'
        esperado = "Carvalho"
        
        #When-Ação
        lucas = Funcionario(entrada, '11/11/2000', 1111)
        resultado = lucas.sobrenome()
        
        assert resultado == esperado