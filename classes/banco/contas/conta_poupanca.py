from contas.conta_bancaria import ContaBancaria

class ContaPoupanca(ContaBancaria):

	def __init__(self, numero, saldo, limite):
		super().__init__(numero, saldo)
		self.__limite = float(limite)

	def __str__(self):
		return f"Conta Poupança: Número: {self.numero}, Saldo: R$ {self.saldo}, Limite: R$ {self.__limite}"

	def get_limite(self):
		return self.__limite

	def set_limite(self, novo_limite):
		self.__limite = float(novo_limite)

	def saque(self, valor):
		if (self.saldo - valor) >= 0:
			self.saldo = self.saldo - valor
			print(f"Saque de R$ {valor} realizado! Saldo atual: R$ {self.saldo}")
		elif ((self.saldo - valor) * -1) <= self.__limite:
			print(f"Saque de R$ {valor} realizado! Saldo atual: R$ {self.saldo - valor}")
			self.saldo -= valor
		else:
			print(f"Incapaz de sacar R$ {valor}! Saldo atual: R$ {self.saldo}")

	def deposito(self, valor):
		self.saldo += float(valor)
		print(f"Depósito de R$ {valor} efetuado! Saldo atual: R$ {self.saldo}")

	limite = property(get_limite, set_limite)
