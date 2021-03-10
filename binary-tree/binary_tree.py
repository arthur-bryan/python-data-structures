class BinaryTree:

	def __init__(self, root):
		self.root = root

	def in_order(self, node):
		if node is None:
			return
		if node.left:
			print('(', end="")
			self.in_order(node.left)
		print(node.data, end="")
		if node.right:
			self.in_order(node.right)
			print(')', end="")

	def show_expression(self, node, expression=[]):
		if node is None:
			return
		if node.left:
			expression.append('(')
			self.show_expression(node.left, expression)
		expression.append(node.data)
		if node.right:
			self.show_expression(node.right, expression)
			expression.append(')')
		string = ''
		for i in expression:
			string += str(i)
		return str(string)

	def calculate_expression(self, expression):
		return eval(expression)
