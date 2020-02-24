# DATA STRUCTURES -> Linked Lists - insert and removal
# Same code as the used in 'linked-lists.py' file, but now with insert and remove functions.

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self._size = 0

    def _getnode(self, index):
        pointer = self.head
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("list index out of range")
        return pointer

    def append(self, elem):
        if self.head:
            # If there is any element in the list.
            pointer = self.head
            while pointer.next:
                pointer = pointer.next
            pointer.next = Node(elem)
        else:
            # If there is no elements in the list.
            self.head = Node(elem)
        self._size += 1

    def __len__(self):
        """Returns the lenght of the list."""
        return self._size

    def __getitem__(self, index):
        pointer = self._getnode(index)
        if pointer:
            return pointer.data
        raise IndexError("list index out of range")

    def __setitem__(self, index, elem):
        pointer = self._getnode(index)
        if pointer:
            pointer.data = elem
        else:
            raise IndexError("list index out of range")

    def index(self, elem):
        pointer = self.head
        i = 0
        while pointer:
            if pointer.data == elem:
                return i
            pointer = pointer.next
            i += 1
        raise ValueError(f"{elem} is not in list.")

    def insert(self, index, elem):
        node = Node(elem)
        if index == 0:
            node.next = self.head
            self.head = node
        else:
            pointer = self._getnode(index - 1)
            node.next = pointer.next
            pointer.next = node
        self._size += 1


lst = LinkedList()
lst.append(8)
lst.append('Bryan')
lst.append(222)
lst.insert(1, 'Success')
print(f"Lenght is {len(lst)}.")
print(f"Index of Bryan is: {lst.index('Bryan')}")
[print(lst[_]) for _ in range(len(lst))]
