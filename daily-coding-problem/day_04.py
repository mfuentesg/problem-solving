"""
Given an array of integers, find the first missing positive integer in linear time and constant space.
In other words, find the lowest positive integer that does not exist in the array.

The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
"""


def finder(elements):
    items = dict()
    for index, element in enumerate(elements):
        if element < 1:
            continue
        items[element] = index

    max_element = max(elements)  # O(n)
    for i in range(1, max_element):
        if items.get(i) is None:
            return i
    return max_element + 1


assert finder([3, 4, -1, 1]) == 2
assert finder([3, 4, 2, 1]) == 5
assert finder([1, 2, 0]) == 3
