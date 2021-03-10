from contas.conta_corrente import ContaCorrente
from contas.conta_poupanca import ContaPoupanca


def testar_conta_corrente():
	print("\n[\t\tTestanto Conta Corrente\t\t]\n")
	conta_c = ContaCorrente(numero="4002-8922", saldo=1000, taxa_de_operacao=12.5)
	print(conta_c)
	conta_c.deposito(9000)
	conta_c.saque(12000)
	conta_c.saque(9000)

def testar_conta_poupanca():
	print("\n[\t\tTestando Conta Poupança\t\t]\n")
	conta_p = ContaPoupanca(numero="4002-8923", saldo=5000, limite=1000)
	print(conta_p)
	conta_p.deposito(5000)
	conta_p.saque(12500)
	conta_p.saque(10500)
	conta_p.saque(500)
	conta_p.saque(1000)

def main():
	testar_conta_corrente()
	testar_conta_poupanca()

if __name__ == '__main__':
	main()
