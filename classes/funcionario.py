class Funcionario:

	def __init__(self, nome, departamento, salario, data_entrada, rg):
		self.nome = str(nome)
		self.departamento = str(departamento)
		self.salario = float(salario)
		self.data_entrada = str(data_entrada)
		self.rg = str(rg)

	def mudar_departamento(self, departamento_origem, departamento_destino):
		if self.departamento == departamento_origem:
			self.departamento = departamento_destino
		else:
			print("Departamento atual inválido!")

	def	get_nome(self):
		return self.nome

	def get_salario(self):
		return '{:.2f}'.format(float(self.salario))

	def get_rg(self):
		return self.rg

	def set_salario(self, novo_valor):
		self.salario = novo_valor

	def receber_aumento(self, porcentagem):
		try:
			porcentagem = float(porcentagem)
		except ValueError:
			print("Porcentagem de aumento inválida!")
		else:
			if float(porcentagem) > 0:
				self.salario = '{:.2f}'.format(self.salario * (1 + (porcentagem/100)))
			else:
				print("Porcentagem de aumento deve ser maior que 0!")


	def calcular_ganho_anual(self):
		return float(self.salario) * 12
