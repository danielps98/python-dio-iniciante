contatos = {
    "danielpds@gmail.com": {"nome": "Daniel", "telefone": "11980311529"},
    
}

copia = contatos.copy()  # Faz uma cópia rasa do dicionário
copia ["danielpdsnpk@gmail,com"] = {"nome": "dan", "tel": "11980311529"}
print(copia)  

contatos ["danielpds@gmail.com"] #{"nome": "Daniel", "telefone": "11980311529"}

copia ["danielpdsnpk@gmail,com"] #{"nome": "daniel", "telefone": "11980311529"}