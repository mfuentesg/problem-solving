"""
Difficulty: Easy

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
"""


def finder(nums, target):
    d = dict()

    for index, item in enumerate(nums):
        if target - item in d and index != d[target - item]:
            return [index, d[target - item]]
        d[item] = index


# finder([10, 15, 3, 7], target=10)
print(finder([1, 6, -7], target=-1))
print(finder([10, 10, -6, 7], target=20))

print(finder([95, 4, -90], 5))
