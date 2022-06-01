#!/usr/bin/env python3
import math
import random
import time
import math


def pow_mod(p, q, n):
    res = 1
    while q :
        if q & 1:
            res = (res * p) % n
        q >>= 1
        p = (p * p) % n
    return res

M = int(input("message:"))
e = int(input("e:"))
n = int(input("n:"))
C = pow_mod(M, e, n) 
print('\n on peut obtenir les chiffrés：\n%d\n'%C)
    


    


