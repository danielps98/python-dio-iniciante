from abc import ABC, abstractmethod
from datetime import datetime
import textwrap


class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)


class PessoaFisica(Cliente):
    def __init__(self, nome, cpf, data_nascimento, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento


class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
            }
        )


class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0.0
        self._numero = numero
        self._cliente = cliente
        self._agencia = "0001"
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, numero, cliente):
        return cls(numero, cliente)

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def historico(self):
        return self._historico

    @property
    def cliente(self):
        return self._cliente

    def sacar(self, valor):
        if valor <= 0:
            print("Valor inválido para saque.")
            return False

        if valor > self._saldo:
            print("Saldo insuficiente para saque.")
            return False

        self._saldo -= valor
        print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
        return True

    def depositar(self, valor):
        if valor <= 0:
            print("Valor inválido para depósito.")
            return False

        self._saldo += valor
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
        return True


class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self._limite = limite
        self._limite_saques = limite_saques

    def sacar(self, valor):
        saques_hoje = [t for t in self.historico.transacoes if t["tipo"] == "Saque"]
        if len(saques_hoje) >= self._limite_saques:
            print("Número máximo de saques diários excedido.")
            return False
        if valor > self._limite:
            print("Valor excede o limite de saque.")
            return False
        return super().sacar(valor)

    def __str__(self):
        return f"Agência: {self.agencia} | Conta: {self.numero} | Titular: {self.cliente.nome}"


class Transacao(ABC):
    @property
    @abstractmethod
    def valor(self):
        pass

    @abstractmethod
    def registrar(self, conta):
        pass


class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        if conta.sacar(self.valor):
            conta.historico.adicionar_transacao(self)


class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        if conta.depositar(self.valor):
            conta.historico.adicionar_transacao(self)


class SistemaBancario:
    def __init__(self):
        self.clientes = []
        self.numero_conta = 1

    def menu(self):
        menu_text = """
        ============ MENU ============
        [1] Criar cliente
        [2] Criar conta
        [3] Depositar
        [4] Sacar
        [5] Extrato
        [6] Listar contas
        [0] Sair
        ==============================
        """
        print(textwrap.dedent(menu_text))

    def buscar_cliente(self, cpf):
        for cliente in self.clientes:
            if cliente.cpf == cpf:
                return cliente
        return None

    def recuperar_conta(self, cliente):
        if cliente.contas:
            return cliente.contas[-1]
        print("Cliente não possui conta.")
        return None

    def criar_cliente(self):
        cpf = input("CPF: ")
        if self.buscar_cliente(cpf):
            print("Cliente já existe!")
            return
        nome = input("Nome: ")
        nascimento = input("Data de nascimento: ")
        endereco = input("Endereço: ")
        cliente = PessoaFisica(nome, cpf, nascimento, endereco)
        self.clientes.append(cliente)
        print("Cliente criado com sucesso!")

    def criar_conta(self):
        cpf = input("CPF do cliente: ")
        cliente = self.buscar_cliente(cpf)
        if not cliente:
            print("Cliente não encontrado.")
            return
        conta = ContaCorrente(numero=self.numero_conta, cliente=cliente)
        cliente.adicionar_conta(conta)
        self.numero_conta += 1
        print(f"Conta criada com sucesso! Número: {conta.numero}")

    def depositar(self):
        cpf = input("CPF: ")
        cliente = self.buscar_cliente(cpf)
        if not cliente:
            print("Cliente não encontrado.")
            return
        conta = self.recuperar_conta(cliente)
        if not conta:
            return
        valor = float(input("Valor do depósito: "))
        transacao = Deposito(valor)
        cliente.realizar_transacao(conta, transacao)

    def sacar(self):
        cpf = input("CPF: ")
        cliente = self.buscar_cliente(cpf)
        if not cliente:
            print("Cliente não encontrado.")
            return
        conta = self.recuperar_conta(cliente)
        if not conta:
            return
        valor = float(input("Valor do saque: "))
        transacao = Saque(valor)
        cliente.realizar_transacao(conta, transacao)

    def extrato(self):
        cpf = input("CPF: ")
        cliente = self.buscar_cliente(cpf)
        if not cliente:
            print("Cliente não encontrado.")
            return
        conta = self.recuperar_conta(cliente)
        if not conta:
            return
        print("\n========== EXTRATO ==========")
        for t in conta.historico.transacoes:
            print(f"{t['data']} - {t['tipo']}: R$ {t['valor']:.2f}")
        print(f"Saldo atual: R$ {conta.saldo:.2f}")
        print("==============================")

    def listar_contas(self):
        for cliente in self.clientes:
            for conta in cliente.contas:
                print(conta)

    def executar(self):
        while True:
            self.menu()
            opcao = input("Escolha a opção: ")
            if opcao == "1":
                self.criar_cliente()
            elif opcao == "2":
                self.criar_conta()
            elif opcao == "3":
                self.depositar()
            elif opcao == "4":
                self.sacar()
            elif opcao == "5":
                self.extrato()
            elif opcao == "6":
                self.listar_contas()
            elif opcao == "0":
                print("Saindo do sistema...")
                break
            else:
                print("Opção inválida.")


if __name__ == "__main__":
    app = SistemaBancario()
    app.executar()
