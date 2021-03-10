from linkedlist import LinkedList
from node import Node


node1 = Node("a")
node2 = Node("a")

node1.next = node2
node2.prev = node1

lista = LinkedList()

lista.head = node1
lista.tail = node2

lista.show()

lista.remover_todas_ocorrencias("a")

print()
lista.show()
print(lista.head)
print(lista.tail)
