"""
A unival tree (which stands for "universal value") is a tree where all nodes under it have the same
value.

Given the root to a binary tree, count the number of unival subtrees.
For example, the following tree has 5 unival subtrees:

unival: 5
   0
  / \
 1   0
    / \
   1   0
  / \
 1   1


unival: 4
 1
  \
   1
    \
     1
      \
       1
"""


def unival_count(node):
    pass


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


bt1 = Node(0, Node(1), Node(0, Node(1, Node(1), Node(1)), Node(0)))
bt2 = Node(1, right=Node(1, right=Node(1, right=Node(1))))

assert unival_count(bt1) == 5
assert unival_count(bt1) == 4
