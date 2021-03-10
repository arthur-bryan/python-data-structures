class Queue:

	def __init__(self):
		self.data = []

	def __str__(self):
		return str(self.data)

	def __len__(self):
		return len(self.data)

	def is_empty(self):
		return len(self.data) == 0

	def insert(self, value):
		self.data.append(value)

	def remove(self):
		if not self.is_empty():
			return self.data.pop(0)
		else:
			print("Queue is empty.")

	def remove_value(self, value):
		if not self.is_empty():
			position = self.data.index(value)
			for i in range(0, position + 1):
				self.data.pop(0)

	def start(self):
		if self.is_empty():
			return ("The queue is empty.")
		else:
			return self.data[0]

	def end(self):
		if self.is_empty():
			return ("The queue is empty.")
		else:
			return self.data[-1]
