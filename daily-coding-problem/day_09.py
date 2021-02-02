"""
Level: Hard

Given a list of integers, write a function that returns the largest sum of non-adjacent numbers.
Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5]
should return 10, since we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant space?
"""

"""
[2, 4, 6, 2, 5]
    [2, 6]
    [2, 2]
    [2, 5]

    [4, 2]
    [4, 5]

    [6, 5]

    [2, 6, 5]
    []


[2, 3]
[1, 2, 3]



[5, 4, 6, 2, 2, 7]
 ^     ^     ^  ^

 [5, 6, 2]
 [5, 6, 7]
 [5, 2, 7]
 [5, 2]


"""
