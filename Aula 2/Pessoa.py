class Pessoa:
    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade

    def get_nome(self):
        return self.__nome
    
    def get_idade(self):
        return self.__idade
    
Pessoa = Pessoa("Ana", 30)
print(Pessoa.get_nome())
print(Pessoa.get_idade())