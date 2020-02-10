# DATA STRUCTURES -> Linked Lists - node and chained allocation


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


node1 = Node(3)     # Instance of the Node class
node2 = Node(19)    # Another instance of the Node class
print(node1.data)   # Prints the data of the node1 object
node1.next = node2  # The 'next' of node1 object, now is the node2 object
print(node1.next.data)  # Prints the data of node1.next (node2)
