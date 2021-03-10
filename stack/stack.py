class Stack:

	def __init__(self):
		self.data = []

	def __str__(self):
		return str(self.data)

	def is_empty(self):
		return len(self.data) == 0

	def push(self, element):
		self.data.append(element)

	def pop(self):
		if self.is_empty():
			return "Can't pop. The stack is empty."
		return self.data.pop()

	def __len__(self):
		return len(self.data)

	def top(self):
		if self.is_empty():
			return "Stack is empty."
		return self.data[-1]
