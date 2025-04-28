contatos = {
    "danielpdsnpk@gmail.com": {"nome": "daniel", "telefone": "11980311529"}
}

resultado = (contatos.pop("danielpdsnpk@gmail.com")
)  # estou apagando o pop e para remover 

print(resultado) 

resultado = contatos.pop("danielpdsnpk@gmail.com" ,"chave nao encontrada")  # uso essa segunda frase apos a virgula pra não dar erro porque o pop apagou o  chamado la em cima  ou uso {} para nao dar erro e 
#para sobrescrever o valor do dicionario 

print(resultado)  # Retorna uma lista de tuplas (chave, valor) do dicionário