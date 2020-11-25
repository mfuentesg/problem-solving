# -*- coding: utf-8 -*-

"""
Given an array of distinct integer values, count the number of pairs
of integers that have difference `k`.
For example, given the array {1,7,5,9,2,12,3} and difference k=2

Pairs: (1,3), (3,5), (5,7), (7,9)

Assumptions:
- k is a positive number
- A[i] is a positive number
"""

# Solution 1 - Brute force => O(n^2)
def brute_force(A, k):
    counter = 0
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            if abs(A[i] - A[j]) == k:
                counter += 1
                print('pair found ({},{})'.format(A[i], A[j]))
    return counter

# Solution 2 - Optimal solution => O(n)
def optimal_solution(A, k):
    counter = 0
    numbers = {n:i for (i,n) in enumerate(A)}

    for n in A:
        if n-k in numbers:
            counter = counter+1
            print('pair found ({},{})'.format(n, n-k))

        if n+k in numbers:
            counter = counter+1
            print('pair found ({},{})'.format(n, n+k))

        numbers.pop(n)

    return counter

A = [1,7,5,9,2,12,3]
print('brute force pairs count: ', brute_force(A, 2))
print('optimal solution pairs count: ', optimal_solution(A, 2))
