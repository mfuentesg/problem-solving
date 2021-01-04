# -*- coding: utf-8 -*-

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    def __init__(self):
        self.capacity = 50
        self.size = 0
        self.buckets = [None] * self.capacity

    def __hash(self, key):
        hash_sum = 0
        for i, c in enumerate(key):
            hash_sum = (hash_sum + (i + len(key)) ** ord(c)) % self.capacity
        return hash_sum

    def insert(self, key, value):
        self.size = self.size + 1
        index = self.__hash(key)

        node = self.buckets[index]
        if not node:
            self.buckets[index] = Node(key, value)
        else:
            while node.next:
                node = node.next
            node.next = Node(key, value)

    def find(self, key):
        if self.size == 0:
            return None

        index = self.__hash(key)
        node = self.buckets[index]
        if not node:
            return None

        while node.next and node.key != key:
            node = node.next

        return None if not node else node.value

    def remove(self, key):
        if self.size == 0:
            return None

        prev = None
        index = self.__hash(key)
        node = self.buckets[index]

        if not node:
            return None

        while node.next and node.key != key:
            prev = node
            node = node.next

        if node is None:
            return None

        if prev is None:
            self.buckets[index] = None
        else:
            prev.next = node.next

        self.size -= 1
        return node.value


ht = HashTable()
ht.insert('hello', '1')
ht.insert('hello', '2')

print('value', ht.find('hello'))
print('remove', ht.remove('hello'))
print('value', ht.find('hello'))
