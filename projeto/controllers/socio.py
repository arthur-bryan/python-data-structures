class Socio:
	def __init__(self, nome, cargo, ramal):
		self.__nome = nome
		self.__cargo = cargo
		self.__ramal = ramal

	@property
	def nome(self):
		return self.__nome

	@property
	def cargo(self):
		return self.__cargo

	@property
	def ramal(self):
		return self.__ramal
