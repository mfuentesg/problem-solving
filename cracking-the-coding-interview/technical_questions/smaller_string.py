# -*- coding: utf-8 -*-

"""
Given a smaller string `s` and a bigger string `b`, design an
algorithm to find all permutations of the shorter string within
the lower one print location of each permutation.

Example:
s = abbc
b = cbabadcbbabbcbabaabccbabc
"""


def get_counters(word):
    counters = dict()
    for letter in word:
        counters[letter] = 1 if letter not in counters else counters[letter] + 1
    return counters


def solve(smaller, bigger):
    base_counters = get_counters(smaller)
    last_visited = 0
    current_position = 0

    counters = base_counters.copy()

    while len(smaller) + last_visited <= len(bigger):
        letter = bigger[current_position]

        if letter not in counters or counters.get(letter, 0) == 0:
            last_visited = current_position + 1 if letter not in counters else last_visited + 1
            current_position = last_visited
            counters = base_counters.copy()
            continue

        counters[letter] = counters[letter] - 1
        current_position = current_position + 1

        if current_position == len(smaller) + last_visited:
            print("found at position `{}` - substring `{}`".format(
                last_visited, bigger[last_visited:last_visited + len(smaller)]
            ))
            last_visited = last_visited + 1
            current_position = last_visited
            counters = base_counters.copy()


s = "abbc"
b = "qwerouqweiruqweoiruqoweiruqowieruoqweiur"

solve(s, b)
