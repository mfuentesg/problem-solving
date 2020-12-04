# -*- coding: utf-8 -*-

"""
Given two sorted arrays, find the numbers of elements in common. The arrays are the same length and
each has distinct elements.

i.e
A = [13,27,35,40,49,55,59]
B = [17,35,39,40,55,58,60]

common elements are: [35,40,55]
"""


def solution_1(list_a, list_b):
    counter = 0
    for i in range(len(list_a)):
        for j in range(len(list_b)):
            if list_a[i] == list_b[j]:
                print('found', list_a[i])
                counter = counter + 1
    return counter


def solution_2(list_a, list_b):
    position_a = 0
    position_b = 0
    counter = 0

    while position_a != len(list_a) and position_b != len(list_b):
        a = list_a[position_a]
        b = list_b[position_b]

        if a == b:
            print('found', a)
            counter = counter + 1
            position_a = position_a + 1
            position_b = position_b + 1
        elif a > b:
            position_b = position_b + 1
        else:
            position_a = position_a + 1

    return counter


A = [13, 27, 35, 40, 49, 55, 59]
B = [17, 35, 39, 40, 55, 58, 60]

print('total items', solution_1(A, B))
print('total items', solution_2(A, B))
