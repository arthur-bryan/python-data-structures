from queue import Queue
from random import randint, choice
from time import sleep

class Evento:

	grupo_c = ['Colisão', 'Atualização da Tela', 'Particulas']
	grupo_b = ['Lógica do Jogo', 'Inteligência Artificial', 'Simulação Física']
	grupo_a = ['Teclado', 'Mouse', 'Internet']

	def __init__(self, nome):
		self.nome = nome
		self.prioridade_grupo = None	# 0 à 1, quanto menor o número, maior a prioridade
		self.prioridade_nome = None	# 0 à 1, quanto menor o número, maior a prioridade

	def __str__(self):
		return str(self.nome)

	def set_priority(self):
		if self.nome in self.grupo_c:
			self.prioridade_grupo = 0
			self.prioridade_nome = self.grupo_c.index(self.nome)
		elif self.nome in self.grupo_b:
			self.prioridade_grupo = 1
			self.prioridade_nome = self.grupo_b.index(self.nome)
		elif self.nome in self.grupo_a:
			self.prioridade_grupo = 2
			self.prioridade_nome = self.grupo_a.index(self.nome)
		else:
			pass

	def get_priority(self):
		return self.prioridade_grupo, self.prioridade_nome

