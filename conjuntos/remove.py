numeros = {1, 2, 3, 4, 5, 5, 7, 8, 8, 9, 10, 2, 1, 0 ,6}  # conjunto original


numeros  # {1, 2, 3, 4, 5, 7, 8, 9, 10} # conjunto original (sem duplicatas)

numeros.remove(0)  # 0


numeros # {2, 3, 4, 5, 7, 8, 9, 10} # conjunto atualizado (sem o elemento 1)

print (numeros) # {2, 3, 4, 5, 7, 8, 9, 10} # conjunto atualizado (sem o elemento 1)
print (numeros.remove(0)) # 2 # remove o elemento 2 do conjunto e retorna o elemento removido
