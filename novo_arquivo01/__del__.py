class cachorro:

    def __init__(self, nome, cor, acordado=True):
        print("INICIALIZANDO CLASSE")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def __del__(self):
        print(f"Despedindo-se de ..")
        print("Adeus!")

    def falar(self):
        print( " está falando!")

    def criar_cachorro():
        c = cachorro("Rex", "preto",False)
        print(c.nome, c.cor, c.acordado)  # Acessando os atributos do objeto criado

# c = cachorro( "Rex", "preto")
# Isso chamará o método __del__ e imprimirá a mensagem de despedida.
# c.falar()  # Isso não funcionará, pois o objeto c foi deletado e não existe mais

