from contas.conta_bancaria import ContaBancaria
from contas.conta_poupanca import ContaPoupanca
from contas.conta_corrente import ContaCorrente

def main():
    # instanciando uma conta bancária comum
    conta1 = ContaBancaria(numero="123", titular="Alice", saldo=1000, limite=500)
    print("\n--- Conta Bancária ---")
    conta1.extrato()
    conta1.deposito(200)
    conta1.extrato()
    conta1.saque(150)
    conta1.extrato()

    # instanciando uma conta poupança com rendimento mensal
    conta_poupanca = ContaPoupanca(numero="456", titular="Bob", saldo=1500, limite=300, taxa_rendimento=0.02)
    print("\n--- Conta Poupança ---")
    conta_poupanca.extrato()
    conta_poupanca.aplicar_rendimento()  # Aplica o rendimento de 2%
    conta_poupanca.extrato()

    # instanciando uma conta corrente com taxa de manutenção
    conta_corrente = ContaCorrente(numero="789", titular="Agustinho", saldo=500, limite=200, taxa_manutencao=20)
    print("\n--- Conta Corrente ---")
    conta_corrente.extrato()
    conta_corrente.descontar_taxa()  # desconta a taxa de manutenção
    conta_corrente.extrato()

    # teste transferência entre contas
    print("\n--- Transferência ---")
    conta1.transferencia(100, conta_corrente)
    conta1.extrato()
    conta_corrente.extrato()

if __name__ == "__main__":
    main()
