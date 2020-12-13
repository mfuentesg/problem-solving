# -*- coding: utf-8 -*-

class Node:
    def __init__(self, data):
        self.next = None
        self.data = data


class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            n = self.head
            while n.next:
                n = n.next
            n.next = Node(data)

    def __str__(self):
        n = self.head
        elements = list()
        while n:
            elements.append(n.data)
            n = n.next
        return '({})'.format(', '.join(map(str, elements)))


ll = LinkedList()
ll.add(1)
ll.add(2)
ll.add(3)
ll.add(4)
ll.add(5)

print(ll)
