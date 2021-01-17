"""
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
"""


def finder(elements, target):
    d = dict()

    for index, item in enumerate(elements):
        d[item] = index

    for index, item in enumerate(elements):
        value = d.get(abs(target - item))
        if index != value and value is not None:
            print('found', item, 'and', abs(target - item))
            break


# finder([10, 15, 3, 7], target=10)
finder([10, 10, 3, 7], target=20)
