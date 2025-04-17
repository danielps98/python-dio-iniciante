# start = 0
# end = 6
# step = 1
# fatiamento de strings


#índice:   0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22
#texto :   d a n i e l   p e r  e  i  r  a     d  a     s  i  l  v  a
nome = "daniel pereira da silva"
nome[0]
# nome[0] == 'd'

nome[0:6]
# nome[0:6] == 'daniel'porque comeca em 0 e vai até 6-1 
# ou seja, 0, 1, 2, 3, 4, 5
# nome[0:6] == 'daniel'

print (nome) # 'daniel'

nome[10:15]
# nome[10:15] == 'eira' porque comeca em 10 e vai até 15-1

nome [10:15:2]
# nome [10:15:2] == 'er' porque comeca em 10 e vai até 15-1 pulando de 2 em 2

nome[:]
# nome[:] == 'daniel pereira da silva' ele vai me retornar a string inteira 

nome[::-1]
#este comando inverte a string, ou seja, ele vai do final para o começo	
# nome[::-1] == 'avlis ad ariepe lianed'
# ele vai me retornar a string inteira invertida


print(nome[10:15:2]) # 'er'
print(nome[10:15]) # 'eira'
print(nome[0:6]) # 'daniel'