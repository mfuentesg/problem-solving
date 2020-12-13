# -*- coding: utf-8 -*-

class HashTable:
    def __init__(self):
        self.items = []

    def __hash(self, key):
        return hash(key) % len(self.items)

    def put(self, key, value):
        self.items[self.__hash(key)] = value

    def __str__(self):
        print(self.items)


ht = HashTable()

ht.put('hello', 'yo!')
ht.put('hello', 'yo!')
ht.put('hello', 'yo!')
ht.put('hello', 'yo!')

print(ht)
