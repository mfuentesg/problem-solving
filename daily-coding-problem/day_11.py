"""
Level: Medium

Implement an autocomplete system. That is, given a query string s and a set of all possible query
strings, return all strings in the set that have s as a prefix.

For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal]

Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.
"""


# This should be solved using Trie (Ref: https://cutt.ly/wjZl4U7)


class Node:
    value = None
    is_last = False

    def add(self, word):
        pass


def finder(items, search):
    return [item for item in items if item.startswith(search)]


elements = ['dog', 'deer', 'deal']
query = 'de'

print(finder(elements, query))
