# -*- coding: utf-8 -*-

def binary_search(elements, target):
    left = 0
    right = len(elements) - 1

    while left <= right:
        mid = (right + left) // 2
        current = elements[mid]

        if current == target:
            return mid
        if current < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


print(binary_search([-1, 1, 2, 3, 4, 5, 9, 11, 25, 100], 101))
