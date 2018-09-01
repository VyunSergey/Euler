import numpy as np


def is_prime(a):
    for b in range(2, int(np.sqrt(a)) + 1, 1):
        if a % b == 0:
            return False
    return True


def prime_n(n):
    if n < 1:
        print('Error')
        return -1
    if n == 1:
        return 2
    p = prime_n(n - 1) + 1
    while not is_prime(p):
        p += 1
    return p


def list_primes_n(n):
    primes = []
    for m in range(n):
        primes.append(prime_n(m + 1))
    return primes


def quad(a, b, x):
    return x**2 + a*x + b


def quad_primes(a, b):
    n = 0
    while is_prime(abs(quad(a, b, n))):
        n += 1
    return n


if __name__ == '__main__':
    num = 168

    prime_lst = list_primes_n(num)
    print(prime_lst)
    print()

    quad_primes_lst = []
    for i in range(-999, 1000, 1):
        for j in prime_lst:
            if quad_primes(i, j) > 70:
                quad_primes_lst.append((i, j, quad_primes(i, j)))

    print(quad_primes_lst)
    print(-61 * 971)
