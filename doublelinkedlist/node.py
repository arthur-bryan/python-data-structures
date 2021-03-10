class Node:

	def __init__(self, data=None, next=None, prev=None):
		""" The constructor method of the Node.
			Args:
				data: The data that the node will hold.
				next: The next node.
				prev: The previous node.
		"""
		self.data = data
		self.next = next
		self.prev = prev

	def __str__(self):
		""" The magic method for an string representation of the object.
			Return:
				self.data(str):  The data of the node represented as string.
		"""
		return str(self.data)

