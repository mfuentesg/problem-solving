"""
Level: Medium

Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it
can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.
"""


def counter(message):
    # checking last k elements, to avoid string duplication
    memo = {}

    def internal(data, k):
        if k == 0:
            return 1

        if k in memo:
            return memo[k]

        pointer = len(data) - k
        if data[pointer] == '0':
            return 0

        result = internal(data, k - 1)
        if k >= 2 and int(data[pointer:pointer + 2]) <= 26:
            result = result + internal(data, k - 2)
        memo[k] = result

        return result

    return internal(message, len(message))


assert counter('001') == 0
assert counter('0') == 0
assert counter('') == 1
assert counter('10') == 1
assert counter('123') == 3
assert counter('27623') == 2
assert counter('1111111111111111111111111111111111111111111111') == 2971215073
