def fib_recursive(n):
    if n == 1 or n == 2:
        return 1
    return fib_recursive(n - 1) + fib_recursive(n - 2)


def fib_memoize(n):
    memo = {}

    def internal(nn):
        if memo.get(nn):
            return memo[nn]

        result = 1 if nn == 1 or nn == 2 else internal(nn - 1) + internal(nn - 2)
        memo[nn] = result
        return result

    return internal(n)


def fib_bottom_up(n):
    if n == 1 or n == 2:
        return 1
    memo = {1: 1, 2: 1}
    for i in range(3, n + 1):
        memo[i] = memo[i - 1] + memo[i - 2]
    return memo[n]


print('fib_recursive', fib_recursive(35))
print('fib_memoize', fib_memoize(35))
print('fib_bottom_up', fib_bottom_up(10000))
