from contas.conta_bancaria import ContaBancaria

class ContaCorrente(ContaBancaria):
    def __init__(self, numero, titular, saldo, limite, taxa_manutencao):
        super().__init__(numero, titular, saldo, limite)
        self.taxa_manutencao = taxa_manutencao

    def descontar_taxa(self):
        if self.saldo >= self.taxa_manutencao:
            self.saque(self.taxa_manutencao)
            print("Taxa de manutenção de R$ {:.2f} descontada.".format(self.taxa_manutencao))
        else:
            print("Saldo insuficiente para descontar a taxa de manutenção.")