class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor  # eu mesmo vou guardar a cor
        self.modelo = modelo  # eu mesmo vou guardar o modelo
        self.ano = ano  # eu mesmo vou guardar o ano
        self.valor = valor  # eu mesmo vou guardar o valor
       
       
    def buzinar(self): # argumento opcional metodo tem que ter um argumento
        print("plim plimmmmmmmmm!")
        
    def para(self):
            print("A bicicleta parou!")
            
            
    #def __str__(self):
        #return f"Bicicleta(cor={self.cor}, modelo={self.modelo}, ano={self.ano}, valor={self.valor})"    
   
    def __str__(self):
        return f"{self.__class__.__name__}: {' ,'.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"  ## e para ver o nome da classe


b1 = Bicicleta("preta", "Caloi", 2020, 1000.00)
b1.buzinar()
b1.para()
b1.correr()
print(b1.cor, b1.modelo, b1.ano, b1.valor)

b2 = Bicicleta("azul", "Monark", 2021, 1200.00)
print(b2)










# --------------------------exemplo----------------------------

# nese formato, o __dict__ é um dicionário que contém os atributos e valores da instância da classe. O método join() é usado para criar uma string formatada com os pares chave=valor separados por vírgulas.

#----------------------------------------------------------------
# codigo muito util para fazer representacao de clase
 #def __str__(self):
     # return f"{self.__class__.__name__}: {' ,'.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"  ## e para ver o nome da classe

 