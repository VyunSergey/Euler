import numpy as np


def fibonacci(n):
    if n < 1:
        return 0
    if n == 2 or n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci_f(n):
    sqr = float(np.sqrt(5))
    f1 = (1 + sqr) / 2
    f2 = (1 - sqr) / 2
    if n < 1:
        return 0
    if n == 2 or n == 1:
        return 1
    return (f1**n - f2**n) / sqr


if __name__ == '__main__':
    num = 10
    print(fibonacci_f(num))
