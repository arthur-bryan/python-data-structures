from linkedlist import LinkedList
from node import Node
import os

list = LinkedList()

node1 = Node('Bryan')
node2 = Node(18)
node3 = Node(True)
node4 = Node(3.40)


node1.next = node2
node2.next = node3
node3.next = node4

list.head = node1
list.tail = node4

def before_after(list):
	os.system('clear')
	print("		----- BEFORE -----\n")
	list.show()
	print("\n		Run...\n")
	list.insert("Test", 1)
	print("\n\n		----- AFTER -----\n")
	list.show()

before_after(list)
