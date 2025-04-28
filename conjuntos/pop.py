numeros = {1, 2, 3, 4, 5, 5, 7, 8, 8, 9, 10, 2, 1, 0 }  # conjunto original


numeros  # {1, 2, 3, 4, 5, 7, 8, 9, 10} # conjunto original (sem duplicatas)

numeros.pop()# 0

numeros.pop() # 1


numeros  # {2, 3, 4, 5, 7, 8, 9, 10} # conjunto atualizado (sem o elemento 1)


print (numeros) # {2, 3, 4, 5, 7, 8, 9, 10} # conjunto atualizado (sem o elemento 1)
print (numeros.pop()) # 2 # remove o elemento 2 do conjunto e retorna o elemento removido
print (numeros) # {3, 4, 5, 7, 8, 9, 10} # conjunto atualizado (sem o elemento 2)
print (numeros.pop()) # 3 # remove o elemento 3 do conjunto e retorna o elemento removido
print (numeros) # {4, 5, 7, 8, 9, 10} # conjunto atualizado (sem o elemento 3)