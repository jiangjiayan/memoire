#!/usr/bin/env python3
import math
# Return the continued fractions expansions of x / y
def continuedFraction(x, y):
    ret = []
    while y:
        ret.append(x // y)
        x, y = y, x % y
    return ret
#print(continuedFraction(6792605526025, 9449868410449))
def expand(ctnf):
    _ctnf = ctnf
    _ctnf.reverse()
    numerator = 0
    denominator = 1
    for x in _ctnf:
        numerator, denominator = denominator, x * denominator + numerator
    return (denominator, numerator)#on changer denominator et numerator,parce que la varable de denomiator est numerator
        


# Return the list of n progressive fraction
def progressiveFraction(x, y):
    cfe = continuedFraction(x, y)
    cfeL = len(cfe)
    ret = []
    for i in range(1, cfeL):
        ret.append(expand(cfe[0 : i]))
    return ret
#print(progressiveFraction(6792605526025, 9449868410449))
# Solve the equation: ax^2 +bx + c = 0
def solve(a, b, c):
    par = math.isqrt(b * b - 4 * a * c)
    return (-b + par) //(2 * a), (-b - par) // (2 * a)



def wienerAttack(e, n):
     res = progressiveFraction(e, n)
     for (k, d) in res:
         if k == 0 : continue
         if (e * d - 1) % k != 0:continue
         phi = (e * d - 1) // k
         p, q = solve(1, -(n - phi + 1), n)
         if p * q == n:
             print ("on trouve! ! !")
             print("p",p)
             print("q",q)
             print("d",d)
             print("k",k)
             print("n",n)
             return




wienerAttack(86880973085700484032684906494609155783772897240397849343305958144720386048789258609544917091857183170005382276545722526685237044833261693117331652863286200706364134644897710942216619334736037829701438655129122920576527333972808613198018808728097598511367834902116582824275882047021332161023624267202890643003, 131386565059911127827339869544089907948921833111420794539967346304392039211359564929246673435279223481617141445495833546587274996796732172208764594232181675817441889969672531022012627284260698466781962687034274952796865519227159401593404871998436453336254678873022572569784315084608574032429679624419043562111
)
