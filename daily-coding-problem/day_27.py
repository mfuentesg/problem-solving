"""
Level: Easy

Given a string of round, curly, and square open and closing brackets, return whether the brackets are balanced
(well-formed).

For example, given the string "([])[]({})", you should return true.

Given the string "([)]" or "((()", you should return false.
"""


def is_balanced(string):
    stack = []
    for c in string:
        if c == '{' or c == '(' or c == '[':
            stack.append(c)
            continue

        if len(stack) == 0:
            return False

        bracket = stack.pop()
        conditions = {']': '[', '}': '{', ')': '('}
        if bracket != conditions.get(c, ''):
            return False

    if len(stack) != 0:
        return False

    return True


assert is_balanced('([])[]({})')
assert is_balanced('([{}])')
assert is_balanced('[]()[{}](())')
assert not is_balanced('([{])')
assert not is_balanced(')(')
assert not is_balanced('()(')
assert not is_balanced('asdf')

