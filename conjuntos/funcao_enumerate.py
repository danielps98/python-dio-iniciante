#as vezes e necessario saber o indice o objeto dentro
# do laco for para isso podemos usar a funcao enumerate

carros = {"palio", "gol", "celta", "palio" }

for indice, carro in enumerate(carros):
    print(f"{indice} : {carro}")
    
    
   