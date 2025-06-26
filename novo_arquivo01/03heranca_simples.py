class Veiculo:
    def __init__(self, cor, placa, numero_de_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_de_rodas = numero_de_rodas

    def ligar_motor(self):
        print("Motor ligado")

    def desligar_motor(self):
        print("Motor desligado")


def __str__(self):
    return self.cor

class Motocicleta(Veiculo):
    pass  # herda tudo da classe Veiculo


class Carro(Veiculo):
    pass  # também herda tudo de Veiculo


class Caminhao(Veiculo):
    def __init__(self, cor, placa, numero_de_rodas, carregado):
        super().__init__(
            cor, placa, numero_de_rodas
        )  # chama o construtor da classe-pai (Veiculo)
        self.carregado = carregado
    super().__init__(cor, placa, numero_de_rodas)

    def esta_carregado(self):
        print(f"{'Sim' if self.carregado else 'Não'} estou carregado")


# Criando uma motocicleta
moto = Motocicleta("preta", "ABC-1234", 2)
moto.ligar_motor()
moto.desligar_motor()

# Criando um carro
carro = Carro("vermelho", "DAN-8031", 4)
carro.ligar_motor()
carro.desligar_motor()

# Criando um caminhão
caminhao = Caminhao("azul", "AFF-1534", 6, True)
caminhao.ligar_motor()
caminhao.esta_carregado()
