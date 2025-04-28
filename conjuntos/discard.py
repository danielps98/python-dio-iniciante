numeros = {1, 2, 3, 4, 5 ,5 ,7 ,8 ,8 ,9 ,10 ,2 , 1 } # conjunto original


numeros # {1, 2, 3, 4, 5, 7, 8, 9, 10} # conjunto original (sem duplicatas)

numeros.discard(3)  # remove o elemento 3 do conjunto

numeros.discard(45)# tenta remover o elemento 45 (não existe no conjunto, mas não gera erro)


numeros # {1, 2, 4, 5, 7, 8, 9, 10} # conjunto atualizado (sem o elemento 3)
