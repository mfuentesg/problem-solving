"""
Difficulty: Medium

Implement integer exponentiation. That is, implement the pow(x, y) function, where x and y are integers and returns x^y.
Do this faster than the naive method of repeated multiplication.
For example, pow(2, 10) should return 1024.
"""


# O(log n)
def my_pow(x, y):
    def internal(base, exp):
        if exp == 0:
            return 1
        if exp == 1:
            return base
        if exp == -1:
            return 1 / base

        # exp % 2 != 0 can be replaced by exp & 1 (odd operator)
        if exp % 2 != 0:
            result = internal(base, (exp - 1) / 2)
            return base * result * result

        result = internal(base, exp / 2)
        return result * result

    return internal(x, y)


assert my_pow(2, 10) == 2 ** 10
assert my_pow(2, -1) == 2 ** -1
assert my_pow(2, -2) == 2 ** -2
assert my_pow(0, 2) == 0
