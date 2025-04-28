fruta = ["laranja ", "banana", "maçã", "uva"]

fruta = []

letra = list("banana")
print(letra)

numero = list(range(1, 10))
print(numero)

carro = ['fusca', 'chevrolete', '42000', '2001' 'Sao paulo',true ]

fruta = ["laranja ", "banana", "maçã", "uva"]
fruta[-1] # "uva"
frutas = [-3] # -3 = banana

matriz = [
    [1, "a", 3],
    ["b", 5, 6],
    [7, 8, "c"]
]

matriz[0] # [1, "a", 3]
matriz[0][1] # "a" a posição 0,1 que selecionei a  coluna 1 da linha 0
matriz[0][-1] # 3
matriz[-1][-1]# "c"


lista = ["p", "y", "t", "h", "o", "n"]

lista[2:]  # "t", "h", "o", "n" ---> 2: se for o numero na frente, ele vai pegar do 2 ate o final
lista[:2]  # ["p","y",]   -->  :2 se estiver sem nada na frente comeca da frente ate o indece
lista[0:3:2]  # ["p", "t"] ---> 0:3:2 comeca do 0 ate o 3 pulando de 2 em 2
lista[:]# ["p", "y", "t", "h", "o", "n"] --->[:] pega tudo
lista[-1]# "n" ---> pega o ultimo elemento da lista
lista[::-1]# ["n", "o", "h", "t", "y", "p"] ---> [::-1] inverte a lista

# a forma mais comum para percorer os dados de uma lista e utilizando o for

carros = ["gol", "volkswagen", "palio", "fiat", "civic", "honda", "corolla", "toyota"]

for carro in carros:
    print(carro)
    
    # as vezes e interessante saber o indice do elemento que esta sendo percorrido, para isso podemos usar a funcao enumerate
    
for indice, carro in enumerate(carros):
    print(indice, carro)
    
    
    # a compreensao de lista e uma forma de criar uma nova lista a partir de uma lista existente, aplicando uma expressao a cada elemento da lista original
    
    #filtro de lista
numeros = [1, 30, 21, 2, 9, 65, 34]
pares = [] 
for numero in numeros:
   if numero % 2 == 0:
     pares.append(numero)
    
print(pares)
# [2, 30, 34]

numeros = [1, 30, 21, 2, 9, 65, 34]
pares = [numero for numero in numeros if numero % 2 == 0]

numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = []
for numero in numeros:
    quadrado.append(numero ** 2)
print(quadrado)

numeros = [1, 30, 21, 2, 9, 65, 34]
quadrados = [numero ** 2 for numero in numeros if numero % 2 == 0]