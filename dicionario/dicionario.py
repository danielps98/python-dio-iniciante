pessoa = {"nome": "Lucas", "idade": 25, "cidade": "São Paulo"}  # dicionário original

pessoa = dict (nome="Lucas", idade=25)  # dicionário original

pessoa["telefone"] = "2289-8854"  # adicionando nova chave ao dicionário

print(pessoa)  # imprime o dicionário original
print(pessoa["nome"])  # imprime o valor associado à chave "nome"
print(pessoa["idade"])  # imprime o valor associado à chave "idade"

print(pessoa["telefone"])  # imprime o valor associado à chave "telefone"
