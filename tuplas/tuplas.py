frutas = ("laranaja", "banana", "uva", "manga", "maçã",)
frutas = [0] #--> laranaja
frutas = [1] #--> banana

#indice negativo 
frutas = [-1] #--> maçã
frutas = [-2] #--> manga

letra = tuple("python")
tuple ("python") #--> ('p', 'y', 't', 'h', 'o', 'n')
tuple [2:] #--> ('t', 'h', 'o', 'n')
tuple [:2] #--> ('p', 'y')
tuple [1:3] #--> ('y', 't')
tuple [0:3:2] #--> ('p', 't') 
tuple [::2] #--> ('p', 't', 'o')
tuple [::] #--> ('p', 'y', 't', 'h', 'o', 'n')
tuple [::-1] #--> ('n', 'o', 'h', 't', 'y', 'p')
#--> Inverte a tupla


numeros = tuple([1, 2, 3, 4, 5])


pais = ("Brasil", "Argentina", "Chile", "Paraguai", "Uruguai")

print(f"Frutas: {frutas}")
print(f"Letras: {letra}")
print(f"Números: {numeros}")
print(f"Países: {pais}")

