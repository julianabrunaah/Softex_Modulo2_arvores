class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Filaa:
    def __init__(self):
        self.first = None
        self.last = None
        self._size = 0

    def push(self, elem):
        node = Node(elem)
        if self.last is None:
            self.last = node
        else:
            self.last.next = node
            self.last = node

        if self.first is None:
            self.first = node

        self._size = self._size + 1

    # remover da fila
    def pop(self):
        if self._size > 0:
            elem = self.first.data
            self.first = self.first.next
            if self.first is None:
                self.last = None
            self._size = self._size - 1
            return elem
        raise IndexError("The Filaa is empty")

    # observar o primeiro da fila
    def peek(self):
        if self._size > 0:
            elem = self.first.data
            return elem
        raise IndexError("The Filaa is empty")

    def __len__(self):
        return self._size

    def __repr__(self):
        if self._size > 0:
            r = ""
            pointer = self.first
            while(pointer):
                r = r + str(pointer.data) + " "
                pointer = pointer.next
            return r
        return "Empty Filaa"

    def __str__(self):
        return self.__repr__()


