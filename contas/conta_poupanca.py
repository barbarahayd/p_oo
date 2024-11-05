from contas.conta_bancaria import ContaBancaria

class ContaPoupanca(ContaBancaria):
    def __init__(self, numero, titular, saldo, limite, taxa_rendimento):
        super().__init__(numero, titular, saldo, limite)
        self.taxa_rendimento = taxa_rendimento

    def aplicar_rendimento(self):
        rendimento = self.saldo * self.taxa_rendimento
        self.deposito(rendimento)
        print("Rendimento de R$ {:.2f} aplicado ao saldo.".format(rendimento))

