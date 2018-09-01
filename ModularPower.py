import numpy as np


def mod(base, md):
    return base % md


def mod_pow(base, pw, md):
    res = 1
    i = pw
    while i > 0:
        res = mod(res * base, md)
        i = i - 1
    return res


def digits_sum(base, pwr):
    digits = []
    n = pow(base, pwr)
    pw = int(int(np.log10(float(n))))
    for i in range(pw + 1, 0, -1):
        dif = mod_pow(base, pwr, pow(10, i)) - mod_pow(base, pwr, pow(10, i - 1))
        dg = dif / pow(10, i - 1)
        digits.append(int(dg))
    print(base, '^', pwr, '=', n)
    print(digits)
    return sum(digits)


if __name__ == '__main__':
    # print(2**100, digits_sum(2, 100))
    arr = []
    num = 2**1000
    print(digits_sum(2, 1000))
