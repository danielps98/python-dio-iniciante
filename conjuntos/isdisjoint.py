conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {6,7,8,9}
conjunto_c = {0,1}

conjunto_a.isdisjoint(conjunto_b) # true
conjunto_a.isdisjoint(conjunto_c)  # false

# A operação de disjunção é uma verificação que determina 
# se dois conjuntos não têm elementos em comum. Se os conjuntos A e B
# não compartilham nenhum elemento, então eles são disjuntos.
# Isso é útil para entender a relação entre conjuntos e identificar se eles são independentes entre si.
