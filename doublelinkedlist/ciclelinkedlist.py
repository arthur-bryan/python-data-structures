from node import Node

class ListaCircular:

    def __init__(self):
        self.cabeca = None
        self.cauda = None

    def len(self):
        tamanho = 0
        if self.cabeca is not None:
            tamanho += 1
            atual = self.cabeca
            while atual is not self.cauda:
                tamanho += 1
                atual = atual.next
        return tamanho

node1 = Node(2)
node2 = Node(5)
node3 = Node('Bryan')
node4 = Node(3.14)
node1.next = node2
node1.prev = node4
node2.next = node3
node2.prev = node1
node3.next = node4
node3.prev = node2
node4.next = node1

lista = ListaCircular()
lista.cabeca = node1
lista.cauda = node4
print(lista.len())
