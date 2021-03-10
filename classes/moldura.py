from retangulo import Retangulo

class Moldura(Retangulo):

	def __init__(self, base, altura, espessura, tipo_madeira):
		super().__init__(base, altura)
		self.__espessura = espessura
		self.__tipo_madeira = tipo_madeira

	@property
	def area(self):
		base = (self.base * 2) - (self.__espessura * 4)
		base += self.altura * 2
		return (base * self.__espessura) / 100


	@property
	def valor(self):
		if self.__tipo_madeira == 1:
			return 20 * self.area
		elif self.__tipo_madeira == 2:
			return 15 * self.area
		elif self.__tipo_madeira == 3:
			return 40 * self.area
		else:
			print("Tipo de madeira inválido!")
			return False
