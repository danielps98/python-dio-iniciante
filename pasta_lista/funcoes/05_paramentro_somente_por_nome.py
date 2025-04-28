# chamado modelo ibrido


def criar_carro(
    modelo, ano, placa, /, *, marca, motor, combustivel
):  # positonal , /, e o keyworld ,*,
    print(modelo, ano, placa, marca, motor, combustivel)


criar_carro( "palio",2020, "ABC-1234", marca="Volkswagen",motor="1.0",combustivel="Gasolina",) # valido


criar_carro(
    modelo="palio",ano=2020,placa="ABC-1234",marca="Volkswagen",motor="1.0", combustivel="Gasolina",  # invalido pois os primerio parametro nao e obrigatio passar modelo
    # ano e placa
)
