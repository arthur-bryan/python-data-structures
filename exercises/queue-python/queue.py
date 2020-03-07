class Queue:

    def __init__(self):
        self.data = []
        self.size = 0

    def add_item(self, value):
        self.data.append(value)
        self.size += 1

    def del_item(self, value):
        i = 0
        while i != self.data.index(value):
            self.add_item(self.data[i])
            i += 1
        for j in range(0, i + 1):
            self.data.pop(0)
            self.size -= 1


    def get_itens(self):
        return self.data

    def len(self):
        return self.size

    def __repr__(self):
        return f"Queue: {self.data}"
