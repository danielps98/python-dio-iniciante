class cachorro:
    def __init__(self, nome, cor, acordado=True):
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def latir(self):
        return f"{self.nome} está latindo!"

    def info(self):
        return f"Nome: {self.nome}, Idade: {self.idade} anos"
    
    