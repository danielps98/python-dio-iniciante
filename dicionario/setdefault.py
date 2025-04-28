contatos = {"danielpdsnpk@gmail.com": {"nome": "daniel", "telefone": "11980311529"}}

contatos.setdefault("nome", "joao")  # Adiciona a chave "nome" com o valor "daniel" se não existir
print(contatos)  # Exibe o dicionário atualizado

contatos.setdefault("idade", 28)
contatos

print(contatos)  # Exibe o dicionário atualizado
