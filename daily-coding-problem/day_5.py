"""
cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that
pair.

For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

Given this implementation of cons:

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair
Implement car and cdr.
"""


def cons(a, b):
    def pair(f):
        return f(a, b)

    return pair


def car(pair):
    def get_element(a, _):
        return a

    return pair(get_element)


def cdr(pair):
    def get_element(_, b):
        return b

    return pair(get_element)


print('car', car(cons(3, 4)))
print('cdr', cdr(cons(3, 4)))
