# dicionario podem armazenar qualquer  tipo de objetos python como valor, desde que a chave para esse valor seja um objeto imutavel (como uma string, um número ou uma tupla). Isso significa que você pode usar dicionarios para armazenar listas, conjuntos, dicionarios aninhados e outros tipos de objetos como valores. No entanto, as chaves devem ser objetos imutáveis.

contatos = {
        "danielpds@gmail.com": {"nome": "Daniel", "telefone": "11980311529"},
         "giovanalpds@gmail.com": {"nome": "giovana ", "telefone": "11965311529"},
          "chappiepds@gmail.com": {"nome": "chappie", "telefone": "11980311529"},
           "melainepds@gmail.com": {"nome": "melaine", "telefone": "11980311529","extra":{"a":1}},
}

telefone =  contatos ["danielpds@gmail.com"]["telefone"]
print (telefone)

extra = contatos ["melainepds@gmail.com"]["extra"]["a"]
print (extra)