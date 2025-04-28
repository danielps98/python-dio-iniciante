#para retornar um valor de uma função, utilizamos a palavra reservada return.

def calcular_total(numeros):
    return sum(numeros)  # soma todos os números da lista e retorna o resultado

def retornar_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1
    return antecessor, sucessor  # retorna uma tupla com o antecessor e o sucessor

def func_4():
   print("ola mundo")

print(calcular_total([1, 2, 3, 4, 5])) # soma todos os números da lista e retorna o resultado
print(retornar_antecessor_e_sucessor(10)) # retorna uma tupla com o antecessor e o sucessor
print(func_4()) # retorna None, pois a função não tem um valor de retorno definido

