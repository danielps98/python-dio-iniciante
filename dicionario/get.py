contatos = {
    "danielpdsnpk@gmail.com": {"nome": "daniel", "telefone": "11980311529"},
}

contatos ["danielpdsnpk@gmail.com"]

contatos.get("chave")  # Retorna None se a chave não existir
contatos.get("chave",{})
contatos.get("danielpdsnpk@gmail.com", {})  # Retorna "valor padrão" se a chave não existir
