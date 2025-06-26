class pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    
    
    @classmethod
    def criar_De_data_Nascimento(cls,ano, mes, dia,nome):
        idade = 2023 - ano
        return cls ( nome, idade)
    
    @staticmethod
    def maior_idade(idade):
        return idade >= 18


p = pessoa.criar_De_data_Nascimento(2000, 1, 1, "João")    
print(p.nome, p.idade)  # Output: João 23      

print( pessoa.maior_idade(18))  # Output: True, since 23 >= 18
print (pessoa.maior_idade(8))

