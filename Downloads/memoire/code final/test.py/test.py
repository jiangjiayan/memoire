#!/usr/bin/env python3
import math
import random
from typing import Tuple, Iterator, Iterable
from rsa import*

from typing import Any

def continuedFraction(e, n):
    ret = []
    while n:
        ret.append(e // n)
        e, n = n, e % n
    return ret

def progressiveFraction(ret: Iterable[int]) -> Iterator[Tuple[int, int]]:
    (p1, p2, q1, q2) = (1, 0, 0, 1)
    convergentsList = []
    for q in ret:
        pn = q * p1 + p2
        qn = q * q1 + q2
        convergentsList.append([pn, qn])
        p2 = p1
        q2 = q1
        p1 = pn
        q1 = qn
    return convergentsList

def wienerAttack2(e, n) :
    res = progressiveFraction(continuedFraction(e, n))
    for (k, d) in res:
        m = random.randint(2,n)
        if  pow(m,e*d,n) == m%n :
                return d

def test_wienerAttack2(d):
    if d==wienerAttack2(e, n):
        test = 0
        print('attaque realisee')
        print('+++++++++++++La clée privée par lattque de wiener c"est +++++++++++++++++++++')
        print(wienerAttack2(e, n))
        test = test + 1
        return (test)
    else:
        print('attaque echouee')
        print('+++++++++++++La clé privée est NON IDENTIQUE  +++++++++++++++++++++')
        print(wienerAttack2(e,n))


if __name__ == '__main__':
    p = rsa.get_prime(512)
    q = rsa.get_prime(512)
    n = p * q
    OrLa = (p - 1) * (q - 1)
    for i in range ( 1, 7):
        d = random.randint(2, 1 / 3 * pow(n, 1 / 4))
        e = mod_1(d, OrLa)
        print('clé privite d')
        print(' %d\n' % d)
        print(test_wienerAttack2(d))
        print(' \n' )



