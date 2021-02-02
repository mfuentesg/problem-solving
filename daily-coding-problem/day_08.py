"""
Level: Easy

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
    if node is None:
        return 0

    if node.left is None and node.right is None:
        return 1

    if node.right is None and node.left.value == node.value:
        return 1 + unival_count(node.left)

    if node.left is None and node.right.value == node.value:
        return 1 + unival_count(node.right)

    extra = 1 if node.value == node.left.value and node.right.value == node.left.value else 0
    return extra + unival_count(node.left) + unival_count(node.right)


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


bt1 = Node(0, Node(1), Node(0, Node(1, Node(1), Node(1)), Node(0)))
bt2 = Node(1, right=Node(1, right=Node(1, right=Node(1))))

assert unival_count(bt1) == 5
assert unival_count(bt2) == 4
