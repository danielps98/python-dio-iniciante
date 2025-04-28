def salvar_carro(marca, modelo, ano , placa="ABC-123"):
    
    # Função para salvar os dados do carro
    print(f"Carro salvo: {marca} {modelo} {ano} {placa}")
    
salvar_carro("fiat","palio", ano=1969)  # Chamada com argumentos nomeados
salvar_carro(marca="Fusca", modelo="palio", ano="1999" ,placa = "abc-123")
salvar_carro(**{"marca": "fiat", "modelo": "palio", "ano": 2020})  # Chamada com argumentos nomeados em ordem diferente
