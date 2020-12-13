# -*- coding: utf-8 -*-

def binary_search(elements, target):
    left = 0
    right = len(elements) - 1
    mid = (right + left) // 2


print(binary_search([-1, 1, 2, 3, 4, 5, 9, 11, 25, 100]), 25)
