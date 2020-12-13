"""
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
"""

k = 10
l = [10, 15, 3, 7]
d = dict()

for index, item in enumerate(l):
    d[item] = index

for item in l:
    if d.get(abs(k - item)):
        print('found', item, 'and', abs(k - item))
        break
