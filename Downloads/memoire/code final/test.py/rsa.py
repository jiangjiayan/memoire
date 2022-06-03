#!/usr/bin/env python3
import math
import random
import time
import math


def pow_mod(p, q, n):
    '''
    calculer (p^q) mod rapide

    '''
    res = 1
    while q:
        if q & 1:
            res = (res * p) % n
        q >>= 1
        p = (p * p) % n
    return res


def gcd(a, b):
    while a != 0:
        a, b = b % a, a
    return b


def mod_1(x, n):
    x0 = x
    y0 = n
    x1 = 0
    y1 = 1
    x2 = 1
    y2 = 0
    while n != 0:
        q = x // n
        (x, n) = (n, x % n)
        (x1, x2) = ((x2 - (q * x1)), x1)
        (y1, y2) = ((y2 - (q * y1)), y1)
    if x2 < 0:
        x2 += y0
    if y2 < 0:
        y2 += x0
    return x2


def probin(w):
    list = []
    list.append('1')
    for i in range(w - 2):
        c = random.choice(['0', '1'])
        list.append(c)
    list.append('1')
    res = int(''.join(list), 2)
    return res


def prime_miller_rabin(a, n):  # on test si n est premier ,method miller-rabin
    ensemblepremier = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41
                       , 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97)
    for y in ensemblepremier:
        if n % y == 0:
            return False

    if pow_mod(a, n - 1, n) == 1:
        d = n - 1
        q = 0
        while not (d & 1):
            q = q + 1
            d >>= 1
        m = d

        for i in range(
                q):  # 0~q-1, tout d'abord on va trouver le plus petit a^u，et puis on le fait grandir jusqu'à a^((n-1)/2)
            u = m * (2 ** i)  # u = 2^i * m
            tmp = pow_mod(a, u, n)
            if tmp == 1 or tmp == n - 1:
                return True
        return False
    else:
        return False
def prime_test(n, k):
    while k > 0:
        a = random.randint(2, n - 1)
        if not prime_miller_rabin(a, n):
            return False
        k = k - 1
    return True
def get_prime(w):
    while True:
        prime_number = probin(w)
        for i in range(50):
            u = prime_test(prime_number, 5)
            if u:
                break
            else:
                prime_number = prime_number + 2 * (i)
        if u:
            return prime_number
        else:
            continue







