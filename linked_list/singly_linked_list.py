class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        node = Node(data)
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = node
        else:
            self.head = node

    def print(self):
        current = self.head
        if current is None:
            return print('Linked list empty.')
        while current is not None:
            print(current.data, end=' ')
            current = current.next
        print()
