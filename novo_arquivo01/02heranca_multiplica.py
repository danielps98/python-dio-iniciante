# Classe base
class Animal:
    def __init__(self, nro_patas):
        self.nro_patas = nro_patas  # atributo e definição do construtor


# Classe Mamífero herda de Animal
class Mamifero(Animal):
    def __init__(self, cor_pelo, **kwargs):
        self.cor_pelo = cor_pelo
        super().__init__(**kwargs)


# Classe Ave herda de Animal
class Ave(Animal):
    def __init__(self, cor_bico, **kwargs):
        self.cor_bico = cor_bico
        super().__init__(**kwargs)


# Classe Gato herda de Mamifero
class Gato(Mamifero):
    pass


# Herança múltipla: Mamifero e Ave
class Ornitorrinco(Mamifero, Ave):
    def __init__(self, nro_patas, cor_pelo, cor_bico):
        super().__init__(nro_patas=nro_patas, cor_pelo=cor_pelo)
        self.cor_bico = cor_bico
        

# Criando um gato com 4 patas
gato = Gato("preto", nro_patas=4)
print(" GATO")
print(gato.nro_patas)  # Saída: 4
print(gato.cor_pelo)  # Saída: preto

# Criando um ornitorrinco
ornitorrinco = Ornitorrinco(2, "marrom", "laranja")
print("\n🦫 ORNITORRINCO")
print(ornitorrinco.nro_patas)  # Saída: 2
print(ornitorrinco.cor_pelo)  # Saída: marrom
print(ornitorrinco.cor_bico)  # Saída: laranja

