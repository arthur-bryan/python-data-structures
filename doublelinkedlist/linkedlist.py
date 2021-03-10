from node import Node

class LinkedList:

	def __init__(self):
		self.head = None
		self.tail = None

	def __len__(self):
		counter = 0
		pointer = self.head
		while pointer != self.tail:
			pointer = pointer.next
			counter += 1
		counter += 1
		return counter

	def show(self):
		""" Show the elements of the list. """

		if self.head is None:
			print("The list is empty!")
			return
		pointer = self.head
		while pointer is not None:
			print(pointer.data)
			pointer = pointer.next

	def delete(self, value):
		""" Delete the value if it's on the list (just the first occurrence).

			Args:
				value: The value tu be deleted if found.
		"""
		if self.head is None:
			print("The list is empty!")
			return
		pointer = self.head
		size = len(self)
		if value == pointer.data:
			self.head = pointer.next
			pointer = None
			return
		while pointer is not None:
			if value == pointer.data:
				break
			previous_node = pointer
			pointer = pointer.next
		if pointer is None:
			return
		previous_node.next = pointer.next
		pointer = None

	def search(self, value):
		""" Verifies if the value is in the list.

			Args:
				value: The value to be searched.

			Returns:
				The return value: True if value was found, False otherwise.
		"""
		pointer = self.head
		if pointer is None:
			print("The list is empty!")
			return
		while pointer is not None:
			pointer = pointer.next
			if pointer.next is None:
				return False
		if value == pointer.data:
			return True
		return False

	def update(self, value, new_value):
		""" Update the data of a node (all occurrences).

			Args:
				value: The current data of the node.
				new_value: The new data for the node.
		"""
		if self.head is None:
			print("The list is empty!")
			return
		pointer = self.head
		size = len(self)
		if pointer == self.tail and pointer.data == value:
			pointer.data = new_value
		else:
			while size:
				if value == pointer.data:
					pointer.data = new_value
				pointer = pointer.next
				size -= 1

	def insert(self, value, index):
		""" Inserts a node with the specified value at the specified position.

			Args:
				value: The data of the new node.
				index (int): the position to insert the new node (starts at 0)
		"""
		new_node = Node(value)
		size = len(self)
		pointer = self.head
		if index > (size):
			raise IndexError('List index out of range')
		elif (self.head is None) and (0 == index):
			self.head = self.tail = new_node
			return
		elif 0 == index:
			new_node.next = self.head
			self.head = new_node
			return
		elif size == index:
			self.tail.next = new_node
			self.tail = new_node
			return
		previous_node = None
		while index != 0:
			previous_node = pointer
			pointer = pointer.next
			index -= 1
		new_node.next = pointer
		pointer = new_node
		previous_node.next = new_node

	def remover_todas_ocorrencias(self, elemento):
		atual = anterior = self.head
		if self.tail.data == elemento:
			self.tail = self.tail.prev
			self.tail.next = None
		while atual != None and atual.data == elemento:
			self.head = atual.next
			atual = self.head
		while atual != None:
			while atual != None and atual.data != elemento:
				anterior = atual
				atual = atual.next
			if atual == None:
				return
			anterior.next = atual.next
			atual = anterior.next

