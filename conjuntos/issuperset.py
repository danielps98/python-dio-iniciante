conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

conjunto_a.issuperset(conjunto_b)  # false
conjunto_b.issuperset(conjunto_a)  # true


# A operação de superconjunto é uma verificação que determina se um conjunto contém todos os elementos de outro conjunto. Se todos os elementos do conjunto A estão presentes no conjunto B, então A é um superconjunto de B.