# A forma mais comum de iterar um dicionário é com o for
# Aqui, vamos acessar as chaves e usar essas chaves para pegar os valores

# dicionario podem armazenar qualquer  tipo de objetos python como valor, desde que a chave para esse valor seja um objeto imutavel (como uma string, um número ou uma tupla). Isso significa que você pode usar dicionarios para armazenar listas, conjuntos, dicionarios aninhados e outros tipos de objetos como valores. No entanto, as chaves devem ser objetos imutáveis.

contatos = {
    "danielpds@gmail.com": {"nome": "Daniel", "telefone": "11980311529"},
    "giovanalpds@gmail.com": {"nome": "giovana ", "telefone": "11965311529"},
    "chappiepds@gmail.com": {"nome": "chappie", "telefone": "11980311529"},
    "melainepds@gmail.com": {
        "nome": "melaine",
        "telefone": "11980311529",
        "extra": {"a": 1},
    },
}

telefone = contatos["danielpds@gmail.com"]["telefone"]
print(telefone)

extra = contatos["melainepds@gmail.com"]["extra"]["a"]
print(extra) 


for chave in contatos:
    print(chave, contatos[chave])  # imprime a chave e o valor associado a ela

# Outra forma é usando o método .items(), que retorna chave e valor ao mesmo tempo

for chave, valor in contatos.items():
    print(chave, valor)  # imprime a chave e o valor diretamente
