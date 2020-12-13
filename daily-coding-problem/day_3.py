"""
Given the root to a binary tree, implement serialize(root), which serializes the tree into a string,
and deserialize(s), which deserializes the string back into the tree.

For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
"""


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def serialize(root):
    if not root:
        return 'none'

    left = serialize(root.left)
    right = serialize(root.right)

    return '(' + root.val + ',' + left + ',' + right + ')'


def deserialize(data):
    print(data)


# "('root', ('left', 'left.left', None), ('right', None, None))"
node = Node('root', Node('left', Node('left.left')), Node('right'))

# print("('root', ('left', 'left.left', None), ('right', None, None))")
print(deserialize(serialize(node)))

#
#
# assert deserialize(serialize(node)).left.left.val == 'left.left'
