# -*- coding: utf-8 -*-

from queue import Queue
from stack import Stack

pilha_s = Stack()

# Alimentando a pilha:
for _ in range(4):
	elemento = input("Adicione algo à pilha: ")
	pilha_s.push(elemento)

# Invertendo a pilha com uma fila:
fila = Queue()

for _ in range(len(pilha_s)):
	fila.insert(pilha_s.pop())

# Nova pilha com valores invertidos
pilha_invertida = Stack()

for _ in range(len(fila)):
	pilha_invertida.push(fila.remove())

# Mostra nova pilha com os valores da primeira invertidos.
print(pilha_invertida)
