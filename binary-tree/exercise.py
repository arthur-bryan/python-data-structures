from binary_tree import BinaryTree
from node import Node
import operator

def is_operator(x):
	operators = {'+': operator.add , '-': operator.sub, '*': operator.mul, '/': operator.truediv}
	if x in operators:
		return operators[x]
	else:
		return False

node1 = Node(12, None, None)
node2 = Node('+', None, None)
node3 = Node('*', None, None)
node4 = Node(10, None, None)
node5 = Node('-', None, None)
node6 = Node('/', None, None)
node7 = Node(7, None, None)
node8 = Node(20, None, None)
node9 = Node(2, None, None)

node2.left = node1
node2.right = node3
node3.left = node4
node3.right = node5
node5.left = node6
node5.right = node7
node6.left = node8
node6.right = node9

tree = BinaryTree(node2)


expression = tree.show_expression(tree.root)
print(expression)

print(tree.calculate_expression(expression))
