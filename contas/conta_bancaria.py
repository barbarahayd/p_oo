class ContaBancaria:

    def __init__(self, numero, titular, saldo, limite):
        print("Construindo o objeto... {}".format(self))
        self.numero = numero
        self._titular = titular
        self.saldo = saldo
        self._limite = limite

    def extrato (self):
        print("Titular: {}\nSaldo: R$ {:.2f}".format(self.titular, float(self.saldo)))

    def deposito(self, valor):
        self.saldo = self.saldo + valor

    def saque(self, valor):
        self.saldo = self.saldo - valor

    def transferencia(self, valor, destino):
        self.saque(valor)
        destino.deposito(valor)
        print("Transferencia de R${} realizado com sucesso".format(valor))

    @property
    def titular(self):
        return self._titular

    @property
    def limite(self):
        return float(self._limite)

    @limite.setter
    def limite(self, valor):
        self._limite = valor

    @titular.setter
    def titular(self, valor):
        self._titular = valor