from random import randint

class Node:

    def __init__(self, data=None, next=None):
        """ The constructor method of the Node.
            Args:
                data: The data that the node will hold.
                next: The next node.
        """
        self.data = data
        self.next = next

    def __str__(self):
        """ The magic method for an string representation of the object.
            Return:
                self.data(str):  The data of the node represented as string.
        """
        return str(self.data)



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
        data = []
        pointer = self.head
        while pointer is not None:
            data.append(pointer.data)
            pointer = pointer.next
        print(data)

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


## Adicione a implementação do algoritmo de ordenação (merge sort ou quicksort usando essas estruturas)

def partition(array, low, high):
    s_index = (low-1)
    pivot = (array[high] + array[low]) / 2
    for i in range(low, high):
        if array[i] <= pivot:
            s_index = s_index+1
            array[s_index], array[i] = array[i], array[s_index]
    array[s_index+1], array[high] = array[high], array[s_index+1]
    return (s_index+1)


def quick_sort(array, low, high):
    if len(array) == 1:
        return array
    if low < high:
        partition_index = partition(array, low, high)
        quick_sort(array, low, partition_index-1)
        quick_sort(array, partition_index+1, high)


def generate_100_nodes(min_node_data, max_node_data):
	""" min_node_data(int): minimun value possible of a node
		max_node_data(int): maximum value possible of a node
		nodes(list): the genarated nodes (class Node)
	"""
	nodes = [Node(randint(min_node_data, max_node_data)) for _ in range(100)]
	for i in range(len(nodes)-1):
		nodes[i].next = nodes[i+1]
	return nodes


nodes = generate_100_nodes(0, 400)
linked_list = LinkedList()
linked_list.head = nodes[0]
linked_list.tail = nodes[-1]

print("Linked List before ordenation:")
linked_list.show()

quick_sort(linked
