class Node:

	def __init__(self, data, left, right):
		self.data = data
		self.left = left
		self.right = right

	def __str__(self):
		return str(self.data)
