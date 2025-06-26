class conta:
    def __init__(self,nro_agencia,saldo):
        self._saldo = saldo  # Atributo privado
        self.nro_agencia = nro_agencia  # Atributo público

    def depositar(self, valor):
          self._saldo += valor
          # Método para depositar dinheiro (a ser implementado)
           
    def sacar(self, valor):
       self._saldo -= valor
       
    def consultar_saldo(self):
        #...
        return self._saldo   

conta = conta("0001", 100)
conta.depositar(50)  # Isso causará um erro, pois depositar não está implementado
print(conta.nro_agencia)  # Saída: 0001, pois nro_agencia é público
print(conta.consultar_saldo())  # Saída: 100, pois consultar_saldo retorna o saldo