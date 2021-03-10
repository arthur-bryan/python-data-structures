from contas.conta_bancaria import ContaBancaria

class ContaCorrente(ContaBancaria):

	def __init__(self, numero, saldo,  taxa_de_operacao):
		super().__init__(numero, saldo)
		self.__taxa_de_operacao = float(taxa_de_operacao)

	def __str__(self):
		return f"Conta Corrente: Número: {self.numero}, Saldo: {self.saldo}, Taxa de operação: R${self.taxa_de_operacao}"

	def get_taxa(self):
		return self.__taxa_de_operacao

	def set_taxa(self, nova_taxa):
		self.__taxa_de_operacao = nova_taxa

	def deposito(self, valor):
		valor_com_taxa = valor - self.__taxa_de_operacao
		self.saldo += valor_com_taxa
		print(f"Depósito de R$ {valor} efetuado! Saldo atual é de R$ {self.saldo}." +
			  f" (Taxa: R$ {self.__taxa_de_operacao})")

	def saque(self, valor):
		valor_com_taxa = valor + self.__taxa_de_operacao
		if (self.saldo - valor_com_taxa) >= 0:
			self.saldo -= valor_com_taxa
			print(f"Saque de R$ {valor_com_taxa} realizado! Saldo atual: R$ {self.saldo}." +
				  f" (Taxa: R$ {self.__taxa_de_operacao})")
		else:
			print(f"Incapaz de realizar saque de R$ {valor_com_taxa}! Saldo disponível: R$ {self.saldo}." +
				  f" (Taxa: R$ {self.__taxa_de_operacao})")
			return

	taxa_de_operacao = property(get_taxa, set_taxa)
