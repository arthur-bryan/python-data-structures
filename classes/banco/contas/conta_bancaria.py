from abc import ABC, abstractmethod

class ContaBancaria(ABC):

	def __init__(self, numero, saldo):
		self.__numero = numero
		self.__saldo = float(saldo)

	@abstractmethod
	def saque(self, valor):
		pass

	@abstractmethod
	def deposito(self, valor):
		pass

	def get_numero(self):
		return self.__numero

	def set_numero(self, novo_numero):
		self.__numero = novo_numero

	def get_saldo(self):
		return self.__saldo

	def set_saldo(self, novo_saldo):
		self.__saldo = novo_saldo

	numero = property(get_numero, set_numero)
	saldo = property(get_saldo, set_saldo)
