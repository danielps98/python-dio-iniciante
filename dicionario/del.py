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

del contatos ["chappiepds@gmail.com"]["telefone"]  # Remove o telefone do contato
del contatos ["giovanalpds@gmail.com"]

print(contatos)  # Exibe o dicionário atualizado